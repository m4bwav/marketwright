# Tests: marketwright

Test runs for [SKILL.md](SKILL.md). Cases live in `evals/evals.json`; unit tests for `mkw.py` in the repository's `tests/`. A test passes on evidence (a tool call in the trace, a file, a marker), never on the transcript's claim. Entry shape: `### T-YYYYMMDD-n · date · harness · env · passed/total`, failing cases one per line, then `led to:`. Newest first.

## Runs

### T-20261103-1 · 2026-11-03 · python -m unittest · owner-pc Windows · 14/14
- mkw.py unit tests (assets headers, timeline arithmetic, wishlist ratios cite sources, lint, ethics scan, communities). The eval suite has not been run yet.
- led to: none
