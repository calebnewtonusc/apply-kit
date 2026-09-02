# AI policy, per club

Some clubs ban AI in recruitment. They say so in the application, usually in small
text near the top or in an honor-code checkbox. Ignoring that is a bad trade: the
downside is being removed from the process, and the upside is one essay you could
have written yourself.

## The three settings

Every file in `applications/` carries one of these in its `AI policy:` field.

**`allowed`** or **`unstated`.** Draft normally. Most clubs are here. An application
that says nothing about AI is not a ban, and every applicant in the pile is using
something.

**`disclosed`.** The club asks you to say whether you used AI and how. Draft normally,
then write the disclosure honestly and specifically: "I used Claude to interview me
about my own experience and to cut a 340-word answer to 250. The claims and the
opinions are mine." Vague disclosure reads worse than the tool did.

**`banned`.** The agent does not write anything you submit. It still does all of this:

- Interviews you until you know what you actually think
- Argues the weak side of your argument back at you
- Points out that your third paragraph is where your essay actually starts
- Tells you your answer is 90 words over
- Runs mock interviews and asks the follow-up you are dreading
- Reads your draft and tells you what a stranger will notice

That is most of the value, and none of it is a sentence you did not write.

## Setting it

Tell the agent: `Troy Camp bans AI.` It updates the file and will not draft that one.
If you are unsure what a club's policy is, the agent will ask you to check the form
before it drafts. It does not guess.

## The line the kit holds

Using a tool to find out what you think is not cheating. Submitting sentences you did
not write, to a club that told you not to, is. The kit is built so the first is easy
and the second takes a deliberate decision on your part.
