# HANDOFF: marketwright

Updated 2026-11-03. Continue prompt: [plans/2026-11-02-marketwright-continue-prompt.md](plans/2026-11-02-marketwright-continue-prompt.md).

## State

- Plugin 0.1.0 built locally at `Ai/marketwright` (git on `main`, local only: no GitHub remote yet). Tests 15/15, budget green, manifest valid. Not installed, not released.
- Everscout beat `indie-game-marketing` built, probed and committed in the indie-ai-scout repo. No scan yet.
- Literature: 3 canon, 1 recent, 1 latest, all `lead`. No book provided yet.
- Evergreen unit `skills/marketwright` (fast tier, next due 2026-11-24), registered, linked to the beat. Evals: 12 of 12 cases pass with the skill (actions run under WSL2 with a fixture scaffold, T-20261103-3). evergreen-worth verdict TRIM recorded: pass 89% with vs 0% without, cost x1.82.

## Waiting on Mark

1. **Name and shape**: keep `marketwright` as its own plugin (decision file `decisions/2026-11-03-one-skill-and-name.md`)? Alternatives there.
2. **Books to buy or provide**: Dreskin, *A Practical Guide to Indie Game Marketing* (2015) is the only book-length indie marketing guide found; Bacon, *The Art of Community* (2012, free under CC); Kleon, *Show Your Work!* (2014). Zukowski has no book: his blog and GDC 2025 talk are the current source. Provide a file and the next session distils it with everscout-library.
3. **Making the repository public** (and the README banner then, per the banner rule) and any release.
4. Any posting or outreach: the plugin drafts only.
5. **Trim (evergreen-worth TRIM)**: cut SKILL.md's general sentences (64% name nothing specific; the probe showed bare Claude already says "gameplay-first trailer"), move procedure detail into `references/`, then re-run the A/B and keep the trim only if the 89% holds. Yes or no?

## Next steps, in order

1. If Mark says yes to the trim: cut, re-run all 12 cases under WSL2 (`claude plugin eval . --scaffold --allow-tools Bash Write Edit --trust-plugin -j 6`), `evergreen.py worth skills/marketwright --results <dir> --record`, keep it only if the gain holds.
2. Give the three trap cases a `regex on the answer:` expectation so `worth --ab` can grade them too (lint gap).
3. First scan of the beat (everscout-scan), then feed its leads into the gaps in RESEARCH.md.
4. Close research gaps (RESEARCH.md Open questions), especially subreddit rules read in a browser and Zukowski's October 2026 post.
5. After Mark's yes on the name: create the GitHub repo (private until he says public), banner, wiki, release 0.1.0.
