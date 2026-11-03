# Existing tools and communities (2026-11-02)

Status: UNVERIFIED-LIVE. Reddit could not be reached. WebFetch refuses www.reddit.com, including the RSS rules feed. No Arctic Shift, no Gemini. All Reddit facts below come from web search results, mostly marketing blogs and archive snapshots.

## Part A: existing tools

Last-update dates and licences were not checked on GitHub this pass unless stated. Check before citing.

### Marketing skill collections
- coreyhaines31/marketingskills. https://github.com/coreyhaines31/marketingskills. 33 to 40+ general marketing skills (CRO, copy, SEO, PR, analytics). MIT. Very popular (tens of thousands of stars). Nothing game-specific. Install with `npx skills add`.
- game-marketer skill. https://claudskills.com/skills/game-marketer/SKILL.md. Store page conversion, trailers, CPI and ROAS, creator programs, wishlist campaigns. Mobile-leaning. Licence unknown. Closest overlap with our plugin.
- steam-publisher (gavinmcfall/agentic-config). https://skill-web-8ek.pages.dev/skill/steam-publisher. Steamworks setup to build upload, plus timelines, pricing, wishlists.
- publishing-platforms (pluginagentmarketplace/custom-plugin-game-developer). https://www.skills.sh/pluginagentmarketplace/custom-plugin-game-developer/publishing-platforms. Platform requirements reference.
- monetize-game (opusgamelabs/game-creator). https://claudemarketplaces.com/skills/opusgamelabs/game-creator/monetize-game. Monetization after deploy.
- inskillflow indie game dev bundle. https://www.vibeindex.ai/plugins/inskillflow/claude-code-skills/antigravity-bundle-indie-game-dev.

Gap: none of these focus on honest marketing, community rules per genre, or not getting banned on Reddit.

### Steam MCP servers
- steamdb-mcp (irfanmaulanaak). https://pypi.org/project/steamdb-mcp/. SteamDB-style data from the Steam Store API and SteamSpy. Not SteamDB itself; SteamDB has no public API.
- tmhsdigital/steam-mcp. TypeScript, 25 tools, store, price, reviews, tags. Read tools need no key.
- Grinv/steam-games-mcp. Keyless store, deals, tags, Steam Deck data. MIT.
- Sarg338/steam-mcp. Read-only store data.
- steam-blade-mcp. https://pypi.org/project/steam-blade-mcp/. Store, library, achievements, market.

### Reddit MCP servers
- hawstein/mcp-server-reddit. Read-only via redditwarp.
- hamzashahbaz/reddit-mcp. Read-only, needs Reddit API app. MIT.
- jordanburke/reddit-mcp-server. Read and post, needs API credentials.
- Arindam200/reddit-mcp. Details not seen.
Note: all need Reddit API access, which our rules avoid. Do not depend on them.

### Press kit generators
- presskit() by Rami Ismail. https://dopresskit.com/. XML plus PHP hosting. De facto structure.
- Wayline game press kit generator. https://www.wayline.io/game-press-kit. Single HTML file output.
- Press Kitty by IMPRESS. https://impress.games/. Fills from a Steam page, needs an account.

Registries skills.sh, smithery, glama, mcp.so and registry.modelcontextprotocol.io were not queried one by one. Results above came via aggregators.

## Part B: communities

Full list in `communities.json`. Only two Reddit subscriber counts were found: r/gamedev about 1.9M and r/IndieGaming about 500K (steampageanalyzer.com, rounded, July 2026).

Rules that search sources support:
- Reddit's sitewide 10:1 guideline is retired. The spirit lives on in sub rules and mod judgment.
- r/gamedev is not for promotion. Use Screenshot Saturday and Feedback Friday threads.
- r/indiegames allows promotion but bans promo dressed as a feedback request (2024).
- r/IndieGaming allows promotion with frequency caps.
- r/Games allows dev promo only in monthly Indie Sunday.
- r/gamedevscreens tolerates WIP promo.
- Guides name genre subs: r/roguelikes, r/metroidvania, r/CozyGamers, r/citybuilders, r/basebuildinggames, r/incremental_games. No deckbuilder sub was found in sources.

Other genre subs in the JSON are educated guesses marked unverified.

Non-Reddit: #screenshotsaturday, #indiedev, #gamedev on Bluesky and Mastodon. mastodon.gamedev.place is the main dev instance. itch.io forums, TIGSource DevLogs, Steam Curator Connect. Discord servers not researched.

## Next steps
- Reach Reddit RSS from a host that allows it, one request per 30 to 60 s, and upgrade confidence.
- Check licences and last commits of the Part A repos with `gh`.

## Sources
- https://www.steampageanalyzer.com/blog/reddit-indie-game-marketing
- https://bugnet.io/blog/reddit-marketing-for-indie-games-without-getting-banned
- https://howtomarketagame.com/?p=1731
- https://redship.io/blog/reddit-self-promotion-rules
- https://thehiveindex.com/communities/r-indiegaming/
- https://awesome.ecosyste.ms/projects/github.com%2Fcoreyhaines31%2Fmarketingskills
- https://pypi.org/project/steamdb-mcp/
- https://awesome.ecosyste.ms/projects/github.com%2Fhawstein%2Fmcp-server-reddit
- https://impress.games/blog/best-free-presskit-tools-for-indie-games
- https://itch.io/t/2936288/which-instances-of-mastodon-are-suitable-for-game-developers
