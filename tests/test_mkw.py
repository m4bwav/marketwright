"""Tests for mkw.py. Run from the repository root: python -m unittest discover -s tests"""
import contextlib
import io
import json
import re
import struct
import sys
import tempfile
import unittest
import zlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "skills" / "marketwright" / "scripts"))
import mkw  # noqa: E402


def png(path, w, h):
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)
    chunk = b"IHDR" + ihdr
    data = b"\x89PNG\r\n\x1a\n" + struct.pack(">I", 13) + chunk + struct.pack(">I", zlib.crc32(chunk))
    Path(path).write_bytes(data)


def jpeg(path, w, h):
    sof = b"\xff\xc0" + struct.pack(">HBHHB", 11, 8, h, w, 1) + b"\x01\x11\x00"
    Path(path).write_bytes(b"\xff\xd8" + b"\xff\xe0" + struct.pack(">H", 4) + b"\x00\x00" + sof + b"\xff\xd9")


def run(argv):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = mkw.main(argv)
    return code, out.getvalue()


class Assets(unittest.TestCase):
    def test_sizes_from_headers(self):
        with tempfile.TemporaryDirectory() as t:
            png(Path(t, "a.png"), 920, 430)
            jpeg(Path(t, "b.jpg"), 1232, 706)
            self.assertEqual(mkw.image_size(Path(t, "a.png")), (920, 430))
            self.assertEqual(mkw.image_size(Path(t, "b.jpg")), (1232, 706))

    def test_complete_set_passes(self):
        with tempfile.TemporaryDirectory() as t:
            for i, (_, w, h, req) in enumerate(mkw.ASSETS):
                if req:
                    png(Path(t, "%d.png" % i), w, h)
            for i in range(5):
                png(Path(t, "shot%d.png" % i), 1920, 1080)
            code, out = run(["assets", t])
            self.assertEqual(code, 0, out)

    def test_missing_and_odd_sizes(self):
        with tempfile.TemporaryDirectory() as t:
            png(Path(t, "header.png"), 460, 215)  # the pre-2024 size Valve no longer accepts
            code, out = run(["assets", t])
            self.assertEqual(code, 1)
            self.assertIn("MISS header capsule", out)
            self.assertIn("header.png: 460x215 matches no Steam size", out)


class Timeline(unittest.TestCase):
    def test_business_days(self):
        # Friday 2027-09-17 minus 7 business days is Wednesday 2027-09-08
        self.assertEqual(mkw.business_days_before(mkw.d("2027-09-17"), 7).isoformat(), "2027-09-08")

    def test_picks_last_fest_before_release(self):
        code, out = run(["timeline", "--release", "2027-09-14"])
        self.assertIn("2027-06-14  Next Fest starts", out)
        self.assertIn("2027-05-10  Next Fest: demo submitted", out)  # 5 weeks before
        # Next Fest needs a public page, so the page deadline moves to the demo review, not two weeks before release
        self.assertIn("2027-05-10  latest day the Coming Soon page can go live: Next Fest", out)
        self.assertNotIn("2027-08-31", out)

    def test_no_fest_uses_two_week_rule(self):
        code, out = run(["timeline", "--release", "2027-01-20"])
        self.assertIn("2027-01-06  latest day the Coming Soon page can go live (two weeks", out)

    def test_sale_clash_warns(self):
        code, out = run(["timeline", "--release", "2026-12-20"])
        self.assertIn("WARN release is within a week of the Winter Sale", out)


class Wishlists(unittest.TestCase):
    def test_ratios_cite_sources(self):
        code, out = run(["wishlists", "--count", "10000"])
        self.assertIn("~1050 sales", out)
        self.assertIn("~2200 sales", out)
        self.assertIn("Next Fest median gain for a game at this size: 5215", out)
        for _, _, _, src in mkw.RATIOS:
            self.assertIn(src, out)


class Lint(unittest.TestCase):
    def lint(self, page):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t, "page.json")
            p.write_text(json.dumps(page), encoding="utf-8")
            return run(["lint", str(p)])

    def test_clean_page(self):
        code, out = self.lint({"short_description": "Build a lighthouse colony on a drowned coast.",
                               "tags": ["Colony Sim", "Base Building", "Pixel Graphics", "Survival", "Singleplayer"],
                               "screenshots": 6, "trailers": 1, "capsule_text": ["Saltlight"]})
        self.assertEqual(code, 0, out)

    def test_breaks(self):
        code, out = self.lint({"short_description": "Wishlist now! Visit www.saltlight.com", "tags": ["Indie"],
                               "screenshots": 3, "capsule_text": ["Saltlight - 9/10 IGN"], "uses_ai": True})
        self.assertEqual(code, 1)
        for want in ("time-bound phrase", "names a website", "1 tags", "3 screenshots", "capsule rules",
                     "no AI disclosure"):
            self.assertIn(want, out)


class Ethics(unittest.TestCase):
    def scan(self, text):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t, "plan.md")
            p.write_text(text, encoding="utf-8")
            return run(["ethics", str(p)])

    def test_flags_slime(self):
        code, out = self.scan("Week 1: make three alt accounts to hype the game on r/indiegames.\n"
                              "Week 2: give a free DLC key for a positive review.\n"
                              "Week 3: join a wishlist for wishlist group.\n"
                              "Week 4: post the trailer to 30 subreddits.\n"
                              "Trailer: use the cinematic footage, it looks better.\n")
        self.assertEqual(code, 1)
        for want in ("astroturfing", "reward for a review", "metric swaps", "mass posting", "misleading footage"):
            self.assertIn(want, out)

    def test_reward_named_after_review(self):
        code, out = self.scan("Ask friends to leave a review in exchange for a free key.\n")
        self.assertEqual(code, 1)
        self.assertIn("reward for a review", out)

    def test_honest_plan_passes(self):
        code, out = self.scan("Post a devlog on r/IndieDev using its flair, as the developer.\n"
                              "Send keys to 20 creators who cover colony sims, no conditions; ask them to disclose.\n"
                              "Launch discount 15 percent for 7 days, ends on 21 September.\n")
        self.assertEqual(code, 0, out)

    def test_dated_offer_is_not_fake_urgency(self):
        code, out = self.scan("Limited time founder price, ends on September 21.\n")
        self.assertEqual(code, 0, out)
        code, out = self.scan("Limited time founder price, act fast!\n")
        self.assertEqual(code, 1)

    # Every rule, in more than one word order; the scan must flag each with its own rule.
    FLAGGED = {
        "review swap": ["We could swap reviews with another dev", "Reviews swapped with other devs",
                        "exchange reviews with a friend's game"],
        "reward for a review": ["Leave a review and get a free key", "Write a review to receive bonus gems",
                                "For every review we give a free DLC", "review it and we send you a gift"],
        "in-game review prompt": ["Pop up a review request in game after level 3",
                                  "After the boss, the game asks players to review it on Steam",
                                  "Remind players inside the game to leave a review"],
        "astroturfing": ["Post from an alt account", "Make a few accounts and pretend to be fans",
                         "Have friends post as if they were random players"],
        "bought metrics": ["Buy 500 wishlists", "Get followers from a paid service", "purchase upvotes",
                           "pay for wishlists", "buy some fake reviews"],
        "metric swaps": ["Swap wishlists with other devs", "Trade follows with other studios", "wishlist swap thread"],
        "vote manipulation": ["Ask our Discord to upvote the post", "Get the team to upvote it in the first hour",
                              "have friends upvote"],
        "mass posting": ["Post it to 20 subreddits", "Crosspost to every subreddit we can find",
                         "share in as many subreddits as possible"],
        "misleading footage": ["Use the cinematic render as gameplay", "Show footage from a cut build",
                               "trailer with gameplay we removed"],
        "urgency without a real date": ["Hurry, limited time only!", "Only 50 keys left", "Last chance to wishlist"],
        "hidden AI use": ["Don't disclose the AI art", "Leave AI off the content survey",
                          "We won't mention we used Midjourney", "Keep quiet about the generative AI"],
        "undisclosed paid coverage": ["Ask the creator not to label the sponsorship", "Pay a streamer and skip the #ad",
                                      "sponsored video with no disclosure", "Tell them not to say it's paid"],
        "conditional keys": ["Send keys only to creators who will recommend it",
                             "Keys only if they promise a positive review", "positive coverage required for a key"],
        "review bombing": ["Get people to review-bomb the rival game", "Bomb their reviews"],
        "grey-market keys": ["Sell keys on G2A", "Put keys on a key reseller site", "use a grey market"],
        "dark pattern": ["Use confirmshaming on the unsubscribe", "Add a fake countdown timer"],
    }
    CLEAN = ["Send free keys to press and creators with no conditions", "Ask for reviews in a Steam news post after launch",
             "Run paid ads on Reddit to get wishlists", "Disclose the AI art on the store page and the content survey",
             "Creators disclose free keys with #ad", "Post in two subreddits that fit and follow their rules",
             "Our trailer shows only gameplay captured from the current build", "The 50% launch discount ends on March 9",
             "Trade press reviews matter less than creators", "Send review copies to curators",
             "Answer negative reviews politely", "We avoid AI art in the capsule",
             "Ask your Discord for feedback on the trailer", "Reply to every comment for the first day",
             "Tell the creator the key is free and ask them to label it #ad", "Read every review and fix what players hit",
             "Show the trailer to friends before release", "Send keys to creators who cover the genre"]

    def test_every_rule_both_orders(self):
        for what, sentences in self.FLAGGED.items():
            for s in sentences:
                with self.subTest(rule=what, sentence=s):
                    self.assertTrue(any(w == what and re.search(p, s, re.I) for p, w, _ in mkw.SLIME))

    def test_honest_sentences_stay_clean(self):
        for s in self.CLEAN:
            with self.subTest(sentence=s):
                self.assertEqual([w for p, w, _ in mkw.SLIME if re.search(p, s, re.I)], [])


class Communities(unittest.TestCase):
    def test_genre_lookup(self):
        code, out = run(["communities", "--genre", "roguelike"])
        self.assertEqual(code, 0)
        self.assertIn("r/roguelikes", out)

    def test_unknown_genre_lists_known(self):
        code, out = run(["communities", "--genre", "zzz"])
        self.assertEqual(code, 1)
        self.assertIn("genres known", out)


if __name__ == "__main__":
    unittest.main()
