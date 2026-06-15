# Market Refresh - 2026-06-15

## Summary

The market supports a GitHub-first release for Skill Radar.

Agent skills are becoming a visible ecosystem, but the ecosystem has predictable pain points:

- Too many skills and skillpacks.
- Redundant or overlapping skills.
- Skills that do not improve outcomes unless they fit the project.
- Permission, runtime, and semantic supply-chain risk.
- Need for repository-aware and context-aware evaluation.

Skill Radar's position is therefore narrow and useful:

> Do not help users install more skills. Help them choose the right skills.

## Evidence

### 1. Skill ecosystems are already large

An arXiv 2026 study reports a dataset of 40,285 publicly listed skills and describes skills as reusable modules with triggers, procedural logic, and tool interactions. It also finds content concentration, redundancy, and safety risks.

Source: [Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large Language Model Functionality](https://arxiv.org/abs/2602.08004)

### 2. More skills do not automatically mean better performance

SWE-Skills-Bench tested 49 public software-engineering skills across real GitHub repositories. The abstract reports that 39 of 49 skills produced no pass-rate improvement, average gain was only +1.2%, and only a small group of specialized skills produced meaningful gains.

Source: [SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?](https://arxiv.org/abs/2603.15401)

Implication: Skill selection is the product. A recommender that accounts for domain fit and context compatibility has a real value proposition.

### 3. Repository-aware evaluation is a market gap

Another arXiv 2026 paper collected 238,180 unique skills from major platforms and GitHub. It reports that repository-aware context reduced suspicious classifications from scanner-heavy views and identifies real risks such as abandoned GitHub repository hijacking.

Source: [Context Matters: Repository-Aware Security Analysis of the Agent Skill Ecosystem](https://arxiv.org/abs/2603.16572)

Implication: Skill Radar should explicitly market "repository-aware, context-aware recommendations" instead of shallow keyword scanning.

### 4. `SKILL.md` is operational text, not passive docs

A 2026 arXiv paper on semantic supply-chain attacks argues that `SKILL.md` content affects discovery, selection, and governance. The abstract reports attack results against discovery, selection, and governance stages.

Source: [Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry](https://arxiv.org/abs/2605.11418)

Implication: Skill Radar's privacy, evidence, and risk sections are not decorative. They are part of trust positioning.

### 5. GitHub distribution fits the adoption loop

The strongest lightweight go-to-market loop is:

1. Publish a clean GitHub repository.
2. Make install and demo friction low.
3. Use README clarity to earn stars.
4. Convert stars, issues, and PRs into eval cases.
5. Improve recommendations from user-submitted examples.

## Positioning

Recommended GitHub tagline:

> A demand-first skill recommender for agent skill stacks.

Alternative:

> Stop installing random agent skills. Install the ones that fit your work.

## Target Users

- Codex/Claude power users collecting skills.
- Teams adopting agent workflows.
- Builders maintaining personal or team skill libraries.
- Developers evaluating GitHub repositories that may or may not be real skills.
- Security-conscious users who want permission and data-risk checks before installing third-party skills.

## GitHub README Hooks

Use these claims:

- "Not a marketplace. A decision layer."
- "Demand before repository."
- "Fewer, better installs."
- "Classifies skills, skillpacks, MCP servers, libraries, templates, and role packs."
- "Includes Evidence Ledger and privacy-bound history review."

Avoid these claims until proven by public users:

- "Best skill recommender."
- "Automatically finds every skill."
- "Guarantees safety."
- "Works with every marketplace."

## Launch Checklist

- Public repo name: `skill-radar`.
- README includes a one-screen explanation and one fast example.
- Public package includes mock demo only.
- No private local paths or internal pilot records.
- Add topics: `agent-skills`, `codex`, `claude-code`, `skill-recommender`, `ai-agents`, `developer-tools`.
- First GitHub issue templates should ask users to submit candidate repo, installed skills, desired workflow, and permission boundary.

## Current Recommendation

Proceed with GitHub-first packaging.

Do not publish internal pilot records. Publish:

- `SKILL.md`
- `README.md`
- privacy model
- public demo pack
- evals
- preflight script
- market note
- license
- contribution/security docs
