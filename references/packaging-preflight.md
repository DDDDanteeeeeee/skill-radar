# Packaging Preflight

This checklist defines the GitHub release boundary for Skill Radar.

## Required Files

- `SKILL.md`
- `README.md`
- `LICENSE`
- `CHANGELOG.md`
- `evals/evals.json`
- `examples/public-demo-pack.md`
- `references/privacy-permission-model.md`
- `references/market-refresh-2026-06-15.md`
- `references/packaging-preflight.md`
- `scripts/preflight_check.py`

## Public Package Rules

- Include mock demo only.
- Do not include internal pilot records.
- Do not include private user history.
- Do not include Obsidian vault paths, local memory paths, credentials, cookies, tokens, or account data.
- Do not imply automatic install, account connection, or publishing.

## Release Criteria

- `SKILL.md` frontmatter name is `skill-radar`.
- README explains the problem in the first screen.
- Demo uses mock data.
- Evals use public/mock prompts.
- Preflight returns `READY_FOR_GITHUB_RELEASE`.
- `.skill` artifact builds successfully if the active environment supports package generation.

## Check Command

```bash
python scripts/preflight_check.py .
```

Expected:

```text
READY_FOR_GITHUB_RELEASE
```
