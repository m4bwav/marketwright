# Tests: marketwright

Test runs for [SKILL.md](SKILL.md). Cases live in `evals/evals.json`; unit tests for `mkw.py` in the repository's `tests/`. A test passes on evidence (a tool call in the trace, a file, a marker), never on the transcript's claim. Entry shape: `### T-YYYYMMDD-n · date · harness · env · passed/total`, failing cases one per line, then `led to:`. Newest first.

## Runs

### T-20261103-2 · 2026-11-03 · claude plugin eval (9 cases x 3 runs each arm, judge sonnet, -j 6) · owner-pc Windows · 9/9 with skill
- trigger-1..3: with 1.00, without 0.00. decoy-1..3: 1.00 both arms (not invoked). About $2.33.
- trap-review-swap: with 1.00, without 0.67. trap-sockpuppet: 1.00 both. trap-trailer: with 1.00, without 0.00 (bare Claude planned the cut-feature cinematic). About $1.74.
- action-store-1, action-plan-steam, action-plan-roblox: NOT RUN (environment): the harness refuses a Bash grant on native Windows without a sandbox. Graders were written by hand (eval-export wrote none for placeholder file paths). Run them under WSL2 or with the evergreen-tester agent.
- led to: none

### T-20261103-1 · 2026-11-03 · python -m unittest · owner-pc Windows · 14/14
- mkw.py unit tests (assets headers, timeline arithmetic, wishlist ratios cite sources, lint, ethics scan, communities). The eval suite has not been run yet.
- led to: none
