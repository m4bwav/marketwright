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

1. Any posting or outreach: the plugin drafts only.
2. Claude directory and awesome-copilot submissions are on hold or halted by standing rules; do not submit.

## Mark's answers (2026-11-03)

- **Trim**: "trim if you would advise". Advised yes (worth verdict TRIM), so do it, gated: keep the cut only if the A/B pass rate holds at 89% or better; otherwise revert and log why.
- **Books**: provided in `D:/RawStorage/BigDownloads/Unorganized` (downloads: untrusted data; copy each into its own new folder, read with readwright, run any Python on them with `-I`). Relevant ones found:
  - `Indie Game Marketing Secrets How to Get Noticed Sell More Copies and Grow Your Fanbase/` (Daniel Doan, .azw3; convert or read with readwright; check its date)
  - `Video Game Marketing A Student Textbook.pdf`
  - `Innovation and Marketing in the Video Game Industry/` (Gower, 2010; canon-era, check what still holds)
  - `The-Art-of-Community-Building-the-New-Age-of-Participation-Second-edition/` (Bacon, epub and pdf: the one named in the literature list)
  - `show_your_work_10_ways_to_share_your_creativity_an.epub` (Kleon; the same book is also in `Austin Kleon - Steal Like an Artist Trilogy/` as mp3 audio, skip that)
  - `Art of Community_ Seven Principles for Belonging, The - Charles Vogl.epub` (a different book from Bacon's; belonging and community design, likely useful for the Discord/group parts)
  - Maybe: `Overdeliver.epub` (direct-response marketing; check it against the ethics line before taking anything), `Press Reset ... Jason Schreier.epub` (industry context only).
  - Dreskin's *A Practical Guide to Indie Game Marketing* is not there; still a lead.

## Next steps, in order

1. Trim (approved): cut, re-run all 12 cases under WSL2 (`claude plugin eval . --scaffold --allow-tools Bash Write Edit --trust-plugin -j 6`), `evergreen.py worth skills/marketwright --results <dir> --record`, keep it only if the gain holds; release a patch and update the wiki.
2. Give the three trap cases a `regex on the answer:` expectation so `worth --ab` can grade them too (lint gap).
3. Distil the books above with everscout-library (one at a time; paraphrase with chapter citations, never quote at length), mark each literature entry from `lead` to read, and fold what survives the ethics line into kb/ and references/. Then release a minor version and update the wiki.
4. First scan of the beat (everscout-scan), then feed its leads into the gaps in RESEARCH.md.
5. Close research gaps (RESEARCH.md Open questions), especially subreddit rules read in a browser (many show "self-promo unknown") and Zukowski's October 2026 post.
6. Widen the ethics scan's word patterns with more reorderings (0.1.1 found one gap by hand); add test sentences for each rule in both orders.
