# Log: marketwright

Newest last.

## [2026-11-02] research | four passes
Steam rules, wishlist data and practice, ethics and law, tools and communities, run in parallel. Files in `research/`, index in `research/2026-11-02-indie-marketing-survey.md`. Reddit could not be fetched by the research pass (L-20261103-1).

## [2026-11-03] beat | indie-game-marketing
Private everscout beat in `Ai/indie-ai-scout/beats/indie-game-marketing` (commit ab38918, pushed): 41 sources (18 scanned, 23 genre rows kept for the community map), 55 entities in 4 facets, 21 questions, 10 searches, 3 metrics, literature with 3 canon, 1 recent, 1 latest. Probe: all ok except the GDC YouTube feed (404 on every form; kept with scan no). r/deckbuildinggames and r/platformers are dead. Data folder `~/.everscout/data/indie-game-marketing`.

## [2026-11-03] build | 0.1.0
One skill (decision `decisions/2026-11-03-one-skill-and-name.md`), four procedures, three kb files plus communities.json, mkw.py with six commands, 15 unit tests passing, budget green, `claude plugin validate .` passes. Bug caught while trying the CLI: the timeline put the store page deadline after Next Fest, which needs a public page; fixed and tested. Eval suite written (12 cases with the saltlight fixture). No GitHub remote yet: Actions on a private repo would cost Mark money, and making it public waits on him.

## [2026-11-03] evals | T-20261103-2
`evergreen.py eval-export --out evals` writes case folders to the root `evals/` (the harness refuses an eval dir inside `skills/`), and only the last `--case` flag counts. 9 cases run: triggers 3/3 (bare 0/3), decoys 3/3, traps 3/3 with the skill; without it, the trailer trap failed every run and the review swap one in three. The three action cases cannot run on native Windows (Bash grant refused without a sandbox); graders written by hand, to run under WSL2. Unit registered with evergreen.

## [2026-11-03] evals | T-20261103-3 and worth
Action cases run under WSL2 (`claude plugin eval . --case "action-*" --scaffold --allow-tools Bash Write Edit --trust-plugin -j 6`). The sandbox hides the plugin's `evals/` folders, so the saltlight fixture is now seeded by a per-case scaffold (L-20261103-2). Results: roblox +1.00, steam +0.92, store +0.67. Probe without the skill missed every Valve store rule. evergreen-worth verdict TRIM (89% vs 0%, cost x1.82), recorded; the trim waits on Mark.

## [2026-11-03] release | public repo, 0.1.0 and 0.1.1, wiki
Mark: "this will be a public repo with wiki and social image". That settles the name and the own-plugin question. Created public m4bwav/marketwright (Discussions, wiki, topics), PR #1 banner (Z-Image Turbo seed 44 of 4, PC host) and social preview (centre 1280x640 crop, uploaded in Settings via the browser), v0.1.0 released with a zip. Writing the wiki found an ethics scan gap ("review in exchange for a free key" scanned clean); PR #2 fixed it with a test, v0.1.1 released. Installed as marketwright@mark-local (added to the Ai marketplace.json), updated to 0.1.1. Wiki: 8 pages, note in notes/2026-11-03-github-wiki.md. CI on GitHub (public repo, free minutes): 6 jobs green on both PRs.

## [2026-11-03] trim, books, 0.2.0
Trim tried (shorter description, no per-use evergreen.json read, merged closing sections) and reverted: full 12-case A/B under WSL2 gave 61% with (gate 89%); trap-trailer 0/3, it asked for intake instead of writing the cut list (T-20261103-4, L-20261103-3, $10.56). Trap cases got `regex on the answer:` lines. Read Doan (myself), Bacon, Kleon and Vogl (reader agents); notes in ai-docs/reading. A parallel session had merged a Kleon devlog step (PR #3) meanwhile; rebased and kept theirs. New community section in references/reach.md. PRs #4, #5 merged, v0.2.0 released, wiki at 0.2.0, plugin updated. indie-ai-scout PR #16 (literature rows) merged from a worktree, since the shared clone was behind.

## [2026-11-03] books | textbook and Wesley and Barczak, 0.3.0
Checked no other session had these books (round-3 game-design readers cover design books only). Two reader agents wrote notes in ai-docs/reading; both low yield (textbook has no Steam content and a "high expectations always help" claim rejected; Gower is a console-era case book). Folded into plan.md (player-first hook, paid/earned/owned, date follows the build, long tail and post-mortem), reach.md (key planning, devlog audience is not the market, answering negative reviews), ethics.md (honest hype, no invented shortages). PR #7 merged, v0.3.0 released, plugin updated, wiki at 0.3.0, indie-ai-scout PR #18 (literature rows) merged from a worktree.

## [2026-11-03] scan and ethics | first beat scan, ethics both orders, 0.4.0
First everscout scan of indie-game-marketing: 41 sources, 691 items, 11 notes (6 Reddit, 5 web), all searches.md rows. Reddit read through RSS (config reddit.reader auto, which switches to Arctic Shift on 2026-11-13; this beat must not use it, so that waits on Mark). Leads into kb/data.md D12-D18 (Oct 2026 Next Fest followers halved, 34% AI disclosure, Reddit ads $2.12 per wishlist, 150k-wishlist launch with 19.8% refunds, paid showcase complaints, Roblox Sponsored Ads retention, Steamworks onboarding up to 30 business days), plan, reach and store. Ethics scan: probe of 55 reordered sentences caught 17; rebuilt each rule with near() (either order), 55 of 55 now and 18 honest sentences clean, both sets in the unit tests. PR #9 merged, v0.4.0 released, plugin updated, wiki at 0.4.0; indie-ai-scout PR #19 (vocab paid-promotion) merged.

## [2026-11-03] research | 2027 Next Fest deadlines, Zukowski post
February 2027 fest dates from Steamworks into kb/steam.md (registration Jan 10, Press Preview review Jan 18, all items Feb 1). Read Zukowski's 2026-10-13 wishlist post directly (D19, pooled R squared, velocity adds little). Short description limit still unpublished. Subreddit rules stay open: reddit.com blocked in the browser extension.

## [2026-11-03] evals | trap-trailer variance check
`claude plugin eval . --case trap-trailer --runs 5 -j 5 --trust-plugin` on the 0.4.0 SKILL.md: 5/5 with the plugin, 4/5 without, $1.12, 48 s (native Windows works for trap cases). The 0/3 under the trim (L-20261103-3) was the trimmed text, not variance. Weekly beat scan not due until about 2026-11-10.
