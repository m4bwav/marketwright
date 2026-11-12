# Changelog: marketwright

Every change to [SKILL.md](SKILL.md) and its companions, newest first, each with the reason (`R-`, `L-`, `T-` ids or "user request"). Entry shape: `### C-YYYYMMDD-n · date · summary`, then `because:`, `files:`, one sentence.

### C-20261112-1 · 2026-11-12 · In-engine capture before the cut (0.4.4)
- because: user request (technique harvest 2026-11-12, C-20261112-E)
- files: SKILL.md (Call, do not copy)
- Clips are captured in engine (Unity Recorder or a scripted camera) to a clips folder, then cut with cinewright-edit; posting stays the owner's.

### C-20261106-1 · 2026-11-06 · Sfxwright, when installed (0.4.3)
- because: user request
- files: references/trailer.md (sfxwright note)
- Hand sound effects to sfxwright when present and read its sounds.json; this plugin's own steps stay as the fallback.

### C-20261103-9 · 2026-11-03 · Overdeliver: plan across the catalogue (0.4.2)
- because: user request (book changes pre-approved); everscout beat indie-game-marketing, books/overdeliver (Kurtz 2019), the one change earlier Overdeliver reads (#15, #16) had not made
- files: references/plan.md
- Plan: the players a launch earns are the next game's first audience; judge channels across the catalogue.

### C-20261103-8 · 2026-11-03 · Futter, The GameDev Business Handbook (0.4.1)
- because: user request (book changes pre-approved); learnings in the everscout beat indie-game-marketing, books/the-gamedev-business-handbook-michael (Futter 2017)
- files: references/plan.md, references/store.md, references/reach.md, kb/ethics.md, SKILL.md (metadata.version was stale at 0.2.0)
- Plan: shows, break-even, date slips, Early Access, ports, crowdfunding, publishers; store: other stores' copy and ratings; reach: two press waves, follow-ups, embargo, gaffes, who joins; ethics: unconfirmed features. 2017 figures marked dated.

### C-20261103-7 · 2026-11-03 · first beat scan into data, plan, reach, store (0.4.0)
- because: everscout beat indie-game-marketing, first scan (11 notes in ~/.everscout/data/indie-game-marketing/notes)
- files: kb/data.md (D12-D18), references/plan.md, references/reach.md, references/store.md
- October 2026 Next Fest benchmarks and AI disclosure share; paid ads and paid showcase anecdotes; Roblox Sponsored Ads retention report; Steamworks onboarding up to 30 business days; capsule judged at real size and traffic read by surface.

### C-20261103-6 · 2026-11-03 · ethics scan matches both word orders (0.4.0)
- because: HANDOFF next step 3; a probe of 55 reordered sentences flagged only 17
- files: scripts/mkw.py, tests/test_mkw.py
- Each rule now built with near() (either order, one sentence); unit tests carry a flagged set per rule and 18 honest sentences that must stay clean.

### C-20261103-5 · 2026-11-03 · two more books (0.3.0)
- because: user request (books provided 2026-11-03); notes in ai-docs/reading (Video Game Marketing textbook, Wesley and Barczak 2010)
- files: references/plan.md, references/reach.md, kb/ethics.md
- Plan: hook leads with what the player does, paid/earned/owned, date follows the build, long tail and post-mortem; reach: key planning, devlog audience is not the market, answering negative reviews; ethics: honest hype, no invented shortages. Both books low yield.

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
