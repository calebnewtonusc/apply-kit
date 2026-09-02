---
description: Orient a new user and tell them the one next thing to do
---

Welcome them and get them moving. Do not dump the whole system on them.

**First, check state** by reading:

- `you/PROFILE.md` and `you/STORY-BANK.md`: still the template, or filled in?
- `you/VOICE.md`: filled in?
- `you/uploads/`: anything in there besides the README?
- `TARGETS.md`: any clubs listed?
- `applications/` and `drafts/`: any real files?

**Then say, in under 200 words:**

1. What this repo does, in two sentences. It interviews them, pulls the real questions
   off each application, tells them exactly what it needs and nothing more, drafts in
   their voice, then reads the packet back as the person who receives it.
2. The one rule that protects them: it never invents a fact about them, and anything
   it does not know shows up as `[NEED: ...]` until they fill it in.
3. **The single next command to run**, based on state:
   - Nothing done: `/intake`. Say it takes about 25 minutes and it is the part that
     decides whether the drafts are good.
   - Intake done, no voice: `/voice`, and tell them to drop old essays, a personal
     statement, long texts, anything they wrote, into `you/uploads/` first.
   - Voice done, no targets: `/targets`.
   - Targets set, no application files: `/extract`, one club at a time.
   - Questions extracted: `/gaps`.
   - Gaps answered: `/draft <club>`.
   - Drafts exist: `/truth`, then `/slop`, then `/reader`.

Then stop and let them run it. Do not run the next command for them unless they say
go. This is the only command in the kit where you wait.

One more thing to mention once, briefly: if any of their clubs ban AI in recruitment,
tell you now and you will not write anything they submit for that club.
