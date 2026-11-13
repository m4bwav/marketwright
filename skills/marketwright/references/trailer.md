# Procedure: trailer, GIFs and short vertical cuts

Output: `trailer-<slug>.md`, a cut list cinewright (or ffmpeg) can execute. You plan the cut; you do not edit video here. Evidence: [../kb/data.md](../kb/data.md) (Trailers), [../kb/steam.md](../kb/steam.md) (Trailers).

1. **Inventory the clips.** List each gameplay clip: file, length, what happens, the best two seconds (timestamps). If a probe is needed, `ffprobe` gives lengths. Only real gameplay from the current build qualifies; label work-in-progress footage on screen.
2. **The hook (seconds 0 to 5).** The most readable moment of the core loop, no logo first, readable muted (it autoplays muted, and the first trailer becomes Steam's 6-second micro trailer).
3. **The Steam trailer (lead, all gameplay).** Beats: hook, the core verb, escalation or variety, the twist that makes the genre fresh, a short end card (name, "Wishlist on Steam", date if known). Name each beat's clip and timestamps. No length rule exists; cut until every shot earns its place, and say so.
4. **Short vertical cuts** (TikTok, Shorts, Reels by the user's choice): 9:16 crops of the same beats, one idea each, captions for muted viewing, under the platform's length limit (check it on the day).
5. **GIFs** for the store's About section and posts: 3 to 6 seconds, one action each, loops cleanly.
6. **Music.** musicwright-game for an original cue; no licensed commercial tracks, since creators avoid footage that draws copyright claims (Hill-Whittall 2015); note any licence; AI music is disclosed like any AI content.
   Sound effects: when the sfxwright plugin is installed, hand it the shots that need a sound and read its `sounds.json` for the picked files and any disclosure. Without it, use the game's own sounds.
7. **Hand off.** A table cinewright can execute: order, source clip, in, out, crop, caption, music cue. Then ask cinewright (or give the ffmpeg commands) to cut it.
8. **Ethics check:** `MKW ethics trailer-<slug>.md`. Every shot is the game as it plays.
