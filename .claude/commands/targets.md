---
description: Build and research the org list
---

Load `application-types` first.

Take the list from the applicant. It can mix types: clubs and internships in the same
month is normal. If they have not given one, ask for it. **Do
not build a list for them and do not argue with the one they give you.** They know
what they want to be in. Your job is research, not selection.

## For each one, set the type first

`student-org`, `job`, `fellowship`, `grad-school`, `grant`, or `accelerator`. It
decides which `reference/` file gets read before anything is written, so it is not
decoration. If a listing is genuinely ambiguous, ask once, in one line, and move on.
The common ambiguous cases are resolved in the `application-types` skill.

## Then verify against a live source

Load `org-research`. Search for the org's actual site, posting, program page, or
profile. Record only what you can source, with the source and the date, and say plainly
when you could not verify something. **Never invent a fact about an org.**

- Full correct name and spelling. Check this carefully. Misspelling an org's name on
  its own form is a cheap loss, and the wrong spelling is sometimes a real word.
- What they actually do, in one sentence, from their own material.
- Application deadline, or "not published" if you cannot find it.
- Info sessions and rush events with dates and locations.
- Meeting day and time, and whether attendance is mandatory.
- Admit rate if they publish one. Label it as an admit rate, not a verdict.
- Whether it is the type it looks like. Things on a list routinely turn out to be
  incubators, fellowships, or paid roles with different requirements and cycles.
- **Whether it needs recommenders**, and if so, their real deadline, which is earlier
  than the applicant's. This is the single most common way a finished application still
  fails, and it goes into `DEADLINES.md` immediately.
- Any published rubric or funding priorities. Where one exists it outranks every general
  instinct in this repo, and it gets copied into the org's file verbatim.

## Then produce three things

**`TARGETS.md`**, grouped into **essay clusters**: orgs whose prompts are similar
enough that one strong core answer adapts across all of them. This is what makes eight
applications take the time of three. Name each cluster and say which org to write
first in each, because that one becomes the source the rest adapt from.

**A conflicts section.** Cross-check meeting times. If several orgs hold mandatory
meetings in the same block, say so directly: they can accept exactly one, and they
will be asked in an interview which they would pick. This is the most useful thing
this command produces and it is invisible until someone checks.

**`DEADLINES.md`**, ordered by date, with what is due each day and every date marked
verified or unverified. Say which day carries the most and how many days away it is.

## Flag, once each, then drop it

- Any org whose stated focus conflicts with something they told you in intake. Say it
  in one sentence, take their answer, and move on.
- Anything on the list that turns out to be a different type than assumed.
- Any org they were rejected from before, since that changes what one prompt is
  really asking.

Then point them at `/extract`, one at a time, starting with the earliest deadline. If
anything needs recommenders, point at `/recommenders` first instead, because that clock
is already running.
