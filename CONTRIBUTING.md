# Contributing

Contributions are welcome when they improve recommendation quality, privacy, or install safety.

Good contributions:

- Better candidate classification rules.
- New public demo cases with mock data.
- More realistic eval prompts.
- Improved privacy and permission boundaries.
- Better install instructions for different agent environments.

Please avoid:

- Adding private user histories or real customer data.
- Adding credentials, cookies, tokens, or browser profile paths.
- Turning recommendations into automatic installs.
- Overfitting the skill to one user's local folder structure.

## Development Check

Run:

```bash
python scripts/preflight_check.py .
```

The expected result is:

```text
READY_FOR_GITHUB_RELEASE
```
