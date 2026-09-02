---
description: Get an answer up to its word limit without padding it
argument-hint: [org name and question number]
---

Expand $1 to 90 to 100 percent of its limit. Run `tools/count.sh` first and report
the real starting count, not an estimate.

An answer at 40 percent of the limit reads as low effort even when it is tight,
because the reader is comparing it to someone who used all 250. But padding reads
worse than being short, so every added word has to be a fact rather than a cushion.

## Where the words come from, in order

Take from the top. Stop as soon as you are past 90 percent.

1. **The specific that is missing.** Almost every short answer is short because a
   number, a name, or a mechanism got left out. Look at the story in
   `you/STORY-BANK.md` and find what is in the bank but not in the answer. This fills
   most of the gap most of the time.
2. **The worst moment.** Short answers skip straight from setup to outcome. What
   happened at the point where it was going badly is usually the most interesting
   thing in the story and the first thing cut.
3. **What it cost.** Answers that claim a win without a price read thin.
4. **Who else was there.** Naming another person makes a story checkable and stops it
   reading as a solo highlight reel.
5. **The unasked question you are only half answering.** Check the block in the
   `applications/` file. If the answer covers the stated prompt and misses the unasked
   one, that miss is where the remaining words go.

## Where words never come from

- Restating the prompt.
- A closing reflection on what it taught you. That is the first thing `/cut` removes.
- Adjectives on nouns that were fine.
- A second example that makes the same point as the first.
- Anything you cannot source. **Never invent a detail to reach a word count.** Write
  `[NEED: what actually happened when the vendor pulled out]` and ask. Reaching a
  limit is not a reason to break the one rule in this repo.

## When it should stay short

Some answers are short because the story is small, and the fix is a different story
rather than more words. Say so when that is true, and name a specific alternative from
`you/STORY-BANK.md` that has enough in it to fill the limit.

A one-line prompt is not a word limit. Do not expand a favorite-snack answer.

## Report

Count before and after from `tools/count.sh`, what you added and where each addition
came from, and any `[NEED:]` you opened. If you got it to 90 percent only by adding
things you cannot source, say that plainly and leave it short.
