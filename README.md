# Skill Radar

**Stop collecting random agent skills. Install the ones that fit your real work.**

Skill Radar is an agent skill that recommends which Codex, Claude, or agent skills you should install, selectively install, record, defer, pass, or reject.

It does not rank repositories by stars. It first asks: what does this user or project actually need?

## Why This Exists

Agent skills are becoming a real ecosystem. That creates a new problem: people can now install dozens of impressive-looking skills that overlap, add permissions, or never get used.

Skill Radar is a decision layer:

- It infers your real user/project demand.
- It checks overlap with what you already have.
- It distinguishes true skills from MCP servers, tools, templates, role packs, and workflow ideas.
- It explains permission, runtime, and data risk before installation.
- It produces a record you can keep in a team or personal skill library.

## When To Use

Use Skill Radar when you ask:

- "Should I install this skill?"
- "Which skills do I actually need?"
- "This GitHub repo looks useful. Is it a real skill?"
- "I found a skillpack. Which parts should I install?"
- "Do I already have this capability?"
- "Recommend a skill stack based on my project."

It also works for mixed candidate lists: one true skill, one skillpack, one MCP server, one tool, and one template resource.

## Recommendation States

| State | Meaning |
| --- | --- |
| `install-now` | Strong fit, clear near-term use, acceptable risk. |
| `install-selective` | Useful package, but install only specific modules. |
| `record-only` | Useful reference or future component, not something to install now. |
| `defer` | Plausible value, but missing real use case, runtime, credentials, or validation. |
| `pass` | Existing capabilities already cover it or the value is too small. |
| `reject` | Unsafe, misleading, abandoned, or not worth tracking. |

## Install From GitHub

Clone or download this repository, then copy the skill folder into your local skills directory.

Example layout:

```text
skill-radar/
  SKILL.md
  README.md
  references/
  examples/
  evals/
  scripts/
```

If your environment supports `.skill` files, use the packaged `skill-radar.skill` artifact.

## Quick Example

Prompt:

```text
I found a GitHub MCP server. I already have a GitHub plugin, but I may need GitHub automation later. Should I install it?
```

Expected recommendation:

```text
State: defer

Why: This is an MCP server, not a normal skill. It may become valuable for cross-tool GitHub automation, but the existing GitHub plugin covers normal repository work. Run a scoped read-only pilot only when a concrete automation workflow appears.
```

## Privacy Model

Skill Radar is privacy-bound by default.

| Level | Default | Example |
| --- | --- | --- |
| H0 current context | Allowed | Current prompt and files already in scope |
| H1 active project memory | Allowed when relevant | Project notes, local docs, previous evaluation records |
| H2 user-provided history | Needs scoped direction | Exported chats or archives |
| H3 sensitive/private stores | Explicit approval required | Browser profiles, credentials, account data, raw customer data |

See [privacy-permission-model.md](references/privacy-permission-model.md).

## Demo

See [public-demo-pack.md](examples/public-demo-pack.md) for a private-data-free demo with mock candidates and expected decisions.

## Preflight

Run:

```bash
python scripts/preflight_check.py .
```

Expected result:

```text
READY_FOR_GITHUB_RELEASE
```

## Market Position

Skill Radar is designed for the GitHub distribution path:

- Open repository.
- Easy download and local configuration.
- Transparent skill instructions.
- Public demo and evals.
- Stars as the first adoption signal.

The product promise is simple: **fewer, better skill installs.**

## License

MIT.
