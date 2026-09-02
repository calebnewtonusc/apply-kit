---
name: application-types
description: Route to the right reference file for the kind of application being written, since the reader, the artifacts, and the traps differ by type. Use at the start of /targets, /extract, /draft, /resume, /interview, and any time the type of an application is unclear.
---

# What kind of application is this

The method in this kit is the same for every application: get real material out of the
person, find the question under the question, never invent a fact, and read the result
as the person who receives it.

**Who reads it and what they need is not the same.** A club officer at 11pm and a PhD
admissions committee are doing different jobs, and advice tuned for one produces a bad
application for the other. Every org file carries a `Type:` field for this reason.

## The six types

| Type           | Covers                                                            | Reference                  |
| -------------- | ----------------------------------------------------------------- | -------------------------- |
| `student-org`  | Clubs, campus orgs, Greek life, student government, service groups | `reference/student-org.md` |
| `job`          | Jobs, internships, co-ops, apprenticeships, contract work          | `reference/job.md`         |
| `fellowship`   | Fellowships, scholarships, awards, funded programs                 | `reference/fellowship.md`  |
| `grad-school`  | Masters, PhD, REUs, research placements, post-baccs                | `reference/grad-school.md` |
| `grant`        | Research, project, nonprofit, arts, and community funding          | `reference/grant.md`       |
| `accelerator`  | Accelerators, incubators, pitch and business plan competitions     | `reference/accelerator.md` |

**Read the matching reference file before extracting questions, before drafting, and
before interview prep.** Do not read all six. One, the one that applies.

## Setting the type

`/targets` sets it per org. If it is genuinely ambiguous, ask once, in one line, and
move on. When something sits between two types, pick the one whose reader is closer and
say which you picked.

The ambiguous cases and how they usually resolve:

- A paid campus role with an application: `job`.
- A student-run consulting group: `student-org`, even though the work resembles a job.
- A university program that funds a summer of research: `grad-school` if the output is
  research and the reader is faculty, `fellowship` if the reader is a committee scoring
  against published criteria.
- A startup competition run by a school: `accelerator`.
- A nonprofit asking for money to run a program: `grant`.

## What changes by type

| | student-org | job | fellowship | grad-school | grant | accelerator |
| --- | --- | --- | --- | --- | --- | --- |
| Carries the application | Essays | Resume | Essays plus letters | Statement plus letters | The plan | Traction plus team |
| Reader | Peer, will be your teammate | Filter, then hiring manager | Committee, published rubric | Faculty, possible advisor | Program officer, rubric | Partner, then panel |
| Time on it | 60 to 90 seconds | Under a minute, then longer | Long, multiple readers | Long | Long, checklist | Fast |
| Lead time | Days to weeks | Weeks to months | Months, letters bind | Months, letters bind | Weeks, partners bind | Batch deadline |
| Recommenders | Rare | Late, often after offer | Central | Decisive | Support letters, different thing | Rare |
| AI bans common | Yes | No | Sometimes | Sometimes | No | No |

## What does not change

Do not let type-specific advice override these. They hold everywhere.

- Never invent a fact about the applicant or about the org.
- The unasked question is what gets scored.
- Specific beats general: names, numbers, mechanisms.
- Every number matches every other document.
- Use 90 to 100 percent of any stated limit, counted with `tools/count.sh`.
- A sentence that could appear in another applicant's application unchanged is filler.

## Mixed cycles

Someone applying to clubs and internships in the same month is normal, and the clusters
in `TARGETS.md` should not cross types. A story adapts across two clubs easily. The
same story adapted from a club essay into a cover letter usually needs rebuilding,
because the reader changed from a future teammate to a hiring manager.

`/adapt` handles within-type adaptation well. Across types, say plainly that it is a
rewrite rather than an adaptation.
