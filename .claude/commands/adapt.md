---
description: Turn one org's finished answer into another org's answer without it reading recycled
argument-hint: [source org] to [target org]
---

Adapt from the source org to the target org named in $1. If they only named one
org, read `TARGETS.md`, find its cluster, and use the cluster's already-written org
as the source. Say which one you picked.

This is the command that makes eight applications cost the time of three. It is also
the command most likely to produce something that reads recycled, so the whole job is
the re-angling, not the copying.

## Before touching a sentence

Read both `applications/` files side by side and answer three questions in writing:

1. **What are the two unasked questions different?** Two orgs can ask a nearly
   identical prompt and be deciding opposite things. A consulting org asking why you
   care about a social issue is deciding whether you last until week nine. A service
   org asking the same thing is deciding whether you are a resume-builder. Same story,
   different half of it.
2. **What is different about who applies here?** The reader's worry changes what your
   answer has to disarm.
3. **What does the target org worry about that the source org did not?**

If the two unasked questions turn out to be the same, say so. Then the adaptation is
mostly a word-limit and specificity job, and it is fast.

## Then adapt in this order

1. **The specific detail.** Every name of the source org, every reference to their
   project, their meeting, their alum. This is where recycled answers get caught, and
   it is a free loss. Grep for the source org's name across the new draft before you
   finish.
2. **The opening sentence.** Rewrite it. The opening is tuned to one reader, and it is
   the sentence carrying the most weight. Reusing it unchanged across a cluster is how
   four answers end up with the same shape.
3. **The middle.** Usually survives. The mechanism of what you did does not change.
4. **The ask.** What you want to learn and what you will do for them. This has to be
   different or the "why us" answer is not a "why us" answer.
5. **The limit.** Run `tools/count.sh drafts/<Target>.md` and hit 90 to 100 percent of
   the new limit, which is almost never the old one.

## The check that matters

Read the finished answer and ask: **could this be pasted back into the source org's
form unchanged?** If yes, you adapted the word count and nothing else. Go back to step
1.

Then read both answers in a row, the way nobody but you ever will, and confirm they do
not open the same way. Two openings with the same move is the tell.

## Report

Which org you adapted from, what the two unasked questions turned out to be, what you
changed and why, the new count against the new limit, and one line on whether this
answer is now weaker than the original. Sometimes it is. Say so rather than hiding it,
because the fix is usually a different story for the target org, and it is cheaper to
learn that now than after `/reader`.
