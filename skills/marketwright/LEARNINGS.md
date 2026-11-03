# Learnings: marketwright

Procedural lessons for [SKILL.md](SKILL.md). Research findings live in [RESEARCH.md](RESEARCH.md); every change is logged in [CHANGELOG.md](CHANGELOG.md); test runs in [TESTS.md](TESTS.md); state in `evergreen.json`. Format and write-time gate: MAINTENANCE.md.

Write an entry the moment a real signal happens: a user correction, the same error twice, a discovered workaround, an environment fact, a failed test or a failure in use. Trigger and Hypothesis are required.

## Active

### L-20261103-1 `reddit-only-through-rss` · 2026-11-03 · active
- Trigger: the creation research could not fetch any reddit.com page (rules pages included) through WebFetch; everscout's RSS probe read all 31 subreddits the same day.
- Hypothesis: Reddit blocks the fetch tool's agent; public RSS still answers but carries no subscriber counts or rules.
- Rule: check a community is alive with `everscout.py probe` (RSS); its self-promotion rule stays marked "search" until someone reads the rules page in a browser.
- Scope: skill · Status: active · helpful 1 · harmful 0 · last_confirmed 2026-11-03
