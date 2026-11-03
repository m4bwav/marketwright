#!/usr/bin/env bash
# Seeds the workspace with saltlight/store-page.md, a copy of skills/marketwright/evals/fixtures/saltlight
# (the eval sandbox denies reads of the plugin's evals folders). Regenerate if the fixture changes.
set -e
mkdir -p saltlight
cat > saltlight/store-page.md <<'SALTLIGHT_EOF'
# Saltlight: Steam store page draft

An invented game written for the marketwright eval suite.

Release: planned for 14 September 2027, price $14.99. Solo developer. Coming Soon page not live yet.

## Capsules

- Header capsule (920 x 430): key art of a lighthouse at dusk, the logo "Saltlight", and a banner reading "9/10 - Indie Weekly".
- Small capsule (462 x 174): the same art scaled down; the logo is about a quarter of the width.
- Main capsule (1232 x 706) and vertical capsule (748 x 896): done, art and logo only.

## Short description

Saltlight is a cozy-but-tense colony sim where you keep a lighthouse town alive on a drowning coast, rationing lamp oil through storm seasons. Wishlist now and visit www.saltlightgame.com for the devlog!

## Tags (in order)

Indie, Casual, Pixel Graphics

## Trailers

1. "Announcement": 75 seconds. Opens on a 12-second animated logo, then a pre-rendered cinematic of the lighthouse in a storm made by a freelancer, then 20 seconds of gameplay at the end.
2. "Gameplay": 2 minutes of raw play.

## Screenshots

Four: the title menu, concept art of the town, and two gameplay shots at 1920 x 1080.

## About this game

Long paragraphs, no images. The town portraits were generated with an image model and touched up by hand. The content survey's AI section has not been filled in.
SALTLIGHT_EOF
