## [Unreleased] — 2026-06-18

### Features

- **Auto CHANGELOG workflow** — generates a grouped CHANGELOG entry on every merged PR and commits it back to the repo; subsequent fixes hardened token auth, trigger event (push → PR merge), and tool allowlist to avoid max-turns
- **Auto PR Description workflow** — automatically rewrites PR descriptions via Claude on pull-request open/edit events; requires `gh pr edit` permission and OIDC `id-token: write`
- **AI Code Review workflow** — runs Claude code-review on every PR; supports inline line-level comments (`--comment` flag) posted directly on the diff
- **Dependency Guard workflow** — compares `requirements.txt` against a checked-in baseline and fails the build on unexpected changes; includes initial `pandas` baseline entry
- **Coverage Summary workflow** — runs pytest with `pytest-json-report` and posts a pass/fail summary as a PR comment
- **Payments module** — new `payments.py` with `invoice_calculation`, `apply_late_fee`, `payment_reminder`, and business-rule tests for refunds and late fees
- **Math utils** — `math_utils.py` with basic arithmetic helpers
- **Demo functions** — `greet()` added to the baseline demo module

### Fixes

- Fixed Auto CHANGELOG YAML parse error caused by unquoted `if`-expression containing a colon
- Fixed Auto CHANGELOG trigger: switched from `push` (unsupported by the action) to `pull_request: closed` with `merged` guard
- Fixed Auto CHANGELOG tool allowlist: added `git-read` and file tools to prevent hitting the max-turns limit
- Fixed Auto CHANGELOG push: pass an explicit token because the default action credential is stripped before the git push step
