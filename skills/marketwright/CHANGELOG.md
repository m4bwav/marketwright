# Changelog: marketwright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason (`R-`, `L-`, `T-` ids or "user request"). Entry shape: `### C-YYYYMMDD-n · date · summary`, then `because:`, `files:`, one sentence.

### C-20261103-4 · 2026-11-03 · books into the reach procedure (0.2.0)
- because: user request (books provided 2026-11-03); notes in ai-docs/reading (Doan, Bacon, Kleon, Vogl)
- files: references/reach.md
- New section on running the game's own community (set it up before linking, rituals, earned roles, health, conflict and burnout), plus outreach and devlog lines, each with a chapter citation.

### C-20261103-3 · 2026-11-03 · trim tried and reverted; trap cases get answer regexes
- because: T-20261103-4
- files: evals/evals.json (SKILL.md unchanged)
- The trim (shorter description, no per-use evergreen.json read, merged closing sections) cut pass from 89% to 61%, so it was reverted. Trap cases now carry `regex on the answer:` lines so `worth --ab` can grade them.

### C-20261102-1 · 2026-11-02 · devlogs: what to post per stage, stock and flow, mailing list (unreleased)
- because: Kleon, Show Your Work! (2014), distilled by everscout-library into the indie-game-marketing beat
- files: references/reach.md
- The devlog step now says what to post at each stage, to capture material while building, to time-box posting, to gather posts onto an owned page and to keep an opt-in mailing list.

### C-20261103-2 · 2026-11-03 · ethics scan: reward named after the review (0.1.1)
- because: found while writing the wiki: "leave a review in exchange for a free key" scanned clean
- files: scripts/mkw.py, tests
- The "reward for a review" rule now also matches the reward named after the word review.

### C-20261103-1 · 2026-11-03 · created (0.1.0)
- because: user request (kickoff 2026-11-02), R-20261103-1 to R-20261103-5
- files: all
- One skill with four procedures (plan, store, trailer, reach), three kb files and kb/communities.json, mkw.py (assets, timeline, wishlists, lint, ethics, communities).
