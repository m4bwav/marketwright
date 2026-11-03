# AGENTS.md

Rules for any AI agent (Claude Code, Copilot, Cursor, Codex, Gemini CLI) working in this repository. `CLAUDE.md` imports this file and `.github/copilot-instructions.md` points here.

## What this is

marketwright: a cross-agent plugin with one skill, `skills/marketwright/`, for honest indie game marketing. SKILL.md holds the ethics line, the rules and the routing; `references/` holds the four task procedures (plan, store, trailer, reach); `kb/` holds Valve's rules (`steam.md`), sourced data and practice (`data.md`), the ethics rules and cases (`ethics.md`) and the community map (`communities.json`); `scripts/mkw.py` is the single standard-library CLI (assets, timeline, wishlists, lint, ethics, communities). Evergreen companions sit beside SKILL.md (RESEARCH, CHANGELOG, LEARNINGS, TESTS, MAINTENANCE, `evergreen.json`, `evals/evals.json` with the `saltlight` fixture). Unit tests in `tests/`; research, decisions, the log and the handoff under `ai-docs/` (start with `ai-docs/HANDOFF.md`).

## Rules

- **The ethics line is the product.** Never add a tactic that only works while hidden, and never weaken the refusals in SKILL.md or the patterns in `mkw.py ethics` without a decision entry in `ai-docs/decisions/`.
- **Every number has a source and a date.** A kb row or a `mkw.py` constant with no source is removed, not kept. UNVERIFIED marks what was not read on a primary page. Re-check rows older than 60 days before a release.
- `mkw.py` stays one standard-library Python file (3.9 or newer) for Windows, macOS and Linux, UTF-8 and LF. Every change gets a test in `tests/test_mkw.py`. Run `python -m unittest discover -s tests` before committing.
- The plugin drafts; the user posts. No code or instruction may log in, post, send email, buy ads or keys, or scrape a platform that forbids it. Reddit is read through public RSS only.
- Fixtures are invented games written for the suite. Never commit another person's store page, sales data or emails.
- Size budget: `python scripts/budget.py` (red fails CI). Keep SKILL.md under 200 lines.
- The skill is an evergreen unit. Before editing it read `skills/marketwright/evergreen.json`; if `next_due` has passed or `contradiction` is set, say so and refresh after the task. Every change is logged in the skill's `CHANGELOG.md` with its reason; lessons go to `LEARNINGS.md`. The linked everscout beat `indie-game-marketing` feeds refreshes as leads.
- A release bumps the version in `.claude-plugin/plugin.json`, `plugin.json`, `VERSION` in `mkw.py`, `metadata.version` in SKILL.md and the CHANGELOG together, then tags `vX.Y.Z` and publishes a GitHub Release.
- Neighbours (call, never copy): ludowright (design and hook), brandwright (capsule and key art), pixelwright and artwright (pixel art and judging), cinewright (trailer editing), musicwright-game (trailer music), sitewright (game site and press page), askwright (decision pages), roblox-agent (Roblox engine work).
- Public-ready: no person named other than the author credit, published authors and public figures in sourced cases; no machine, no absolute local path, no credential. Plain short sentences, no em dashes, relative markdown links.
- No AI attribution anywhere: no Co-Authored-By trailers, no "generated with" lines in commits, pull requests, releases or files.

## Commands

- Tests: `python -m unittest discover -s tests`
- Budget: `python scripts/budget.py`
- CLI: `python skills/marketwright/scripts/mkw.py --help`
- Plugin manifest: `claude plugin validate .`
- Evals: `claude plugin eval . --no-publish --trust-plugin --case "trigger-*"`

## everlast (session knowledge, load on demand)

- Read `ai-docs/HANDOFF.md` when continuing unfinished work; `ai-docs/log.md` has the history.
- Before finishing a task that hit a dead end, verified a non-obvious command or made a design choice, record it in `ai-docs/` and rewrite `HANDOFF.md` when work is left unfinished.
