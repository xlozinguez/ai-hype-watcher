---
source_id: "187"
title: "Authentication Methods Compared: Basic, Bearer, OAuth2, JWT, and SSO"
creator: "Hayk Simonyan"
platform: "YouTube"
url: "https://www.youtube.com/watch?v=iX8g4LqF8p8"
date: "2026-02-18"
duration: "21:08"
type: "video"
tags: ["security", "infrastructure"]
curriculum_modules: ["06-strategy-and-economics"]
---

# 187: Authentication Methods Compared: Basic, Bearer, OAuth2, JWT, and SSO

> **Creator**: Hayk Simonyan | **Platform**: YouTube | **Date**: 2026-02-18 | **Duration**: 21:08

## Summary

A comprehensive walkthrough of authentication methods and frameworks, clarifying the distinctions that most developers conflate. Hayk Simonyan methodically covers the evolution from basic authentication through modern token-based systems, emphasizing that many concepts developers treat as interchangeable (JWT vs. bearer tokens, OAuth2 vs. authentication, SSO vs. authentication methods) are fundamentally different things serving different purposes.

The video progresses from the simplest methods (basic auth, digest auth, API keys) through session-based authentication, then into modern token-based approaches (bearer tokens, JWT, access/refresh tokens), authorization frameworks (OAuth2), identity layers (OpenID Connect), and user experience patterns (SSO). This progression mirrors the historical evolution of web security and helps viewers understand why each layer was added.

## Key Concepts

### Authentication vs. Authorization Confusion
The core confusion Simonyan addresses is that developers routinely mix up authentication methods, token formats, authorization frameworks, and UX patterns. JWT is a token format, not an authentication method. OAuth2 is an authorization framework, not authentication. SSO is a user experience pattern. Bearer is a token transmission pattern. Understanding these distinctions is essential for building secure systems.

### Basic Authentication Methods
The simplest approaches — basic auth (Base64-encoded credentials), digest auth (MD5-hashed credentials), and API keys (unique strings per client) — all share a fundamental limitation: credentials or keys are sent with every request. Basic auth is easily reversible without HTTPS. API keys have no built-in expiration and contain no embedded information, requiring database lookups for every validation.

### Session-Based vs. Token-Based Authentication
Session-based auth is stateful — the server must maintain a session store (typically Redis in production). This works well for traditional web apps but scales poorly for APIs and distributed systems. Token-based auth (JWT) flips this by making tokens self-contained and stateless — the server can verify a JWT's signature locally without hitting a database, reducing load and simplifying distributed architectures.

### Access and Refresh Token Pattern
Modern systems use two tokens: short-lived access tokens (15 minutes to 1 hour) for API calls and long-lived refresh tokens (days to weeks) for renewing access tokens. Refresh tokens must be stored in HTTP-only cookies (never localStorage) to prevent XSS attacks. When an access token expires, the client uses the refresh token to obtain a new one without requiring re-authentication.

### OAuth2 vs. OpenID Connect
OAuth2 answers "what can this app access on behalf of the user" — it is purely an authorization framework. The access token it returns proves the app can access resources but says nothing about who the user is. OpenID Connect adds an identity layer on top of OAuth2, returning an ID token (a JWT containing user identity) alongside the access token. This is what powers "Sign in with Google/GitHub/Microsoft" flows.

### SSO and Identity Protocols
Single Sign-On is a UX pattern, not an authentication method — it allows logging in once to access multiple services. Underneath, SSO uses identity protocols: SAML (XML-based, common in enterprise/legacy systems) or OpenID Connect (modern, JWT-based). Both are secure and relevant, but OIDC is the more modern approach used by services like Google.

## Practical Takeaways

- **Know what you are actually using**: JWT is a token format, bearer is a transmission pattern, OAuth2 is authorization, OIDC is authentication+identity, SSO is a UX pattern — stop conflating them
- **Use Redis for session storage in production**: In-memory sessions are lost on restart, file-system sessions do not scale, and Redis provides built-in key expiration
- **Never store refresh tokens in localStorage**: Always use HTTP-only cookies to prevent XSS attacks
- **Prefer stateless JWT for API authentication**: Reduces database load and simplifies distributed system design
- **OIDC over raw OAuth2 for user identity**: If you need to know who the user is (not just what they can access), use OpenID Connect which adds the ID token layer

## Notable Quotes

> "They treat JWT as an authentication method when in reality it's just a token format." — Hayk Simonyan

> "The access token just proves that the app can access your resources. But it doesn't tell the app who you are." — Hayk Simonyan

## Related Sources

- [017: Be Careful w/ Skills](017-primeagen-skills-security.md) — security considerations in AI tooling
- [191: LLM-Powered Deanonymization at Scale](191-ai-paper-slop-llm-deanonymization.md) — security and privacy implications of AI systems

## Related Curriculum

- [Module 06: Strategy & Economics](../curriculum/06-strategy-and-economics/README.md) — infrastructure and security foundations for AI-driven systems
