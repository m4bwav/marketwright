# Procedure: a marketing and launch plan

Output: `marketing-plan-<slug>.md` beside the user's request. Read [../kb/steam.md](../kb/steam.md) and [../kb/data.md](../kb/data.md) first; [../kb/ethics.md](../kb/ethics.md) when a tactic is in doubt.

1. **The game in four lines.** Genre and the one-line hook a player of that genre would click for; platform and price; stage (prototype, demo, Coming Soon page, released); release window. If the hook is vague, say so and stop at a hook exercise (or hand to ludowright); no tactic rescues a game nobody can describe.
2. **Who and where.** The players of the closest three games on the platform. `MKW communities --genre <genre> --general` lists where they gather and each place's rule. Pick at most five places to be a member of.
3. **Where the game stands.** Wishlists now, if any. `MKW wishlists --count <n>` for honest ranges at launch; say plainly when the count is too low for the launch the user hopes for and what moves it (a public page early, a demo, Next Fest, themed fests).
4. **The timeline.** `MKW timeline --release <date>` (add `--nextfest <start>` for a newer fest). Then add the beats it cannot know, each with an owner and a date:
   - Store page public as early as the page is good (months, not the two-week minimum), capsule from brandwright. Start Steamworks onboarding six weeks before that: verification took up to 30 business days in late 2026 (kb/data.md).
   - Announcement trailer and first posts; devlog cadence the user can keep (weekly beats monthly beats abandoned).
   - Playtest (Steam Playtest is free and collects signups) and the demo; Next Fest needs the demo reviewed 5 weeks ahead for the press preview.
   - Themed fests that fit the genre (dates in kb/steam.md), press and creator outreach waves (references/reach.md), launch discount decision.
   - Steam: for Roblox, replace this list with the Roblox steps below.
5. **Roblox.** Discovery ranks first-session bounce, play-through, play days and playtime per user (kb/data.md). The plan's first weeks go to the first five minutes, measured; ads only after the bounce rate is good, because ad-acquired players do not count for ranking. Small, frequent updates; a group and a Discord for regulars. Hand engine work to roblox-agent.
6. **Budget and time.** What the user can spend per week. Cut the plan to fit; a short plan done beats a long one dropped.
7. **Ethics check.** Save the file, run `MKW ethics <file>`, fix flags, then the embarrassment question on each step. Add a line at the end: `Ethics check: <n> flags fixed, passed <date>`.

## The plan file

Sections: The game in four lines · Audience and places · Where it stands (numbers with sources) · Timeline (table: date, step, owner, done) · Assets needed (each with the plugin that makes it) · What we will not do (the ethics line in two lines) · Open questions · Sources.

While writing it:
- **The four lines lead with what the player gets to do**, not the engine or features; test that hook on players who do not know the developer (playtest, demo) before pushing the page (Wesley and Barczak, Introduction and Conclusion).
- **Paid, earned, owned** under Audience and places: what the user owns (Steam page, mailing list, Discord, devlog, earlier games), how attention will be earned (creators, press, festivals, communities), and any paid budget, stated as a number or "none" (Video Game Marketing textbook, ch. 5).
- **Grow the owned, opted-in list first** (mailing list, Discord, playtest sign-ups): a small list of people who play similar games beats broad targeting of strangers. Before writing the hook, ask the developer what is new, what was hard and what other games lack; the hook comes from those answers (Overdeliver chs. 4, 6).
- **Plan for the next game too**: the players this launch earns are the first audience for the next game, its DLC and the back catalogue, so judge a channel by what it brings across the catalogue, not only launch week; on a second game, ask how many launch buyers had followed or bought the first (Overdeliver ch. 9).
- **The date follows the build**: never fix a release date to beat a rival or hit a season if the build will not be ready; a broken launch week costs reviews a patch does not win back (Wesley and Barczak, Conclusion and ch. 6).
- **Past launch week**: plan the long tail (updates, sales, bundles) and a short post-mortem with the real numbers after launch (textbook ch. 6; Wesley and Barczak ch. 10).
- **Shows and fests in person**: before booking, write the one goal (show, research, network, pitch), the full cost (booth, travel, lodging, the build days lost) and the cheaper event that might do the same. Every show gets its own demo-build line in the timeline two to three weeks before (Futter 2017, p. 38-39, 105).
- **Break-even line** under Budget: spend divided by what the developer nets per copy, after the store cut and any publisher recoup, gives the copies needed. Use today's store terms, not the book's 2017 figures (Futter 2017, p. 41, 120-122).
- **An unsure date stays private**: if the team doubts it can hit a date, list that as a risk and announce a window instead (Hill-Whittall 2015, ch. 2; book rule, unverified).
- **A date that moves** is announced once, with the reason and the new date; repeated slips cost trust (Futter 2017, p. 47-48).
- **Early Access** only for a replayable, content-led game the team can finish, with a named owner answering the forum from day one. Put the 1.0 scope on the page, announce price changes ahead, and give 1.0 news of its own (held-back features or a platform launch), since leaving Early Access is not news by itself (Futter 2017, p. 189-202).
- **A late port** gets news of its own: ship it with a content update and a sale across versions (Futter 2017, p. 129-130).
- **Crowdfunding** is a campaign of months: show gameplay, not concept art; set the goal at the real budget plus contingency; write a candid risks section; post updates even with no news (Futter 2017, p. 172-186).
- **If a publisher is possible**, talk before the name, price and announcement are fixed, and get their marketing commitments itemised in the contract (Futter 2017, p. 112-119).
