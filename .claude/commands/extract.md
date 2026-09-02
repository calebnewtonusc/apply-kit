---
description: Pull one org's real application questions into a file
argument-hint: [org name]
---

Build `applications/<Org Name>.md` for **$1** from `applications/_TEMPLATE.md`.

Set the `Type:` field first, then load `application-types` and read that type's file in
`reference/`. What counts as a question, an artifact, and a trap all depend on it.

## Get the real questions

In order of preference:

1. The applicant pastes the actual form text. Best source. Ask for it.
2. A screenshot or PDF of the form in `you/uploads/`.
3. The org's published application link, if it is public.

**Never invent or paraphrase a prompt.** A drafted answer to a question they did not
ask is worse than nothing. If you cannot get the real text, create the file with the
verified org info, mark the questions section `NOT YET AVAILABLE`, and tell them
exactly what to send.

Record each prompt **verbatim**, including its word or character limit and whether it
is required or optional.

## Then write the unasked question under every prompt

Load the `unasked-questions` skill and follow it. Two to four sentences per prompt, in
a quoted block, naming the decision the org is making. Do every prompt, including the
fun ones.

## Also fill in

**Format requirements**, copied exactly from the form: file type, the org's specific
filename convention, page limits, link-permission warnings, video length. These differ
per org and cost people applications.

**Every non-prose artifact** the form requires: video, portfolio, writing sample,
transcript, take-home, letters. List them with their exact specs and hand them to
`/materials`. These fail applications quietly and nobody writes back to say which one.

**AI policy.** Look for it in the form text. Set the field to `allowed`, `disclosed`,
`banned`, or `unstated`. If banned, put the org's exact wording in the file.

**Which stories to pull** from `you/STORY-BANK.md` for each prompt, and why.

**Dead lines**: a grep list of phrases from their bank that must not appear in this
application, so it can be checked before submitting.

## Finally

Update `applications/INDEX.md` and `DEADLINES.md`. If an unasked question you wrote
here now appears at four or more orgs, promote it to the shared list at the top of
INDEX.md instead of repeating the analysis.

Tell them the one prompt in this application that fits their material best, and the
one that will be hardest, and why.
