---
title: "How we built passwordless authentication with Auth0 and Elixir/Phoenix"
date: '2020-04-19T12:10:31+00:00'
category: webclip
summary: 'Describes why a React Native app backed by Elixir/Phoenix adopted SMS-based passwordless login with Auth0 and Twilio, and details the backend design using JWTs and Guardian.'
tags: ["authentication", "jwt", "elixir-phoenix", "auth0"]
has_commentary: false
generated_by: "openai/gpt-5.1"
sources:
  - title: "How we built passwordless authentication with Auth0 and Elixir/Phoenix"
    url: "https://web.archive.org/web/20191212103812id_/https://www.madebymany.com/stories/how-we-built-passwordless-authentication-with-auth0-and-elixir-phoenix"
    kind: article
  - title: "Raw clipping (archived copy)"
    url: "https://github.com/thluiz/scholion/blob/main/clippings/2026-11/web-archive-org--passwordless-auth-with-auth0-elixir-phoenix.md"
    kind: repo
---

The article explains how a React Native app for a client’s employees moved from email/password login to passwordless SMS authentication. Employee data from an internal HR system is used to pre-create user accounts and restrict access to staff. Auth0 handles SMS-based identity verification via Twilio, issuing JWT access and refresh tokens that include the user’s phone number. The Elixir/Phoenix backend verifies Auth0 tokens, maps them to local users via a UserAuth schema, and then issues its own JWTs with permissions, using Guardian and Guardian DB for authorization, routing protection, and token revocation.

## Reading notes

- The team wanted a smooth, low-friction onboarding flow for an iOS/Android React Native app backed by an Elixir/Phoenix API running in Docker on AWS.
- Initial email/password auth caused problems: secure credential distribution, manual reset work, and confusion for users with multiple email addresses.
- Because the app targets employees, only staff should access it, which shaped the onboarding constraints and options.
- Integration with the client’s secure, non-cloud HR system lets them pre-generate accounts for all employees as they are added, and disable accounts for leavers.
- Using HR data means users do not re-enter personal details in the app, since those are already stored in the HR system.
- A QR-code-based login tied to manager-led induction was explored, avoiding usernames and passwords and using in-person contact.
- QR login was dropped due to practical issues: employees need to log out and back in without managers, and managers would have to reauthenticate staff when they change phones.
- The chosen flow relies on the HR phone number field: employees enter their mobile number, receive a one-time 6-digit SMS code, and log in if a matching account exists.
- If the backend cannot find a user with the submitted phone number, the app treats them as not matched and directs them to correct their number in the HR system.
- Auth0 is used for identity management and Twilio for sending SMS; Auth0’s JWT-based system underpins the passwordless flow.
- A Twilio account is created with a UK number (and later a US number for California testers), configured as a Programmable SMS Service with the app name as Alpha Sender ID.
- An Auth0 client is configured with a Passwordless SMS connection using the Twilio SID and auth token, including customized SMS message content.
- When a user enters a phone number, the app calls Auth0’s /passwordless/start endpoint with client_id, connection="sms", and phone_number.
- On success, Auth0 sends the 6-digit SMS code; the app then calls /oauth/ro with client_id, connection="sms", grant_type="password", username as phone number, password as verification code, and scope including "openid offline_access phone_number".
- A correct code yields an access token with configurable lifetime (set to 24 hours) and, because of "offline_access", a refresh token that does not expire and must be stored securely.
- Including "phone_number" in scope ensures the Auth0 token carries the phone number claim, which the Elixir backend uses to identify the user.
- With the Auth0 access token, the app knows the verified phone number but not yet whether the person is an employee.
- The app sends the Auth0 access token to the Elixir backend’s login endpoint, which looks up a user by phone number and logs them in as an employee if found.
- If no matching user is found, the backend authenticates them as an anonymous user and sends them to a waiting screen while still issuing a JWT for API access.
- The Elixir app issues its own JWTs instead of reusing Auth0’s, to separate concerns between identity verification and application-level authorization.
- Backend-issued tokens encode application-specific claims such as permissions, allowing future expansion to more granular permission levels.
- Issuing local tokens also makes it easier to swap or add other identity verification services later, without tying authorization to Auth0 alone.
- A has_one association is set from User to a UserAuth schema that models a user’s authentication method and identifiers.
- On a user’s first login, a UserAuth record is created with fields: method (currently always "phone number"), remote_id (the phone number), and auth0_id (Auth0’s unique user identifier like "sms|...").
- Both remote_id and auth0_id come from claims in the Auth0 token, ensuring backend records align with Auth0’s identity data.
- The Phoenix SessionController#create action receives the Auth0 JWT and uses Guardian to verify its signature against the stored Auth0 client public key.
- Auth0 is configured with an asymmetric signing algorithm, so the backend only needs the public key to verify tokens.
- The text highlights that JWT contents are only Base64-decoded, so claims are publicly readable and should not contain secrets unless JSON Web Encryption is used.
- After verifying the Auth0 token, the login_with_auth0_token function runs, fetching or creating the relevant UserAuth using the phone number and Auth0 ID.
- When UserAuth is created, the system attempts to associate it with an existing User sharing the same phone number, though such a user may not exist.
- With UserAuth in hand, login_with_auth0_token decides what JWT to issue by checking whether a UserAuth has an associated User via UserAuth.anon?.
- If the UserAuth is anonymous, the backend issues a token without permissions, allowing only limited API actions such as device registration for push notifications.
- If the user has an account, the backend issues a JWT with full permissions, marking them as an employee-level user.
- Once the app has a backend-issued token, it can call the API; anonymous users can only hit limited endpoints, while employee users access broader functionality.
- Phoenix Router plug pipelines enforce access rules; Guardian plugs are used across API routes for authentication and permission checks.
- Guardian.Plug.EnsureAuthenticated is applied globally to API routes to require a valid JWT for all API access.
- Guardian.Plug.EnsurePermissions is configured so that only tokens with employee: [:full] claims can access protected employee-only endpoints.
- A GuardianSerializer module is defined to link UserAuth records with tokens, making the associated UserAuth available in controller actions.
- Controller logic uses the associated UserAuth to enforce resource-level rules, such as limiting access so users can only retrieve their own user records.
- Guardian DB is used to persist issued tokens, track them, and revoke them when necessary, extending Guardian’s basic functionality.
- Since JWTs remain valid until expiry, the team sets token expiry to 24 hours to reduce frequent logins while keeping lifetime manageable.
- Guardian DB enables instant revocation of access for a user by invalidating tokens in the database, without waiting for expiry.
- Configuring Guardian DB involves adding its migration, defining repo and cleanup interval configuration, and adding its worker to the supervision tree.
- With that setup, the backend can programmatically revoke tokens, providing stronger security control over active sessions.
- The author invites readers to ask questions or comment via their Twitter handle or the company account.
