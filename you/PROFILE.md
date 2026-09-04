# Profile

**Template. `/intake` fills this in. Do not write here by hand unless you want to.**

Every fact in every application comes from this file. If something here is wrong, the
applications are wrong.

## The dating rule

**Every fact here carries the date it was last confirmed.** Not the date it was true,
the date somebody checked.

This is not bookkeeping. A fact does not have to be false to sink an application, it
only has to have expired. A GPA moves. A role ends. A graduation date shifts. A course
load changes at add/drop, three weeks after you wrote it down and one week before you
submit. All of those were true when they were written, none of them would fail an
honesty check, and any of them will be the thing an interviewer asks about.

`tools/stale.sh` finds them. `/refresh` fixes them. Anything unchecked for more than
three weeks gets read back before a submission goes out.

## Basics

Each line ends with `(checked YYYY-MM-DD)`.

- Name:
- Year:
- School / program:
- Major, minor, and whether either is declared:
- Expected graduation:
- GPA, and whether it is confirmed on an official transcript:

## Roles and experience

One per row. Real dates. Present tense only if it is still true today.

| What | Role | Dates | Still active | Checked |
| ---- | ---- | ----- | ------------ | ------- |
|      |      |       |              |         |

## Canonical numbers

**The most important section in the repo.** Every number that appears anywhere: the
resume, an essay, an interview answer. One agreed value each, plus what it counts,
where it came from, and when it was last confirmed.

If a number appears here, it appears that way everywhere. No exceptions.

Two rules that matter more than they look:

- **"What it counts" is not optional.** Thirty members of what, counted how? You will
  be asked in an interview, and the answer has to be the same one you wrote down.
- **A number you cannot derive is a number you should not use.** If you cannot explain
  how it was calculated, it does not go in an application, because the follow-up
  question is exactly that.

| Claim | Value | What it counts | Source | Checked |
| ----- | ----- | -------------- | ------ | ------- |
|       |       |                |        |         |

## Skills

Only things you would be happy to be quizzed on. Some applications ask which technical
skill you want to be evaluated on, and anything listed is an invitation.

## Current commitments

Every application asks. Hours per week, honestly, including course load.

This is the single most perishable section in the file. It is written before a term
starts and it is usually wrong by week three.

| Commitment | Hours / week | Checked |
| ---------- | ------------ | ------- |
|            |              |         |

## What you want to learn

Specific. "Unit economics and market sizing" is usable. "Business skills" is not.

## What you would bring

The thing you can do that most applicants to these orgs cannot.

<!-- TEMPLATE: unfilled. Delete this line the moment you write real content here. -->
