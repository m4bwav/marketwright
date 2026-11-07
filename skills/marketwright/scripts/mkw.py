#!/usr/bin/env python3
"""marketwright CLI: the checkable parts of honest indie game marketing.

Standard library only (Python 3.9+). Every number it prints names its source; a number with no source is not printed.

  mkw.py assets <folder>                 match images to Steam asset sizes, list what is missing
  mkw.py timeline --release YYYY-MM-DD   milestones back from a release date (Next Fest, reviews, sales to avoid)
  mkw.py wishlists --count N             first-week and first-month sales ranges from published ratios
  mkw.py lint <page.json>                Steam page lint against Valve's written rules
  mkw.py ethics <plan.md>                flag tactics a community would call slimy, with the honest version
  mkw.py communities --genre G           communities for a genre, with their self-promotion rule and check date
"""
import argparse
import datetime as dt
import json
import re
import struct
import sys
from pathlib import Path

VERSION = "0.4.3"
HERE = Path(__file__).resolve().parent
KB = HERE.parent / "kb"

# Valve, partner.steamgames.com/doc/store/assets/standard and /assets (checked 2026-11-02).
ASSETS = [
    ("header capsule", 920, 430, True),
    ("small capsule", 462, 174, True),
    ("main capsule", 1232, 706, True),
    ("vertical capsule", 748, 896, True),
    ("page background", 1438, 810, False),
    ("library capsule", 600, 900, True),
    ("library hero", 3840, 1240, True),
    ("event cover", 800, 450, False),
    ("event header", 1920, 622, False),
]
ASSET_SRC = "partner.steamgames.com/doc/store/assets (checked 2026-11-02)"

# Ratios of sales to launch wishlists. (label, low, high, source)
RATIOS = [
    ("first week, median, Aug-Oct 2024 releases with 5k+ wishlists", 0.105, 0.105,
     "GameDiscoverCo via Game World Observer, 2024-12-06"),
    ("first week, median, 2024-25 releases with 25k+ wishlists", 0.15, 0.15,
     "GameDiscoverCo as cited by Inven Global, 2026-10-15"),
    ("first month, average per wishlist, 2023-25 cohort (126 games)", 0.22, 0.22,
     "Chris Zukowski's data via Inven Global, 2026-10-15 (was 0.45 for 2020-22)"),
]

# Median wishlists gained during the February 2026 Next Fest, by wishlists before it.
# howtomarketagame.com/2025/03/26/benchmarks-how-many-wishlists-can-i-get-from-steam-next-fest/ (updated 2026-04-08)
NEXTFEST = [(0, 999, 322, 71), (1000, 9999, 1006, 60), (10000, 99999, 5215, 36), (100000, None, 12882, 7)]

# Steam events with published dates, partner.steamgames.com/doc/marketing/upcoming_events (checked 2026-11-02).
NEXTFEST_DATES = [("2027-02-22", "2027-03-01"), ("2027-06-14", "2027-06-21")]
SALES = [
    ("Winter Sale", "2026-12-17", "2027-01-04"),
    ("Spring Sale", "2027-03-18", "2027-03-25"),
    ("Summer Sale", "2027-06-24", "2027-07-08"),
]


def image_size(path):
    """(width, height) of a PNG or JPEG, read from its header; None for anything else."""
    with open(path, "rb") as f:
        head = f.read(26)
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            return struct.unpack(">II", head[16:24])
        if head[:2] != b"\xff\xd8":
            return None
        f.seek(2)
        while True:
            b = f.read(1)
            while b and b != b"\xff":
                b = f.read(1)
            while b == b"\xff":
                b = f.read(1)
            if not b:
                return None
            marker = b[0]
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                continue
            seg = f.read(2)
            if len(seg) < 2:
                return None
            n = struct.unpack(">H", seg)[0]
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                h, w = struct.unpack(">xHH", f.read(5))
                return w, h
            f.seek(n - 2, 1)


def cmd_assets(a):
    folder = Path(a.folder)
    found, shots, other = {}, [], []
    for p in sorted(folder.iterdir()):
        if p.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            continue
        size = image_size(p)
        if not size:
            other.append((p.name, "unreadable"))
            continue
        w, h = size
        kind = next((k for k, aw, ah, _ in ASSETS if (aw, ah) == (w, h)), None)
        if kind:
            found.setdefault(kind, []).append(p.name)
        elif w >= 1920 and h >= 1080 and abs(w / h - 16 / 9) < 0.01:
            shots.append(p.name)
        else:
            other.append((p.name, "%dx%d" % (w, h)))
    bad = 0
    for kind, w, h, req in ASSETS:
        names = found.get(kind)
        mark = "ok  " if names else ("MISS" if req else "opt ")
        bad += (not names) and req
        print("%s %-17s %4dx%-4d %s" % (mark, kind, w, h, ", ".join(names or [])))
    ok_shots = len(shots) >= 5
    bad += not ok_shots
    print("%s screenshots       %d at 1920x1080 or larger, 16:9 (need 5)" % ("ok  " if ok_shots else "MISS", len(shots)))
    for name, why in other:
        print("??   %s: %s matches no Steam size" % (name, why))
    print("library logo is checked by eye: 1280 wide and/or 720 tall .png on transparency, no other words")
    print("source: " + ASSET_SRC)
    return 1 if bad else 0


def d(s):
    return dt.date.fromisoformat(s)


def business_days_before(day, n):
    while n:
        day -= dt.timedelta(days=1)
        if day.weekday() < 5:
            n -= 1
    return day


def cmd_timeline(a):
    rel = d(a.release)
    rows = []
    for name, s, e in SALES:
        if d(s) - dt.timedelta(days=7) <= rel <= d(e) + dt.timedelta(days=7):
            rows.append((rel, "WARN release is within a week of the %s (%s to %s): pick another date" % (name, s, e)))
    fest = None
    for s, e in NEXTFEST_DATES:
        if d(e) < rel:
            fest = (d(s), d(e))
    if a.nextfest:
        fest = (d(a.nextfest), d(a.nextfest) + dt.timedelta(days=7))
    live = rel - dt.timedelta(days=14)
    why = "latest day the Coming Soon page can go live (two weeks, Valve rule); aim for months earlier"
    if fest and fest[0] - dt.timedelta(weeks=5) < live:
        live = fest[0] - dt.timedelta(weeks=5)
        why = "latest day the Coming Soon page can go live: Next Fest needs a public page, set here with the demo review"
    rows.append((live, why))
    rows.append((business_days_before(live, 7), "submit the store page for review (7 business days ahead, Valve)"))
    rows.append((rel - dt.timedelta(days=7), "set the launch discount now if you want one (10 to 40 percent, 7 to 14 days)"))
    if fest:
        s, e = fest
        rows += [
            (s - dt.timedelta(weeks=5), "Next Fest: demo submitted for review, to be in the press preview (5 weeks)"),
            (s - dt.timedelta(days=11), "Next Fest press preview starts (11 days before)"),
            (s - dt.timedelta(weeks=3), "Next Fest: last day to submit the demo for review (3 weeks)"),
            (s, "Next Fest starts (one per game, ever; the game must still be unreleased when it ends)"),
            (e, "Next Fest ends"),
        ]
    else:
        rows.append((rel, "no published Next Fest ends before this release; check the events page for newer dates"))
    rows.append((rel, "RELEASE (press Release App yourself; wishlisters get an email)"))
    today = dt.date.today()
    for day, what in sorted(rows):
        late = "  (past)" if day < today else ""
        print("%s  %s%s" % (day.isoformat(), what, late))
    print("sources: partner.steamgames.com/doc/store/coming_soon, /store/releasing, /marketing/upcoming_events/nextfest, "
          "/marketing/discounts (checked 2026-11-02)")
    return 0


def cmd_wishlists(a):
    n = a.count
    print("launch wishlists: %d" % n)
    for label, lo, hi, src in RATIOS:
        print("  %-62s ~%d sales  (x%.3g; %s)" % (label, round(n * lo), lo, src))
    for lo, hi, med, cnt in NEXTFEST:
        if n >= lo and (hi is None or n <= hi):
            print("  Next Fest median gain for a game at this size: %d wishlists (n=%d; Zukowski survey of Feb 2026 fest)"
                  % (med, cnt))
    print("these are medians of other games, not a forecast; quote a range and the source, never one number")
    return 0


PHRASES_TIMED = re.compile(r"\b(now available|available now|out now|wishlist now|coming soon|on sale)\b", re.I)
LINK = re.compile(r"(https?://|www\.|\b[a-z0-9-]+\.(com|net|org|io|gg|games)\b)", re.I)
CAPSULE_BANNED = re.compile(r"(\d(\.\d)?\s*/\s*10|\b\d{2,3}\s*%|award|winner|goty|metacritic|wishlist|buy now|sale|"
                            r"pre-?order|prepurchase|out now|available)", re.I)


def cmd_lint(a):
    page = json.loads(Path(a.page).read_text(encoding="utf-8"))
    out = []

    def say(level, msg):
        out.append((level, msg))

    short = page.get("short_description", "")
    if not short:
        say("ERROR", "no short description")
    elif len(short) > 300:
        say("WARN", "short description is %d characters; Valve says a few hundred, keep it near 300 or under" % len(short))
    if PHRASES_TIMED.search(short):
        say("WARN", "short description has a time-bound phrase (%s); Valve asks to avoid them" % PHRASES_TIMED.search(short).group(0))
    for field in ("short_description", "about"):
        m = LINK.search(page.get(field, ""))
        if m:
            say("ERROR", "%s links or names a website (%s); Valve bans links in the description" % (field, m.group(0)))
    tags = page.get("tags", [])
    if len(tags) < 5:
        say("ERROR", "%d tags; at least 5 are required before launch" % len(tags))
    elif len(tags) > 20:
        say("WARN", "%d tags; only the top 20 count" % len(tags))
    shots = page.get("screenshots", 0)
    if shots < 5:
        say("ERROR", "%d screenshots; at least 5 are required" % shots)
    for text in page.get("capsule_text", []):
        m = CAPSULE_BANNED.search(text)
        if m:
            say("ERROR", "capsule text '%s' breaks the capsule rules (%s): only art, the name and an official subtitle" % (text, m.group(0)))
    if page.get("trailers", 0) < 1:
        say("WARN", "no trailer; the first trailer autoplays muted and becomes the micro trailer")
    if page.get("first_trailer_gameplay") is False:
        say("WARN", "the first trailer is not mostly gameplay; Valve highly recommends it is")
    if page.get("uses_ai") and not page.get("ai_disclosure"):
        say("ERROR", "the game uses AI content players see but the page has no AI disclosure")
    for level, msg in out:
        print("%-5s %s" % (level, msg))
    print("%d errors, %d warnings. sources: partner.steamgames.com/doc/store/page/description, /store/tags, "
          "/store/assets/rules, /store/trailer, /gettingstarted/contentsurvey (checked 2026-11-02)"
          % (sum(l == "ERROR" for l, _ in out), sum(l == "WARN" for l, _ in out)))
    return 1 if any(l == "ERROR" for l, _ in out) else 0


def near(a, b, gap=40):
    """a and b in either order, at most gap characters apart in one sentence."""
    w = r"[^.\n]{0,%d}" % gap
    return r"(?:%s)%s(?:%s)|(?:%s)%s(?:%s)" % (a, w, b, b, w, a)


REVIEW = r"\breview(s|ed|ing)?\b(?! cop(y|ies)| keys?)"
REWARD = r"\b(free|reward\w*|bonus|gems?|coins?|dlc|keys?|gifts?|prizes?|discount|skins?)\b"
AI = r"\b(ai|generative|gen-?ai|midjourney|stable diffusion|chatgpt)\b"
PAID = r"\b(paid|sponsor\w*|gifted|free keys?|partnership|pay(ing)? (an? |the )?(streamer|creator|youtuber|influencer)s?)\b"
SAY = r"(disclos\w*|mention\w*|tell\w*|say\w*|label\w*|list\w*|tag\w*|#ad)"

# (pattern, what it is, honest version). Grey-zone rows say so. Each rule matches both word orders
# (near); tests/test_mkw.py holds a flagged and a clean sentence set for every rule.
SLIME = [
    (near(r"\bswap\w*|\b(?<!in )exchang\w*|\btrad(e|es|ed|ing)\b(?! press)", REVIEW, 25), "review swap",
     "Ask for reviews only outside the game, with no reward and no swap. Steam bans incentivised reviews; the FTC rule (16 CFR 465) bans paid or fake ones."),
    (near(REWARD, r"\b(leave|leaving|write|writing|post|posting|for (a|every|each|your)|in exchange for|in return for|if you leave)\s+"
               r"(a |an |your |their |us )?(steam |positive |good |5-star )?reviews?\b")
     + r"|review (it|us|the game)\b[^.\n]{0,40}\b(get|receive|unlock|we (send|give))|" + REVIEW
     + r"[^.\n]{0,30}\b(in exchange for|in return for|to (get|unlock|receive))\b", "reward for a review",
     "No reward of any kind for a review (Steam rule). Ask once, in a news post or newsletter, never in the game."),
    (near(r"in[- ]game|inside the game|from the game|the game (asks|prompts|shows|reminds)|pop[- ]?ups?", r"\breview", 50),
     "in-game review prompt",
     "Steam bans asking for reviews from inside the game. Ask in a Steam news post, devlog or newsletter."),
    (r"sock ?puppet|alt(ernate)? accounts?|fake accounts?|second account|burner accounts?|"
     r"\b(make|create|open|use|from|with)\b[^.\n]{0,20}\b(several|a few|multiple|extra|other|new)\b[^.\n]{0,10}accounts|"
     r"\b(pose|posing|pretend\w*)( to be| as)( an?)? (\w+ )?(players?|fans?|customers?)\b|"
     r"as if (they|we|i) (were|was) (an? )?(\w+ )?(players?|fans?|customers?)\b", "astroturfing",
     "Post as yourself, say you are the developer every time. Communities find sock puppets (the 2025 Trap Plan case) and the ban follows."),
    (r"astroturf", "astroturfing", "Post as yourself and say you made it."),
    (r"\b(buy\w*|bought|purchas\w*|pay(ing)? for)\s+(\d[\d,k]*\s+|some\s+|more\s+|fake\s+|cheap\s+)*"
     r"(wishlists|followers|likes|upvotes|views|reviews|subscribers)\b|"
     r"(followers|wishlists|upvotes|views|likes|subscribers)[^.\n]{0,30}\b(paid|follower|bot) (service|accounts?|farm)|"
     r"bot (followers|upvotes|views|accounts)", "bought metrics",
     "Never buy followers, views, upvotes or wishlists: the FTC rule bans fake social indicators, and fake wishlists wreck the numbers you plan with."),
    (near(r"\bswap\w*|\btrad(e|es|ed|ing)\b|\bexchang\w*", r"\b(wishlists?|follows?|followers|upvotes?|subs|subscribers)\b", 25)
     + r"|wishlist[- ]for[- ]wishlist|w4w|follow[- ]for[- ]follow|f4f|upvote[- ]for[- ]upvote|sub4sub", "metric swaps",
     "Skip swaps: the wishlists come from people who will not buy, and Steam reads them as real interest."),
    (r"(vote|upvote) ring|brigad|\b(ask|get|have|tell)\w*\b[^.\n]{0,30}\b(friends|discord|the team|server|community|everyone|family)\b"
     r"[^.\n]{0,20}\bupvot", "vote manipulation",
     "Never organise votes. Share the post where people can find it and let it stand on its own."),
    (r"(post|share|crosspost|spam)\w*[^.\n]{0,30}\b(every|all|many|\d{2,}|as many)\b[^.\n]{0,15}\b(subreddits?|subs|communities|servers|forums|groups)\b",
     "mass posting",
     "Pick the two or three communities where the game fits, read each one's rules, use their flair and threads, answer comments, space posts out."),
    (r"pre-?rendered|cinematic (footage|trailer)|target render|bullshot|(fake|mock|staged)[- ]gameplay|not (actual|real) gameplay|"
     r"render\w*[^.\n]{0,30}\bas (actual |real |in-game )?gameplay|"
     + near(r"\b(footage|trailer|gameplay|clips?)\b", r"\b(cut|removed|dropped|scrapped)\b", 30), "misleading footage",
     "Show the game as it plays. Label early footage (work in progress). A disclaimer does not cure a misleading ad (ASA, Playrix 2020)."),
    (r"(fake|artificial) (scarcity|urgency)|only \d+ (copies|keys) left|\bhurry\b|(last chance|limited time|ending soon)(?![^.\n]{0,60}\b(until|ends?|on) \w+ \d)", "urgency without a real date",
     "Grey zone: a real offer is fine. Give the true end date and keep it; never fake stock or countdowns."),
    (near(r"(don'?t|do not|won'?t|will not|never|without|not to|no need to|skip)\s+(\w+\s+)?" + SAY
          + r"|\bhid(e|ing)\b|keep (it )?(quiet|secret)|\bleave\b[^.\n]{0,15}\boff\b|no one will know", AI)
     + r"|\bleave\b[^.\n]{0,20}" + AI + r"[^.\n]{0,20}\boff\b|without disclosing", "hidden AI use",
     "Disclose AI content players see on Steam's content survey, the store page and the press kit. Hiding it is what turned the backlash cases."),
    (near(r"\b(don'?t|do not|won'?t|not|never|without|skip|no)\b[^.\n]{0,15}" + SAY + r"|\bno (disclosure|label)", PAID),
     "undisclosed paid coverage",
     "Paid or gifted coverage is disclosed (#ad, the platform's paid partnership label). FTC and ASA both require it; ask creators to disclose free keys."),
    (r"(only|just) (positive|good) reviews|"
     + near(r"\bkeys?\b|\bcop(y|ies)\b", r"\b(only|if|as long as|provided)\b[^.\n]{0,40}\b(positive|good|recommend\w*|favou?rable)\b"
            r"|\b(positive|good|favou?rable)\b[^.\n]{0,25}\b(required|only)\b"), "conditional keys",
     "Send keys with no condition on the verdict. Steam allows press and creator copies; a condition on the verdict makes it a paid review."),
    (r"review[- ]?bomb|bomb\w* (their|its|the|his|her) reviews", "review bombing",
     "Never organise or invite review bombs, for or against anyone."),
    (r"\bg2a\b|kinguin|eneba|key resell\w*|(grey|gray)[- ]market", "grey-market keys",
     "Sell through Steam and stores you trust; send creator keys yourself, log them, and vet requesters (Valve warns of fake journalists)."),
    (r"dark pattern|confirmshaming|fomo (pop|timer)|fake (countdown|timer)|pay to (skip|win)[^.\n]{0,20}nag", "dark pattern",
     "Remove it. A store page or game that tricks players costs more goodwill than it earns."),
]


def cmd_ethics(a):
    text = Path(a.plan).read_text(encoding="utf-8")
    hits = []
    for n, line in enumerate(text.splitlines(), 1):
        for pat, what, honest in SLIME:
            m = re.search(pat, line, re.I)
            if m:
                hits.append((n, what, m.group(0), honest))
    seen = set()
    for n, what, frag, honest in hits:
        if (n, what) in seen:
            continue
        seen.add((n, what))
        print("line %d: %s ('%s')\n  honest version: %s" % (n, what, frag, honest))
    print("%d flagged. The scan finds words, not intent: still ask of every step, would this embarrass you if the "
          "community saw how it was done?" % len(seen))
    return 1 if seen else 0


def cmd_communities(a):
    rows = json.loads((KB / "communities.json").read_text(encoding="utf-8"))
    g = a.genre.lower()
    picked = [r for r in rows if any(g in x.lower() for x in r["genres"]) or ("general" in r["genres"] and a.general)]
    if not picked:
        print("no community listed for '%s'; genres known: %s" % (a.genre, ", ".join(sorted({x for r in rows for x in r["genres"]}))))
        return 1
    for r in picked:
        alive = r.get("alive", "not probed")
        print("%-24s %-9s self-promo %-10s %s | alive: %s | rule checked %s (%s)" % (
            r["name"], r["platform"], r["self_promo"], r["rule_summary"], alive, r["checked"], r["confidence"]))
    print("read each community's rules page yourself before posting; rules change and these were not all read live")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="mkw.py", description=__doc__.split("\n")[0])
    p.add_argument("--version", action="version", version="mkw.py " + VERSION)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("assets"); s.add_argument("folder"); s.set_defaults(f=cmd_assets)
    s = sub.add_parser("timeline"); s.add_argument("--release", required=True); s.add_argument("--nextfest")
    s.set_defaults(f=cmd_timeline)
    s = sub.add_parser("wishlists"); s.add_argument("--count", type=int, required=True); s.set_defaults(f=cmd_wishlists)
    s = sub.add_parser("lint"); s.add_argument("page"); s.set_defaults(f=cmd_lint)
    s = sub.add_parser("ethics"); s.add_argument("plan"); s.set_defaults(f=cmd_ethics)
    s = sub.add_parser("communities"); s.add_argument("--genre", required=True)
    s.add_argument("--general", action="store_true", help="also list the general indie spaces")
    s.set_defaults(f=cmd_communities)
    a = p.parse_args(argv)
    return a.f(a)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
