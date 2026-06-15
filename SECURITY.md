# Security Policy

Skill Radar is a recommendation skill. It should not directly install packages, configure credentials, connect accounts, publish content, or mutate production systems.

## Report A Concern

Open a GitHub issue if you find:

- Instructions that encourage reading private files without authorization.
- Prompts that copy raw private history into public output.
- Dangerous install or credential-handling behavior.
- Repository evaluation logic that ignores permission or data-transfer risk.

## Design Boundary

The skill may recommend an install state. It must not execute installation unless the user explicitly authorizes that exact action in their own environment.

Sensitive context is H3 and requires explicit approval:

- Browser profiles.
- Credentials, cookies, tokens, or API keys.
- Account data.
- Private messages.
- Raw customer data.
- Payment or legal records.
