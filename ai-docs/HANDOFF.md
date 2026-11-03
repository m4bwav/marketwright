# HANDOFF: marketwright

Updated 2026-11-03. Continue prompt: [plans/2026-11-02-marketwright-continue-prompt.md](plans/2026-11-02-marketwright-continue-prompt.md).

## State

- Public at https://github.com/m4bwav/marketwright. v0.1.1 released 2026-11-03 (v0.1.0 the same day). README banner and social preview set; Discussions on. CI green on GitHub (Windows, macOS, Linux; Python 3.9 and 3.14).
- Wiki live (8 pages, https://github.com/m4bwav/marketwright/wiki); working copy `Ai/marketwright.wiki`; how to update it: [notes/2026-11-03-github-wiki.md](notes/2026-11-03-github-wiki.md).
- Installed as `marketwright@mark-local` at 0.1.1.
- Everscout beat `indie-game-marketing` built, no scan yet. Literature: 3 canon, 1 recent, 1 latest, all `lead`.
- Evergreen unit `skills/marketwright` (fast tier, next due 2026-11-24). Evals 12/12 with the skill; worth verdict TRIM (89% vs 0%, cost x1.82).
- Name and own plugin: settled by Mark making it public (2026-11-03).

## Waiting on Mark

1. **Trim (evergreen-worth TRIM)**: cut SKILL.md's general sentences, move procedure detail into `references/`, re-run the A/B and keep the trim only if the 89% holds. Yes or no?
2. **Books to buy or provide**: Dreskin, *A Practical Guide to Indie Game Marketing* (2015); Bacon, *The Art of Community* (2012, free under CC); Kleon, *Show Your Work!* (2014). Provide a file and the next session distils it with everscout-library.
3. Any posting or outreach: the plugin drafts only.
4. Claude directory and awesome-copilot submissions are on hold or halted by standing rules; do not submit.

## Next steps, in order

1. If Mark says yes to the trim: cut, re-run all 12 cases under WSL2 (`claude plugin eval . --scaffold --allow-tools Bash Write Edit --trust-plugin -j 6`), `evergreen.py worth skills/marketwright --results <dir> --record`, keep it only if the gain holds; release a patch and update the wiki.
2. Give the three trap cases a `regex on the answer:` expectation so `worth --ab` can grade them too (lint gap).
3. First scan of the beat (everscout-scan), then feed its leads into the gaps in RESEARCH.md.
4. Close research gaps (RESEARCH.md Open questions), especially subreddit rules read in a browser (many show "self-promo unknown") and Zukowski's October 2026 post.
5. Widen the ethics scan's word patterns with more reorderings (0.1.1 found one gap by hand); add test sentences for each rule in both orders.
