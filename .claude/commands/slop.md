---
description: Find the sentences that read as AI-written or as generic filler
argument-hint: [optional: org name, or blank for all drafts]
---

Load `no-slop-writing`. Run in **detect mode** by default. Do not rewrite unless they
ask, because a scan they act on themselves teaches the pattern and a silent rewrite
does not.

Scan $1 if given, otherwise every file in `drafts/`. Write `review/SLOP.md`.

## Report, in this order

**1. Portability failures.** The most important section. Every sentence that could
appear in another applicant's essay to another org unchanged, quoted, with the file
and question. For each, one line on what would make it theirs: a name, a number, a
mechanism, an opinion someone could disagree with.

Run this on every opening sentence first. That is where filler costs the most.

**2. Machine tics.** Quoted, with the fix. Em dashes, binary contrasts, throat
clearing, colon reveals, closing aphorisms, importance puffery, `-ing` clauses,
rule-of-three lists, dramatic fragments.

**3. Banned words**, with a count and locations.

**4. Voice mismatch.** Compare against `you/VOICE.md`. Any sentence that does not
sound like them, quoted, with what is off about it. Rhythm, register, or humor written
in a mode they do not use.

**5. One judgment.** Does this packet read as this person or as a competent stranger?
Answer in two sentences, honestly.

## Then

Give the three edits that would most improve the packet, specific and quoted. If they
ask you to apply them, switch to rewrite mode: fix the pattern, change nothing else,
and show before and after for anything you touched so they can veto it.
