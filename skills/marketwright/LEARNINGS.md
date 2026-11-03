# Learnings: marketwright

Procedural lessons for [SKILL.md](SKILL.md). Research findings live in [RESEARCH.md](RESEARCH.md); every change is logged in [CHANGELOG.md](CHANGELOG.md); test runs in [TESTS.md](TESTS.md); state in `evergreen.json`. Format and write-time gate: MAINTENANCE.md.

Write an entry the moment a real signal happens: a user correction, the same error twice, a discovered workaround, an environment fact, a failed test or a failure in use. Trigger and Hypothesis are required.

## Active

### L-20261103-3 `trim-moved-the-trailer-case` · 2026-11-03 · active
- Trigger: T-20261103-4. Trimming the description and the freshness and maintenance text flipped trap-trailer from writing a cut list to asking intake questions in 3 of 3 runs.
- Hypothesis: the long description's "trailer and short-form cut list from gameplay clips" primed the model to produce the list without asking; the short version dropped it. It could also be run-to-run variance in the intake step.
- Rule: the description's job phrases stay as they are. A future trim touches the body only, and the case set is re-run in full before it is kept.
- Scope: skill · Status: active · helpful 0 · harmful 0 · last_confirmed 2026-11-03

### L-20261103-2 `fixtures-need-a-scaffold` · 2026-11-03 · active
- Trigger: T-20261103-3's first run: every agent in both arms reported the plugin's `evals/` folder on the sandbox's read-deny list, so cases that said "copy evals/fixtures/saltlight" could not start.
- Hypothesis: `claude plugin eval` hides the eval folders from the agent so it cannot read graders; fixtures there are hidden too.
- Rule: seed a fixture with a per-case `case.yaml` (`context: scaffold_script: fixture.sh`) and run with `--scaffold`; the prompt names the workspace folder, not the plugin path. `evergreen.py eval-export` does not write these files: re-add them after a re-export (copy of the fixture is embedded in fixture.sh; regenerate when the fixture changes). `--case` takes `*` globs but not `[..]` classes.
- Scope: skill · Status: active · helpful 1 · harmful 0 · last_confirmed 2026-11-03

### L-20261103-1 `reddit-only-through-rss` · 2026-11-03 · active
- Trigger: the creation research could not fetch any reddit.com page (rules pages included) through WebFetch; everscout's RSS probe read all 31 subreddits the same day.
- Hypothesis: Reddit blocks the fetch tool's agent; public RSS still answers but carries no subscriber counts or rules.
- Rule: check a community is alive with `everscout.py probe` (RSS); its self-promotion rule stays marked "search" until someone reads the rules page in a browser.
- Scope: skill · Status: active · helpful 1 · harmful 0 · last_confirmed 2026-11-03
