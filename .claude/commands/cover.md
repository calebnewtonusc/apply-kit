---
description: Write a cover letter that is not a prose version of the resume
argument-hint: [org name]
---

Draft the cover letter for **$1** into `drafts/<Org> - cover letter.md`. Read
`reference/job.md` first, plus the org's `applications/` file and the posting itself.

## Before writing, decide whether it is worth it

Cover letters are optional at many employers and unread at some. They earn their time
in three cases: a small org where a person will actually read it, a career change or
non-obvious background that the resume alone reads oddly, and a role where writing is
part of the job.

If none of those hold and the resume is not yet matched to the posting, say so. An hour
on `/resume` beats an hour here, and that is an honest answer rather than a dodge.

## What it is for

The resume says what you did. The letter says **why those things add up to this job**,
which the resume cannot say because a resume has no argument in it.

So it is not a prose retelling of the bullets. Anything that just restates a line from
the resume is wasted, and the reader has both documents open.

## The shape

Four paragraphs, under 400 words, usually well under.

1. **What you are applying for and the one reason it is you.** Skip the throat-clearing.
   "I am writing to express my interest in" is the most skippable sentence in the genre.
   Open on the specific thing.
2. **The strongest piece of evidence, told as a mechanism.** One thing, in detail, with
   what you did and what happened. Not three things in summary. Pull it from
   `you/STORY-BANK.md` and pick for relevance to the posting rather than for impressiveness.
3. **Why this employer, specifically.** Same rule as everywhere: if it would work for a
   different company, it is not an answer. A product you actually use, a problem in
   their domain you have hit, something they published. Load `org-research` and source
   it. **Never invent a fact about the company.**
4. **A close that is not a plea.** What you would want to work on, or what you would
   bring to the specific thing the posting is about. One sentence. No "I look forward to
   the opportunity to further discuss how my skills."

## Use their words

Read the posting and use its vocabulary for the work you have actually done. Their word
for the tool, their word for the method, their word for the domain. This is not keyword
stuffing and it is not a license to claim anything you have not done. It is removing a
translation step the reader should not have to make.

## Rules that hold

- Address a person if you can find one, sourced. "Dear Hiring Team" is fine. "To Whom
  It May Concern" reads as a template.
- Never invent a fact about the applicant or the employer. `[NEED:]` as always.
- No paragraph about how impressive the company is. They know.
- Run `tools/count.sh` if the form states a limit, and load `no-slop-writing`. The
  portability test applies harder here than anywhere: a cover letter that could go to
  four employers is worth less than no cover letter.

## Report

The count, the one sentence you would keep if it had to be cut to a paragraph, and the
weakest claim in it. If the letter ended up restating the resume, say so and cut it back
to the paragraph that has an argument in it.
