# HANDOFF: marketwright

Updated 2026-11-03. Continue prompt: [plans/2026-11-02-marketwright-continue-prompt.md](plans/2026-11-02-marketwright-continue-prompt.md).

## State

- Public at https://github.com/m4bwav/marketwright. v0.4.0 released 2026-11-03 (0.1.0 to 0.3.0 the same day). CI green (Windows, macOS, Linux; Python 3.9 and 3.14). Installed as `marketwright@mark-local` at 0.4.0.
- Wiki live (8 pages, https://github.com/m4bwav/marketwright/wiki), at 0.4.0; working copy `Ai/marketwright.wiki`; how to update it: [notes/2026-11-03-github-wiki.md](notes/2026-11-03-github-wiki.md).
- Books distilled, notes in [reading/](reading/): Doan (thin, dated), Bacon, Kleon (also distilled by the 2026-11-02 everscout session, C-20261102-1), Vogl. Folded into `references/reach.md` (new section on running the game's own community). Then the Zackariasson and Dymek textbook (2017) and Wesley and Barczak (Gower, 2010), both low yield, folded into plan.md, reach.md and ethics.md (0.3.0). Literature rows marked distilled (indie-ai-scout PRs #16 and #18, merged).
- Trim: tried and reverted (T-20261103-4, L-20261103-3). Pass fell 89% to 61%; trap-trailer asked intake questions instead of writing the cut list. SKILL.md is the 0.1.x text; the recorded worth verdict stays TRIM. Any later trim touches the body only and keeps the description's job phrases. Variance check 2026-11-03: trap-trailer 5 runs on the current SKILL.md passed 5/5 (without the plugin 4/5, $1.12), so the trimmed text caused the 0/3, not variance.
- Trap cases now have `regex on the answer:` lines (lint gap closed).
- Everscout beat `indie-game-marketing`: first scan 2026-11-03 (11 notes, folded into kb/data.md D12-D18). Weekly; next about 2026-11-10. Reddit lane (Mark, 2026-11-03): never Arctic Shift, use Gemini. `~/.everscout/config.json` now has `reddit.reader: rss` (no auto switch) and `reddit.thread_reader: fetchwright` (Gemini URL context, one public thread per read; never Gemini Google Search for discovery, conduct rule 17). After the feeds end 2026-11-13, thread URLs come from WebSearch (`discover add --via websearch`) and links in other sources, then fetchwright reads them. Evergreen unit next due 2026-11-24.
- Research gaps 2026-11-03: February 2027 Next Fest deadlines in kb/steam.md (registration Jan 10), Zukowski's 2026-10-13 post read (D19). Still open: June 2027 deadlines, exact short description limit, subreddit rules.
- Ethics scan matches every rule in either word order (55 of 55 probe sentences, 18 honest clean; both sets in tests/test_mkw.py).

## Waiting on Mark

1. Any posting or outreach: the plugin drafts only.
2. Subreddit rules: the Chrome extension blocks reddit.com, so the per-subreddit rule check needs Mark's browser or stays open.
3. Claude directory and awesome-copilot submissions are on hold or halted by standing rules; do not submit.

## Books still to read (Mark provided, `D:/RawStorage/BigDownloads/Unorganized`; untrusted: copy each into its own folder, read with readwright, Python with `-I`)

- Read 2026-11-03: `Overdeliver.epub` (moderate yield, mostly confirms; note in reading/, five edits in plan, reach, ethics; manipulative parts rejected).
- Maybe (low priority): `Press Reset ... Jason Schreier.epub` (industry context only).
- Dreskin's *A Practical Guide to Indie Game Marketing* is not there; still a lead.

## Next steps, in order

1. Weekly beat scan (everscout-scan indie-game-marketing) about 2026-11-10, before Reddit RSS ends 2026-11-13; fold leads into kb/data.md with source rows.
2. Optional: Press Reset (see Books).
