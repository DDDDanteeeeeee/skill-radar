# Privacy And Permission Model

## Principle

Skill Radar recommends skills from user/project context without turning that context into a data harvest.

Use the smallest context that can change the decision. Prefer summarized evidence over raw private content.

## History Levels

| Level | Name | Default | Examples | Required Handling |
| --- | --- | --- | --- | --- |
| H0 | Current context | Allowed | Current prompt, recent conversation, files the user is actively discussing | Use directly. Cite as current-context evidence. |
| H1 | Active project memory | Allowed inside the active project | Project docs, local notes, previous evaluation records | Read only relevant files. Summarize demand signals. |
| H2 | User-provided history | Needs scoped user direction | Exported chats, project archives, external notes | Confirm scope and purpose. Keep review read-only. |
| H3 | Sensitive/private stores | Explicit approval required | Browser profiles, credentials, account data, private messages, customer raw data, payment records | Stop and request purpose, scope, retention, and permission. |

## What To Record

Record:

- Source level used: H0, H1, H2, H3.
- Source type, not private raw text.
- Recurring demand inferred.
- Confidence level.
- Whether evidence may be stale.
- Unverified assumptions.

Avoid recording:

- Raw private conversations.
- Credentials, tokens, cookies, account identifiers, or customer data.
- Full browser/profile paths unless needed for a user-approved technical task.
- Sensitive source text copied into public demo files.

## Installation Boundary

Skill Radar may recommend install states, but it must not execute installation unless the user explicitly confirms the exact action.

High-risk actions requiring explicit confirmation:

- Installing a skill or plugin.
- Initializing runtime dependencies.
- Configuring API keys, tokens, cookies, or account links.
- Enabling write access.
- Publishing, sending messages, posting content, or deploying.
- Reading H3 sources.

## Public Packaging Boundary

Public examples must use mock data. A packaged version must not depend on:

- A specific user's Obsidian vault.
- A specific user's local memory files.
- Local absolute paths.
- Private project records.
- Installed skills that are not declared as optional inputs.

The public version can describe how to connect a user's own project memory, but that review remains permission-bound.
