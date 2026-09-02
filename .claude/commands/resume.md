---
description: Scan the resume against every org's requirements and against the drafts
---

Read the resume in `you/uploads/`. Load `application-types`. Write
`review/RESUME-SCAN.md`.

How much this matters depends entirely on type. For `job` the resume **is** the
application and this is the highest-value command in the kit. For `grad-school` it is a
CV, which is a different document: longer, with publications and presentations, and
cutting them to fit one page is a mistake. For `student-org` it is a supporting document
with fussy filename rules. Read the matching `reference/` file before scanning.

## The frame to open with

**Their resume is the interview's question bank.** Orgs interview off the page in
front of them, line by line, and the follow-up is always "walk me through that
number." Every figure on the page is a place an interview can go wrong. Say this first
so the rest of the scan makes sense.

## 0. For jobs, match the posting

Skip this section for other types. For `job`, read the posting next to the resume and
pull out its exact nouns: the tools, the frameworks, the methods, the domain words.
Where the applicant has done the thing, use the posting's word for it rather than a
synonym. A resume saying "data pipelines" against a posting saying "ETL" is a worse
match for both the parser and the human, for no good reason.

This is not a license to claim anything they have not done. Report every term in the
posting the resume does not cover, and ask which ones are real. The ones that are not
stay off.

Then check the mechanics that break parsers: multi-column layouts, tables, text inside
headers or footers, a PDF that is actually an image, and missing or unparseable dates.

## 1. Format, per org

Read every `applications/` file and build a table: which org needs which file type,
which exact filename, what page limit, and whether a link is required.

Filename conventions differ per org and often specify comma or underscore order.
Getting one wrong is a free loss. If an org says one page and the resume will not fit
at readable size, say so and name the specific lines to cut, in order.

If an org wants a link, remind them to open it in a private window. Orgs that warn
twice about link permissions do so because applicants keep failing it.

If the resume is not a PDF, that is blocking. Say it first.

## 2. Numbers against every other document

Compare every claim on the resume to `you/PROFILE.md` and to each file in `drafts/`.
Any claim with more than one value goes in a table with all its versions and sources.

Escalating numbers across documents are the pattern to catch, not any individual
figure. Ask which version is defensible and what exactly it counts.

## 3. Claims to defend

For each number and title, ask whether they could answer "how did you get that" in
ninety seconds. Flag anything that cannot be, especially:

- Plans written in the past tense
- Round success figures on small samples
- Multipliers with no baseline
- Titles whose scope has changed
- Listed skills they would not want quizzed, when an org asks which skill to evaluate

## 4. Verify the checkable

Search for anything institutionally verifiable: degree program names, official titles,
organization names. A degree name that does not match the school's own catalogue is a
credibility problem before anyone reads a bullet, especially at orgs whose members
attend the same school.

## 5. What is strong

Name the most credible line on the page and say whether it is buried. Name the best
line for each org cluster. If there is a genuinely human "interests" line, tell them
not to cut it for space. That line is what gets them asked about something they enjoy.

## Then

Update `you/PROFILE.md` with anything the resume records that the repo did not have,
and say what you changed. **If they say a claim is accurate, it is accurate.** Correct
the repo and drop it.
