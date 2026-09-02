---
description: Say where things stand and what happens next
---

**You should almost never need this.** The session-start hook already briefs you on
where things stand, and `CLAUDE.md` tells you how to open. This exists for when someone
types it, or asks "where am I."

Welcome them and get them moving. Do not dump the whole system on them, and do not list
commands back at them. They do not use commands.

**First, check state** by reading:

- `you/PROFILE.md` and `you/STORY-BANK.md`: still the template, or filled in?
- `you/VOICE.md`: filled in?
- `you/uploads/`: anything in there besides the README?
- `you/OUTCOMES.md`: any past cycles recorded? If so, read them. What happened last time
  changes where this cycle starts.
- `TARGETS.md`: anything listed, and does each one have a type?
- `applications/` and `drafts/`: any real files?

**Then say, in under 250 words:**

1. What this repo does, in two sentences. It interviews them, pulls the real questions
   off each application, tells them exactly what it needs and nothing more, drafts in
   their voice, then reads the packet back as the person who receives it.
2. The rule that protects them: it never invents a fact, about them or about the org,
   and anything it does not know shows up as `[NEED: ...]` until they fill it in.
3. **What they are applying to**, if `TARGETS.md` is empty. Ask once, in one line, and
   accept a rough answer: clubs, jobs and internships, fellowships or scholarships, grad
   school, grants, accelerators, or a mix. A mix is normal. This decides which brief in
   `reference/` gets read before anything is written, and getting it wrong produces
   confident advice aimed at the wrong reader.
4. **Then do the next thing yourself**, based on state. Do not name a command. Just
   start doing it:
   - Nothing done: start the interview in `intake.md`. Ask for a resume first, since it
     halves everything after.
   - Intake done, no voice: ask for two things they wrote, per `voice.md`.
   - Voice done, no targets: research the list, per `targets.md`.
   - Targets set, no application files: ask them to paste the real form text for the
     nearest deadline, per `extract.md`.
   - Questions extracted: ask the blocking questions, per `gaps.md`.
   - Gaps answered: draft it, per `draft.md`.
   - Drafts exist: run the checks and report what you found.

Ask the first question of whichever of those applies, in the same message. Do not stop
and wait for them to tell you to begin.

Two things to mention once, briefly, and only if they apply:

- **If anything on their list needs recommenders**, say that the letter clock is already
  running and `/recommenders` comes before drafting. This is the most common way a
  finished application still fails.
- **If any org bans AI in recruitment**, tell them to say so now and you will not write
  anything they submit for that one.
