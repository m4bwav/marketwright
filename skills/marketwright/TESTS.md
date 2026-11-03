# Tests: marketwright

Test runs for [SKILL.md](SKILL.md). Cases live in `evals/evals.json`; unit tests for `mkw.py` in the repository's `tests/`. A test passes on evidence (a tool call in the trace, a file, a marker), never on the transcript's claim. Entry shape: `### T-YYYYMMDD-n · date · harness · env · passed/total`, failing cases one per line, then `led to:`. Newest first.

## Runs

### T-20261103-3 · 2026-11-03 · claude plugin eval under WSL2 Ubuntu (3 action cases x 3 runs each arm, --scaffold, --allow-tools Bash Write Edit, -j 6) · owner-pc WSL2 · 3/3 cases with skill
- First try (results 2026-11-03T02-02-03-309Z): both fixture cases 0.00 in both arms, environment: the eval sandbox denies reads of the plugin's `evals/` folders, so `evals/fixtures/saltlight` was unreachable. Fixed with a `case.yaml` + `fixture.sh` scaffold that writes `saltlight/store-page.md` into the workspace, and prompts that point at that folder.
- Second run (results 2026-11-03T02-05-13-807Z), about $5.10: action-plan-roblox with 1.00, without 0.00. action-plan-steam with 0.92 (one run's judge FAIL FAIL FAIL with a plan that did use 14 June Next Fest and a 10 May demo date), without 0.00. action-store-1 with 1.00, without 0.33 (bare Claude named the five rule breaks once it could read the page, but never wrote the file).
- Probe (no skill, no tools, store case): named 1 of 7 anchors; its checklist missed the capsule text rule, URL ban, AI disclosure, 5-tag minimum and trailer opening.
- worth: TRIM (pass 89% with, 0% without, margin 21; cost x1.82, turns x4.54, time x1.36). Recorded in evergreen.json.
- led to: trim proposal in HANDOFF (waits on Mark's yes, per evergreen-worth Step 4).

### T-20261103-2 · 2026-11-03 · claude plugin eval (9 cases x 3 runs each arm, judge sonnet, -j 6) · owner-pc Windows · 9/9 with skill
- trigger-1..3: with 1.00, without 0.00. decoy-1..3: 1.00 both arms (not invoked). About $2.33.
- trap-review-swap: with 1.00, without 0.67. trap-sockpuppet: 1.00 both. trap-trailer: with 1.00, without 0.00 (bare Claude planned the cut-feature cinematic). About $1.74.
- action-store-1, action-plan-steam, action-plan-roblox: NOT RUN (environment): the harness refuses a Bash grant on native Windows without a sandbox. Graders were written by hand (eval-export wrote none for placeholder file paths). Run them under WSL2 or with the evergreen-tester agent.
- led to: none

### T-20261103-1 · 2026-11-03 · python -m unittest · owner-pc Windows · 14/14
- mkw.py unit tests (assets headers, timeline arithmetic, wishlist ratios cite sources, lint, ethics scan, communities). The eval suite has not been run yet.
- led to: none
