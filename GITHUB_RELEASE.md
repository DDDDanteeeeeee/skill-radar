# GitHub Release Plan

## Repository Name

`skill-radar`

## Tagline

Stop installing random agent skills. Install the ones that fit your work.

## Description

Demand-first recommender for Codex, Claude, and agent skill stacks. Classifies skills, skillpacks, MCP servers, tools, templates, and role packs before recommending install, selective install, record, defer, pass, or reject.

## Suggested GitHub Topics

- `agent-skills`
- `codex`
- `claude-code`
- `skill-recommender`
- `ai-agents`
- `developer-tools`
- `mcp`
- `llm-tools`

## First Release

Release tag: `v0.1.0`

Artifacts:

- `skill-radar.skill`
- `skill-radar-github-source.zip`

## README Positioning

Lead with:

> Stop collecting random agent skills. Install the ones that fit your real work.

Then show the six recommendation states and one short example.

## Growth Loop

1. Publish repository.
2. Ask users to submit candidate repos through the issue template.
3. Turn good issues into eval cases.
4. Add more classification examples.
5. Use stars as the first adoption signal.

## Do Not Publish

- Internal pilot records.
- Private project paths.
- User memory files.
- Obsidian vault contents.
- Credentials, cookies, tokens, or account data.

## Launch Checklist

- [ ] Repository is public.
- [ ] README first screen explains the problem.
- [ ] `SKILL.md` frontmatter says `name: skill-radar`.
- [ ] `python scripts/preflight_check.py .` returns `READY_FOR_GITHUB_RELEASE`.
- [ ] First release includes `.skill` and source zip artifacts.
- [ ] Issue template asks for candidate URL, installed overlap, desired workflow, and permission boundary.
