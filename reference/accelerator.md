# Accelerators, incubators, and pitch competitions

Startup accelerators, university incubators, venture fellowships, pitch and business
plan competitions, founder programs.

## Who reads it

A partner or program lead, fast, in volume, looking for a reason to take a call. Then a
panel or interview where the decision actually gets made.

The distinguishing feature: **they are underwriting the team more than the idea.**
Ideas change during the program and everyone in the room knows it. The application is
evidence about whether these specific people move quickly, know their market, and are
honest about what is not working.

## The artifacts

- A short written application, often with hard character limits, sometimes brutally
  short
- A video, frequently 60 to 120 seconds, sometimes required to be unedited and
  unscripted
- Traction numbers, however small
- Sometimes a deck, sometimes explicitly not wanted at the application stage
- An interview or a pitch, usually the deciding round

## Short answers are the test

Character limits here are shorter than any other type, and that is deliberate. They
are checking whether you can say what you do in one sentence. An answer that needs a
paragraph of setup to make sense reads as a founder who has not gotten to clarity yet.

Write the one-sentence version, then check whether a stranger could repeat it back.

## Traction beats projection

A real number, however small, beats any forecast. Forty users you talked to beats a
model showing a million. The most common failure is a market-size slide where evidence
should be.

If there is no traction yet, say what you have actually done: conversations, a
prototype, a waitlist, a pilot. Name the count. **Never invent the number.** These
readers ask for the underlying data more often than any other type, and a made-up
figure ends the process rather than the answer.

## What is usually unasked

| Stated                        | Usually deciding                                                |
| ----------------------------- | ----------------------------------------------------------------|
| What are you building         | Can you say it in one sentence                                  |
| Why you                       | Why is this team unfair to compete with, specifically           |
| Your market                   | Do you know your customer, or did you read a report about them  |
| Your traction                 | Is there evidence anyone wants this                             |
| What is your biggest risk     | Are you honest about the thing that could kill it               |
| Why now                       | What changed recently that makes this possible                  |

The risk question is where most applications fall down. Naming a real risk plainly is
read as maturity. Naming a fake risk, or saying execution, is read as someone who has
not thought about it.

## The video

Often the most-watched artifact and the least prepared. What works: talk to the camera,
say what you are building in the first ten seconds, show the thing if it exists, do not
read a script. Over-produced video reads worse than a plain one here, and some programs
say so explicitly.

## Format traps

- Character limits including spaces, enforced silently
- Video length limits enforced by the upload
- A deck link that is not viewable without requesting access
- Founder equity, incorporation, and team commitment questions answered inconsistently
  across the form

## Timeline

Batch deadlines, hard, with fast turnaround after. Some programs run rolling admissions
where early applications genuinely do better. Interviews are scheduled quickly and
often within days.

## The interview

Fast, interruptive, and comfortable with being adversarial. They will push on the
weakest part of what you wrote. The correct response to "why would that not work" is a
real answer or an honest "I do not know yet, here is how I would find out," never a
deflection. Practice being interrupted, because a rehearsed pitch delivered over an
interruption is the most common way this round goes badly.

## Lead with the end state, then earn it

YC and speedrun fund companies that could get very large, so a pre-traction app that
only describes its wedge reads small. The first sentence of the one-liner, the
description and "what are you building" states the end state. The second sentence
states what is built. Then show the route as numbered steps, each earned by the one
before it, with every unbuilt step labeled as the plan.

On 2026-10-28 the Anchored drafts led with "church follow-up by text" and the founder
sent them back: "YC and a16z invest in billion dollar ideas! You need to sell them on
the route to an OS ecosystem that every christian on earth will use on all their
devices." The fix kept traction honest (zero users, test data) while the vision led.

Never do:

- Lead with the wedge alone on a venture app when the founder has a bigger end state.
- Size the market with a population count alone. Use sourced counts, a price or fee
  marked `[NEED]` until set, and name the source and year of each number.
- Write a later route step as if it exists. Built means the repo shows it.
- Answer "why us" without naming the incumbents and what each one misses, with sourced
  facts (customer counts, exits).

## Rewriting a Google Doc draft whole

The Drive connector's update_file changes metadata only, never content. To replace a
Doc's text with a new markdown draft, upload over it:
`gws drive files update --params '{"fileId":"<id>"}' --upload draft.md --upload-content-type text/markdown`,
then `chewbacca google read <id>` and grep for the new lines and the absence of the old
ones (2026-10-28, Anchored drafts Doc).
