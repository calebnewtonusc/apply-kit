---
description: Write one club's answers
argument-hint: [club name]
---

Draft every answer for **$1** into `drafts/<Club Name>.md`.

## Before writing a word

1. **Check the AI policy** in that club's `applications/` file. If `banned`, do not
   draft. Say so in one sentence and switch to the mode described in `AI-POLICY.md`.
2. Read `you/PROFILE.md`, `you/STORY-BANK.md`, `you/VOICE.md`, `you/DISCLOSURE.md`.
3. Read the club's `applications/` file, especially the unasked question under each
   prompt. Those change which story you pick, not just how you tell it.
4. Load `application-writing`, `no-slop-writing`, and `honesty-guard`.

## While writing

**Match their voice**, per `you/VOICE.md`. The target is their sentences, not yours.

**Never invent a fact.** `[NEED: how many people]` inline, and collect every marker at
the bottom of the file. Six markers is a good draft.

**Answer the unasked question**, not only the stated one.

**Hit 90 to 100 percent of every word limit** and put the exact count next to each
answer, like `247 / 250`.

**No repeated story within one application.** Track which story each answer uses and
list it in the file.

**Vary the shape across answers.** If three of them run "here is what I built, here is
what I lack, teach me," rewrite one to be what they will do for the club.

**Respect `you/DISCLOSURE.md`** without exception and without relitigating it.

## The file

For each question: the prompt verbatim, the limit, the draft, the word count, which
story it uses, and any `[NEED:]` items. Then at the bottom:

- Every `[NEED:]` collected in one list
- The dead-lines grep check for that club, run and reported
- A one-line honest note on which answer is weakest and why

## Then

Report in a short message: how many answers, how many `[NEED:]` items block
submission, the strongest answer and why, and the weakest. Do not describe every
answer back to them. They can read the file.

Point them at `/truth` next.
