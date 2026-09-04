---
description: Final check before pasting an application in
argument-hint: [org name]
---

Run every check for **$1** and give a go or no-go. Be honest. A no-go the night before
is worth more than a reassuring yes.

Start with two mechanical checks. Both exit non-zero on a real problem and both catch
things you cannot catch by reading.

```
sh tools/count.sh drafts/<Org>.md
sh tools/stale.sh
```

`count.sh` fails when an answer is over its limit or a `[NEED:]` marker is still open.
Both are automatic no-gos.

`stale.sh` fails when a fact has not been confirmed in three weeks. **Do not wave this
one through.** It is the check that catches the true-when-written number, and it is the
last moment anybody looks at it before a stranger does. Run `/refresh` and get the
answer. If they are mid-submission and will not stop, say which specific facts are
going out unverified and let them decide with that in front of them.

Then read that type's file in `reference/` and check its format traps specifically.

## Checklist

**Content**

- [ ] Every question answered, including optional ones. Declining an optional
      invitation answers a question badly, especially when reapplying
- [ ] Zero `[NEED:]` markers remaining
- [ ] Every word limit met, and each answer at 90 to 100 percent of it, per
      `tools/count.sh` rather than per the counts written in the file
- [ ] No story told twice within this application
- [ ] Not every "why us" answer running the same shape
- [ ] Org name spelled exactly right, everywhere, including in the essays
- [ ] The "why us" answer names something specific to this org that would not work
      for another one

**Truth**

- [ ] Every number matches **Canonical numbers** in `you/PROFILE.md`
- [ ] `sh tools/stale.sh` clean, or every stale fact confirmed this session
- [ ] Anything describing the current term (course load, hours per week, current
      roles) confirmed since the term actually started
- [ ] Every claim on the resume matches every claim in the essays
- [ ] Dead-lines grep for this org run and clean
- [ ] Nothing crosses a boundary in `you/DISCLOSURE.md`

**Format**

- [ ] Correct file type. Almost always PDF
- [ ] The exact filename this org specifies, comma and underscore order included
- [ ] Page limit met if there is one
- [ ] Any link opened in a private window to confirm public access
- [ ] Video length and format if required

**Policy**

- [ ] AI policy checked. If `banned`, confirm every submitted sentence is theirs
- [ ] If `disclosed`, the disclosure is written and specific

**Logistics**

- [ ] Deadline and time zone confirmed against a live source
- [ ] Anything needing another person is done, not pending. Letters confirmed
      submitted, not confirmed promised
- [ ] Every non-prose artifact checked per `/materials`: video length, links opened in
      a private window, writing sample inside its page range
- [ ] Attendance conflicts known, and they have an answer for "which would you pick"

## Output

Go or no-go, then the blocking items as a numbered list with what to do about each.
Then the last read: the one sentence in this application you would change if there
were time, quoted.

Do not pad it with encouragement. They are about to hit submit.
