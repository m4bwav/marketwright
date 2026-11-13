# Procedure: Steam store page review

Output: `store-review-<slug>.md`, findings ranked by impact, each with the rule or source it rests on. Read [../kb/steam.md](../kb/steam.md).

1. **Get the page.** A live URL (read it), a saved page, or the user's draft. Write what can be checked into `page.json` beside the review: `short_description`, `about`, `tags` (in order), `screenshots` (count), `trailers` (count), `first_trailer_gameplay` (true or false), `capsule_text` (every word on the capsules), `uses_ai`, `ai_disclosure`, and `press_headline` when a press release is drafted. Run `MKW lint page.json`.
2. **Assets.** If the user has the image files, `MKW assets <folder>`: missing sizes, pre-2024 sizes, screenshots under 1920 x 1080.
3. **Judge what the script cannot**, in this order (the order a shopper meets them):
   - Capsule: does it say the genre at small-capsule size (462 x 174)? Is the name legible there? Text beyond name and subtitle is a rule break, not a style note. Judge it at real size in a row of the genre's rivals, and design the small capsule on its own rather than cropping the header. When the complaint is a low click rate, read the traffic breakdown by surface first: a broad fest audience clicks less than similar-game browsers, so the art may not be the problem.
   - First trailer: gameplay in the first seconds, readable muted, the core loop shown. Handoff: references/trailer.md.
   - Short description: genre, hook and the player's verb in the first sentence; no time-bound phrases.
   - Screenshots: first four show the core loop at play, not menus or art; varied; all are gameplay.
   - Tags: the first five are the genre a buyer would search, in order of truth, not of popularity.
   - About section: GIFs of play, short paragraphs, textless images where it will be localised.
   - AI disclosure present when players see AI content; plain wording.
   - Coming Soon timing against the release (at least two weeks; earlier is better).
4. **Write findings**: `severity` (rule break, high, medium, low), what, why (Valve's rule or a dated source), the fix, and who makes it (brandwright for capsules, cinewright for trailers). A rule break leads.
5. **Ethics check** on any copy you wrote: `MKW ethics store-review-<slug>.md`.

Other stores (consoles, Epic, GOG, itch) want short, medium and long descriptions, localised copy and an IARC or regional age rating; start them weeks before the page goes live (Futter 2017, p. 108).

Pixel art capsules: brandwright makes, pixelwright cleans, artwright-pixel judges.
