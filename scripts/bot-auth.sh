#!/usr/bin/env bash
# bot-auth.sh — Switch git/gh identity to the GitHub App bot for PR creation.
# Usage: bash scripts/bot-auth.sh [activate|deactivate|status]

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$REPO_ROOT/.env"
TOKEN_CACHE="/tmp/.bot-token-cache"
REPO_SLUG="xlozinguez/ai-hype-watcher"

# Load .env
load_env() {
  if [[ ! -f "$ENV_FILE" ]]; then
    echo "Error: $ENV_FILE not found" >&2; exit 1
  fi
  set -a; source "$ENV_FILE"; set +a
  for var in GITHUB_APP_ID GITHUB_APP_INSTALLATION_ID GITHUB_APP_PRIVATE_KEY_PATH; do
    if [[ -z "${!var:-}" ]]; then
      echo "Error: $var not set in $ENV_FILE" >&2; exit 1
    fi
  done
  if [[ ! -f "$GITHUB_APP_PRIVATE_KEY_PATH" ]]; then
    echo "Error: PEM key not found at $GITHUB_APP_PRIVATE_KEY_PATH" >&2; exit 1
  fi
}

# Base64url encode (no padding)
b64url() {
  openssl base64 -e -A | tr '+/' '-_' | tr -d '='
}

# Generate JWT signed with the app's private key
generate_jwt() {
  local now
  now=$(date +%s)
  local iat=$((now - 60))
  local exp=$((now + 600))

  local header='{"alg":"RS256","typ":"JWT"}'
  local payload="{\"iss\":\"${GITHUB_APP_ID}\",\"iat\":${iat},\"exp\":${exp}}"

  local h_b64 p_b64 sig
  h_b64=$(echo -n "$header" | b64url)
  p_b64=$(echo -n "$payload" | b64url)
  sig=$(echo -n "${h_b64}.${p_b64}" | openssl dgst -sha256 -sign "$GITHUB_APP_PRIVATE_KEY_PATH" | b64url)

  echo "${h_b64}.${p_b64}.${sig}"
}

# Get or reuse cached installation access token
get_token() {
  # Check cache
  if [[ -f "$TOKEN_CACHE" ]]; then
    local expires_at
    expires_at=$(jq -r .expires_at "$TOKEN_CACHE" 2>/dev/null || echo "")
    if [[ -n "$expires_at" ]]; then
      local exp_epoch now_epoch
      exp_epoch=$(date -j -f "%Y-%m-%dT%H:%M:%SZ" "$expires_at" +%s 2>/dev/null || echo 0)
      now_epoch=$(date +%s)
      if (( exp_epoch - now_epoch > 300 )); then
        jq -r .token "$TOKEN_CACHE"
        return 0
      fi
    fi
  fi

  # Generate fresh token
  local jwt
  jwt=$(generate_jwt)
  local response
  response=$(curl -s -X POST \
    -H "Authorization: Bearer $jwt" \
    -H "Accept: application/vnd.github+json" \
    "https://api.github.com/app/installations/${GITHUB_APP_INSTALLATION_ID}/access_tokens")

  local token expires_at
  token=$(echo "$response" | jq -r .token)
  expires_at=$(echo "$response" | jq -r .expires_at)

  if [[ -z "$token" || "$token" == "null" ]]; then
    echo "Error: Failed to get installation token" >&2
    echo "$response" >&2
    exit 1
  fi

  # Cache it
  echo "{\"token\":\"$token\",\"expires_at\":\"$expires_at\"}" > "$TOKEN_CACHE"
  chmod 600 "$TOKEN_CACHE"
  echo "$token"
}

activate() {
  load_env
  echo "Generating installation access token..."
  local token
  token=$(get_token)

  # Set git identity (local to this repo)
  git -C "$REPO_ROOT" config user.name "ai-hype-watcher-bot[bot]"
  git -C "$REPO_ROOT" config user.email "${GITHUB_APP_ID}+ai-hype-watcher-bot[bot]@users.noreply.github.com"

  # Set remote URL with embedded token for push
  git -C "$REPO_ROOT" remote set-url origin "https://x-access-token:${token}@github.com/${REPO_SLUG}.git"

  echo "Bot identity activated."
  echo "  git user: ai-hype-watcher-bot[bot]"
  echo "  token cached at: $TOKEN_CACHE"
  echo ""
  echo "For gh commands, prefix with:"
  echo "  GH_TOKEN=\$(jq -r .token $TOKEN_CACHE) gh pr create ..."
}

deactivate() {
  # Restore git identity
  git -C "$REPO_ROOT" config user.name "Xavier Lozinguez"
  git -C "$REPO_ROOT" config user.email "xavier@lozinguez.com"

  # Restore remote URL
  git -C "$REPO_ROOT" remote set-url origin "https://github.com/${REPO_SLUG}.git"

  # Remove token cache
  rm -f "$TOKEN_CACHE"

  echo "Bot identity deactivated. Restored human identity."
}

status() {
  echo "=== Git Identity ==="
  echo "  user.name:  $(git -C "$REPO_ROOT" config user.name 2>/dev/null || echo '(not set)')"
  echo "  user.email: $(git -C "$REPO_ROOT" config user.email 2>/dev/null || echo '(not set)')"
  local url
  url=$(git -C "$REPO_ROOT" remote get-url origin 2>/dev/null || echo '(unknown)')
  # Redact token from URL
  echo "  remote:     $(echo "$url" | sed 's/x-access-token:[^@]*/x-access-token:***/')"
  echo ""
  echo "=== Token Cache ==="
  if [[ -f "$TOKEN_CACHE" ]]; then
    local expires_at
    expires_at=$(jq -r .expires_at "$TOKEN_CACHE" 2>/dev/null || echo "unknown")
    echo "  cached: yes"
    echo "  expires: $expires_at"
  else
    echo "  cached: no"
  fi
}

case "${1:-activate}" in
  activate)   activate ;;
  deactivate) deactivate ;;
  status)     status ;;
  *)          echo "Usage: $0 [activate|deactivate|status]" >&2; exit 1 ;;
esac
