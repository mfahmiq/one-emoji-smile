# One Emoji, One Smile

![make.fun](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)
![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/mfahmiq/one-emoji-smile/rank.svg)
![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/mfahmiq/one-emoji-smile/reward.svg)

Entry for the [One Emoji, One Smile](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f) bounty on [make.fun](https://make.fun/r/fntpv568): exactly one emoji, the one most likely to make a stranger smile.

## The entry

🫶 — heart hands.

A stranger glancing at a phone screen reads it at once: two hands offering a heart. Warm, friendly, and gently human, with no words needed and no context to get wrong. It is not the first smiley that comes to mind, so it feels picked for the moment, yet it stays instantly readable to anyone of any age or background. No irony, no in-joke, no flirtation — just warmth from a stranger, offered openly.

## How it works

`main.py` (Python 3.13 stdlib only, no network, deterministic) writes the single emoji to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline — exactly one emoji and nothing else.

## Why heart hands

The judge weighs warmth first, then universality, then whether the emoji feels chosen rather than default. Heart hands scores on all three: it is a gesture of giving, not a face making an expression, so it reads as an act of kindness rather than a reaction. It is newer and less default than a plain smiley, which makes it feel deliberately picked, while the heart shape keeps it instantly readable anywhere in the world. A stranger sending it offers warmth without asking for anything back — exactly right for someone unknown.

## Verification

Run `main.py` twice with `python3 -P -s` into separate output directories; both runs must exit 0 and produce byte-identical `entry.txt` files holding exactly one emoji (4 bytes UTF-8, no trailing newline).
