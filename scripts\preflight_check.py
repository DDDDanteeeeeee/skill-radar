from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "evals/evals.json",
    "examples/public-demo-pack.md",
    "references/privacy-permission-model.md",
    "references/market-refresh-2026-06-15.md",
    "references/packaging-preflight.md",
    "scripts/preflight_check.py",
]

FORBIDDEN_PATTERNS = [
    r"C:\\Users\\",
    r"agent_memory",
    r"CoCreationOS\\data",
    r"BEGIN .*PRIVATE",
    r"API[_-]?KEY\s*=",
    r"token\s*=",
    r"cookie\s*=",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files(root: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")
    return errors


def check_skill_frontmatter(root: Path) -> list[str]:
    errors: list[str] = []
    text = read_text(root / "SKILL.md")
    if not text.startswith("---"):
        errors.append("SKILL.md must start with YAML frontmatter")
    if "name: skill-radar" not in text:
        errors.append("SKILL.md frontmatter must include name: skill-radar")
    match = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
    if not match:
        errors.append("SKILL.md missing description")
    elif len(match.group(1).strip()) < 120:
        errors.append("SKILL.md description should be specific enough for triggering")
    for required in ["History Review Protocol", "Recommendation States", "Evidence Ledger"]:
        if required not in text:
            errors.append(f"SKILL.md missing required phrase: {required}")
    return errors


def check_evals(root: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(read_text(root / "evals" / "evals.json"))
    evals = data.get("evals", [])
    if data.get("skill_name") != "skill-radar":
        errors.append("evals.json skill_name must be skill-radar")
    if len(evals) < 5:
        errors.append("evals.json should include at least 5 evals")
    for item in evals:
        if not item.get("prompt") or not item.get("expected_output"):
            errors.append(f"eval {item.get('id')} missing prompt or expected_output")
        if not item.get("assertions"):
            errors.append(f"eval {item.get('id')} missing assertions")
    return errors


def check_public_only(root: Path) -> list[str]:
    errors: list[str] = []
    if (root / "runs").exists():
        errors.append("public package must not include internal runs directory")
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if rel.as_posix() == "scripts/preflight_check.py":
            continue
        if path.suffix.lower() in {".skill", ".zip", ".png", ".jpg", ".jpeg", ".gif"}:
            continue
        try:
            text = read_text(path)
        except UnicodeDecodeError:
            continue
        for pattern in FORBIDDEN_PATTERNS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                errors.append(f"forbidden private or secret-like pattern in {rel}: {pattern}")
    return errors


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []
    errors.extend(check_required_files(root))
    if not errors:
        errors.extend(check_skill_frontmatter(root))
        errors.extend(check_evals(root))
        errors.extend(check_public_only(root))

    if errors:
        print("NOT_READY")
        for error in errors:
            print(f"- {error}")
        return 1

    print("READY_FOR_GITHUB_RELEASE")
    print(f"skill_dir={root}")
    print("checks=required_files,frontmatter,evals,public_only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
