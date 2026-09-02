---
name: org-research
description: Verify facts about the organization being applied to, and never invent one. Use during /targets, /whyus, /extract, and any time an application needs a specific detail about the reader's organization.
---

# Researching the org

The rule against inventing facts about the applicant has a twin that is easier to break
and just as expensive: **never invent a fact about the organization.**

A hallucinated project name, a made-up alum, a client they never had, a professor's
research described from the title alone. Every one of these goes into a "why us" answer
and gets caught by the one person in the room who was actually there. It is worse than
a generic answer, because generic reads as lazy and wrong reads as dishonest.

## The standard

Every fact you write into an `applications/` file carries a source and a date:

```markdown
- Runs four pro-bono projects a semester, one per team.
  Source: campusconsulting.example.edu/projects, checked 2026-09-02.
```

Anything you cannot source goes in a separate block:

```markdown
## Unverified, do not use

- Possibly partnered with the county food bank in 2025. Could not confirm. Ask a
  member, or drop it.
```

Never move something from the second block to the first because it is probably true.

## Where facts actually come from

In descending order of both reliability and value:

1. **The applicant's own contact with them.** An info session, a conversation with a
   member, a workshop they attended. Logged in `you/CHATS.md`. Unfakeable and nobody
   else has it.
2. **The org's own current material.** Their site, their application form, their
   handbook, their published rubric or funding priorities, a lab page, a job posting.
3. **Primary documents they produced.** A paper, an annual report, a case study, a
   product, a public deck.
4. **First-party posts.** Their LinkedIn, Instagram, or newsletter. Check the date.
5. **Third-party coverage.** Useful, and the place errors enter. Attribute it.

Anything you half-remember about an organization from training rather than from a
source you just read is not a fact. This is the specific failure mode to watch in
yourself, and it is strongest for well-known organizations, where a confident wrong
detail is most likely and most damaging.

## Things that go stale and get people caught

- Officers, leads, and advisors. People graduate and rotate every year.
- Whether a professor is taking students this cycle.
- Deadlines and cycles carried over from last year's calendar.
- Programs that ended. Naming a discontinued initiative as a reason you are applying
  is a bad look that a current member spots instantly.
- Funding priorities, which funders revise.

Anything with a person's name or a date on it needs a current source, not a
plausible one.

## Reading a published rubric

Fellowships, grants, and many student orgs publish what they score. When one exists,
it outranks every general instinct about application writing in this repo. Copy the
criteria verbatim into the org's file and map each prompt to the criterion it serves.

Most applicants skim the criteria once and never look again. Mapping answers to them
is close to free and almost nobody does it.

## When research comes up empty

Say so plainly rather than padding the file. Then name the two fastest fixes: attend
the thing on the date in `DEADLINES.md`, or message one member and run `/chat`. Thirty
minutes of either produces better material than any amount of searching, and it is the
only way to get a first-tier specific.

An honest "I could not verify anything specific about this org" is a useful finding. It
usually means the "why us" answer has to be built from what the applicant will do for
them rather than from what they already are.
