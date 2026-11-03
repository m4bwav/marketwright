# marketwright

![An indie developer at a desk at dusk: a monitor showing a pixel-art game with a lighthouse, a launch calendar pinned to a corkboard with sticky notes, a paper megaphone, a mug and a sketch notebook](https://raw.githubusercontent.com/m4bwav/marketwright/main/.github/images/banner.jpg)

Honest marketing for indie games. It helps a small developer get a game seen, wishlisted and bought by the people who would love it, using methods they could explain in public.

- **Launch plan**: audience and hook, where the genre's players gather, a dated timeline from the store page to launch (Next Fest, demo, playtest, themed fests, discounts), sized to the hours you have.
- **Steam store page review**: capsule sizes and capsule text rules, tags, short description, screenshots, the trailer slot, the AI disclosure, each finding tied to Valve's rule.
- **Trailer plan**: the hook in the first seconds, gameplay first, a cut list from your clips for cinewright or ffmpeg, GIFs and vertical cuts.
- **Reach**: communities by genre with their self-promotion rules, press kit contents, creator and press lists and emails, devlogs and a post calendar. It drafts; you post.
- **Roblox**: discovery works differently, and the plan says how.

## The ethics line

No fake or swapped reviews, no rewards for reviews, no sock puppets, no bought wishlists, followers or votes, no misleading trailers, no fake scarcity, no dark patterns, no undisclosed paid coverage, no hidden AI use. Every plan it writes goes through `mkw.py ethics` and one question: would this embarrass you if the community saw how it was done? Ask for a slimy tactic and you get a plain no and the honest route to the same goal.

## Numbers

Every number carries its source and date (Valve's Steamworks docs, Chris Zukowski's How To Market A Game data, GameDiscoverCo). They are medians of other games, never a forecast.

## The CLI

`skills/marketwright/scripts/mkw.py`, Python 3.9+, standard library only:

| Command | Does |
|---|---|
| `assets <folder>` | matches PNG and JPEG files to Steam's asset sizes and lists what is missing |
| `timeline --release YYYY-MM-DD` | milestones back from a release date: page review, Next Fest deadlines, sale clashes |
| `wishlists --count N` | first-week and first-month sales ranges from published ratios, with sources |
| `lint <page.json>` | Steam page lint against Valve's written rules |
| `ethics <plan.md>` | flags tactics a community would call slimy, with the honest version |
| `communities --genre G` | communities for a genre, their self-promotion rule and check date |

## Install

```
claude plugin marketplace add m4bwav/marketwright
claude plugin install marketwright@marketwright
```

Other agents: copy `skills/marketwright/` into your agent's skills folder.

## Works with

ludowright (the game's design and hook), brandwright (capsule and key art), pixelwright and artwright (pixel art), cinewright (cutting the trailer), musicwright (trailer music), sitewright (a game site or press page), askwright (decision pages), roblox-agent.

## Licence

MIT. Not legal advice.
