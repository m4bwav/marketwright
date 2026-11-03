# Procedure: a marketing and launch plan

Output: `marketing-plan-<slug>.md` beside the user's request. Read [../kb/steam.md](../kb/steam.md) and [../kb/data.md](../kb/data.md) first; [../kb/ethics.md](../kb/ethics.md) when a tactic is in doubt.

1. **The game in four lines.** Genre and the one-line hook a player of that genre would click for; platform and price; stage (prototype, demo, Coming Soon page, released); release window. If the hook is vague, say so and stop at a hook exercise (or hand to ludowright); no tactic rescues a game nobody can describe.
2. **Who and where.** The players of the closest three games on the platform. `MKW communities --genre <genre> --general` lists where they gather and each place's rule. Pick at most five places to be a member of.
3. **Where the game stands.** Wishlists now, if any. `MKW wishlists --count <n>` for honest ranges at launch; say plainly when the count is too low for the launch the user hopes for and what moves it (a public page early, a demo, Next Fest, themed fests).
4. **The timeline.** `MKW timeline --release <date>` (add `--nextfest <start>` for a newer fest). Then add the beats it cannot know, each with an owner and a date:
   - Store page public as early as the page is good (months, not the two-week minimum), capsule from brandwright.
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
- **The date follows the build**: never fix a release date to beat a rival or hit a season if the build will not be ready; a broken launch week costs reviews a patch does not win back (Wesley and Barczak, Conclusion and ch. 6).
- **Past launch week**: plan the long tail (updates, sales, bundles) and a short post-mortem with the real numbers after launch (textbook ch. 6; Wesley and Barczak ch. 10).
