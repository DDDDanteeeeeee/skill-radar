---
name: skill-radar
description: Recommend which agent or Codex skills a user should install, skip, defer, or record by first inferring their real project needs and existing capability overlap. Use this whenever the user asks which skills to install, whether a skillpack is worth it, whether a GitHub repository is a real skill, how to build a personal or team skill stack, or wants a risk-aware skill recommendation instead of a popularity-based answer.
license: MIT
---

# Skill Radar

## Purpose

Help users choose the right agent skills for their real situation.

Skill Radar is not a generic GitHub repository reviewer. It is a decision layer for skill adoption. It combines:

1. User and project demand inference.
2. Candidate skill or repository evaluation.
3. Existing capability overlap checking.
4. Permission, runtime, and workflow-fit judgment.
5. A clear recommendation state and next action.

## Core Rule

Start with the user's real need, not with the candidate repository.

A technically strong skill can still be the wrong choice if it duplicates existing capabilities, adds unnecessary permissions, does not match the user's current workflows, or has no realistic near-term use.

## Inputs To Inspect

Use the smallest relevant set:

- Current user request and recent conversation.
- Project files or memory that the user has already put in scope.
- Installed skills, plugins, scripts, and workflows, when available.
- Candidate repository README, `SKILL.md`, manifests, examples, package files, releases, issues, and license.
- Public market or ecosystem sources when the user asks for adoption, opportunity, or current market context.

Do not read unrelated private files just because they are accessible. Ask for authorization before reading sensitive histories, browser profiles, account data, credentials, private chats, customer data, or documents outside the relevant project.

## History Review Protocol

Use history only when it changes the recommendation. The goal is to infer demand patterns, not to collect user data.

| Level | Allowed by default? | Examples | Handling |
| --- | --- | --- | --- |
| H0 Current context | Yes | Current prompt, current conversation, files already attached or named | Use directly and cite as current-context evidence. |
| H1 Active project memory | Yes, if the project is in scope | Project docs, local notes, prior evaluation records | Read the smallest relevant files and summarize evidence. |
| H2 User-provided history | Only after the user points to it | Exported chats, project archives, external notes | Confirm scope, then review read-only. |
| H3 Sensitive/private stores | No, explicit approval required | Browser profile, credentials, account data, private messages, raw customer data | Stop and ask for purpose, scope, retention boundary, and permission. |

When using H1-H3 evidence, record source level, source type, inferred recurring need, confidence, and whether evidence may be stale.

## Decision Dimensions

Score each candidate with concise judgment rather than fake precision.

| Dimension | What To Judge |
| --- | --- |
| D1 User/project true demand | What recurring need appears in the user's current request, project, or authorized history? |
| D2 Existing capability overlap | Is the same capability already covered by installed skills, plugins, scripts, or workflows? |
| D3 Technical maturity | Is it maintained, documented, runnable, and backed by real implementation rather than only marketing? |
| D4 Workflow fit | Where does it sit: capture, research, planning, execution, QA, publishing, governance, or maintenance? |
| D5 Permission and data risk | Does it need credentials, external data transfer, write permissions, browser/session access, payments, or public publishing? |
| D6 Verification path | Can it be smoke tested locally or piloted with low risk? |
| D7 Operating cost | Does it add dependency weight, runtime setup, API cost, account setup, or cognitive clutter? |
| D8 Strategic value | Does it improve reusable workflows, team adoption, or future product packaging? |

Default weights:

- D1: 30%
- D2: 15%
- D3: 15%
- D4: 15%
- D5: 10%
- D6: 5%
- D7: 5%
- D8: 5%

Adjust weights when the user explicitly prioritizes speed, safety, cost, research depth, content production, or engineering automation.

## Candidate Classification

Classify the candidate before recommending action:

- `skill`: a single installable skill with `SKILL.md`.
- `skillpack`: multiple installable skills.
- `plugin-marketplace`: plugin bundle or marketplace with many skills/commands.
- `mcp-server`: MCP connection layer, not a skill.
- `cli-library`: CLI, SDK, or code library.
- `template-resource`: templates, examples, prompts, or vault resources.
- `workflow-idea`: useful process idea without installable runtime.
- `role-pack`: agent personas or role definitions.
- `unknown`: insufficient evidence.

## Recommendation States

Use one of these states:

- `install-now`: high fit, clear near-term use, acceptable risk, no better local substitute.
- `install-selective`: valuable package, but install only specific skills or modules.
- `record-only`: useful reference or future component, but not a skill or not needed now.
- `defer`: plausible value, but missing real use case, credentials, runtime, or validation.
- `pass`: existing capability already covers it, or value is marginal.
- `reject`: unsafe, unmaintained, misleading, or not worth future tracking.

If the candidate is already installed, explain whether to keep, disable, expand, or leave it untouched. Do not imply an install action happened unless the user explicitly confirmed it and it actually ran.

## Workflow

1. Restate the user's target outcome in one sentence.
2. Identify the evidence used for D1 user/project true demand.
3. List existing capabilities that overlap with the candidate.
4. Inspect the candidate's real implementation and maintenance signals.
5. Classify the candidate type.
6. Score the candidate across the decision dimensions.
7. Give the recommendation state and the shortest reason that changes the decision.
8. If useful, say where it belongs in the user's workflow or knowledge base.
9. If installation is recommended, state the exact module/path and permissions needed, but do not install without explicit user confirmation.

## Output Format

Use this structure by default:

```markdown
**Recommendation**
State: install-now | install-selective | record-only | defer | pass | reject
Score: x/10

**Why**
[2-4 sentences focused on the decision]

**User Demand Evidence**
- [history/project/current-request signal]
- Confidence: high | medium | low

**Fit And Overlap**
- Candidate type: [...]
- Existing capability: [...]
- Gap this candidate fills: [...]

**Risks**
- Permission/data/runtime risk: [...]
- Verification needed: [...]

**Evidence Ledger**
- History sources used: H0 | H1 | H2 | H3
- Candidate sources checked: [...]
- Unverified assumptions: [...]

**Next Action**
[exact next step: install module, record only, run pilot, defer, pass, or reject]
```

For multiple candidates, use a compact table first, then expand only the most important 1-3 decisions.

## Public Recording

When the user wants a reusable record, create a concise recommendation note that avoids private raw content. Include:

- Candidate name and URL.
- Candidate type.
- Recommendation state.
- Main user-demand signal.
- Overlap and risk summary.
- Next action.

## Safety Boundaries

- Never install, configure credentials, connect accounts, publish, send messages, or write production systems without explicit user confirmation.
- Treat history review as read-only and purpose-limited.
- Prefer summaries over copying private historical content.
- Mark unverifiable claims as unverified.
- For current market, legal, medical, financial, dependency, or security claims, verify with current sources before using them as a deciding reason.
