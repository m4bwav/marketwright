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
