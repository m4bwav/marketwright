# Research: marketwright

Findings that back [SKILL.md](SKILL.md). Full notes with every URL: the repository's `ai-docs/research/` (2026-11-02 survey and its four parts). Protocol: MAINTENANCE.md.

Topic: honest indie game marketing: Steam store pages, wishlists and festivals, trailers, press and creator outreach, communities and their self-promotion rules, Roblox discovery, and the platform rules and law on reviews, endorsements and AI disclosure. Tier `fast`. Last refresh 2026-11-03; next due 2026-11-24.

## Current understanding

- R-20261103-1 (subject, Valve): asset sizes changed August 2024; capsule text rules since 2022; Next Fest one per game with 5- and 3-week demo deadlines; 30-day discount cooldown; AI disclosure narrowed to content players consume (January 2026 per press; Valve's page has no date). Magnitude: baseline.
- R-20261103-2 (practice, data): wishlists are worth about half what they were (0.45 to 0.22 first-month sales per wishlist, 2020-22 against 2023-25); Popular Upcoming bar rose to about 100,000 in June 2026; Next Fest medians by size. Baseline.
- R-20261103-3 (subject, ethics and law): Steam review and key rules; FTC 16 CFR 465 (in force 2024-10-21); UK DMCC fake review ban (2025-04-06); ASA/CAP influencer guidance updated October 2026; sourced backlash cases. Baseline.
- R-20261103-4 (tooling): no existing skill, plugin or MCP server covers honest indie marketing with community rules; closest are coreyhaines31/marketingskills (general), a game-marketer skill (claudskills.com), steam-publisher, and Steam and Reddit MCP servers (Reddit ones need API access). Confidence: medium (aggregator pages).
- R-20261103-5 (practice, communities): 31 subreddits probed alive or dead by RSS on 2026-11-03 (r/deckbuildinggames and r/platformers dead); rules pages not readable by fetch. Stored in kb/communities.json.
- R-20261113-1 (practice, book): Hill-Whittall, Indie Game Developer Handbook (2015), chs. 2-4: re-contact reviewers after a fix, no licensed trailer music, an unsure date is a risk, short About bullets and press headlines near 70 characters. Book rules, unverified; 2015 store details dated.
- Linked everscout beat `indie-game-marketing` (created 2026-11-03): its notes are leads only.

## Open questions

- Exact short description limit (Steamworks still says only "a few hundred characters", 2026-11-03); June 2027 Next Fest deadlines (February 2027 recorded in kb/steam.md); how the AI disclosure renders; Discovery Queue and Upcoming mechanics.
- Gamalytic and VG Insights; Valve Dev Days talks; GDC 2026 Vault.
- Woovit status; Lurkit and Keymailer prices from their own pages; TikTok, Bluesky, Discord and X manipulation and paid-label rules; fake scarcity rulings.
- Every subreddit rule read in a browser (the Chrome extension blocks reddit.com; needs Mark or another route).

## Search plan

- Subject: `site:partner.steamgames.com/doc` store assets, Next Fest, discounts, content survey; Steamworks group news; FTC, CMA, ASA news on reviews and influencers.
- Practice: howtomarketagame.com newest posts; GameDiscoverCo newsletter; "Next Fest" postmortem <month year>; the beat's notes.
- Tooling: `path:SKILL.md "steam" marketing` on GitHub; registry.modelcontextprotocol.io search steam, reddit.
- Testing: how store page reviews and launch plans are judged (Zukowski's page critiques, GDC "Critique My Page").
