"""Tests for mkw.py. Run from the repository root: python -m unittest discover -s tests"""
import contextlib
import io
import json
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
