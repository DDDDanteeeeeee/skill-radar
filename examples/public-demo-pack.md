# Public Demo Pack

This demo uses mock data only. It is safe to publish.

## Mock User Profile

User: independent builder maintaining a personal AI workflow library.

Current projects:

1. A research vault with notes, PDF summaries, and reusable project memory.
2. A content intelligence workflow that tracks web pages and social discussions.
3. A product prototype that needs PRD, roadmap, launch, and presentation assets.

Installed capabilities:

- GitHub connector.
- PDF/document skills.
- Presentation skills.
- Basic web browsing and page cleaning.
- One general writing/humanizing skill.

Preference:

- Fewer, better installs.
- No account connection without approval.
- Record useful candidates for later instead of installing everything.
- Prefer local or reversible pilots before broad adoption.

## Mock Candidates

| Candidate | Type | Expected Decision |
| --- | --- | --- |
| `example/frontend-slides-skill` | True skill | `install-now` if presentation work is active |
| `example/product-management-skillpack` | Skillpack | `install-selective` for execution/planning modules |
| `example/github-mcp-server` | MCP server | `defer` until cross-tool GitHub automation is concrete |
| `example/pdf-tool-platform` | Non-skill tool | `record-only` or `defer` until batch PDF operations appear |
| `example/web-clipper-templates` | Template/resource | `record-only` because it is not an agent skill |

## Expected Output Shape

The answer should:

1. State the inferred demand profile.
2. Rank candidates by user fit, not popularity.
3. Classify candidate types correctly.
4. Compare installed overlap.
5. Include permission and runtime risk.
6. Include an Evidence Ledger.
7. Give a next action for each candidate.

## Example Summary

| Candidate | State | Reason |
| --- | --- | --- |
| `example/frontend-slides-skill` | `install-now` | Active presentation workflow and low overlap with document-only skills. |
| `example/product-management-skillpack` | `install-selective` | Product workflow is real, but only execution/planning modules are needed now. |
| `example/github-mcp-server` | `defer` | Existing GitHub connector covers normal use; MCP write access needs a concrete automation case. |
| `example/pdf-tool-platform` | `defer` | Strong PDF operation layer, but runtime and file-governance cost require a real batch task. |
| `example/web-clipper-templates` | `record-only` | Useful template resource, not a skill to install. |

## Demo Evidence Ledger

- History sources used: H0 mock profile only.
- Candidate sources checked: mock candidate descriptions only.
- Unverified assumptions: no real repository freshness, license, or maintenance check.
