# Club Apps Kit

A working setup for doing club applications with a coding agent instead of a blank Google Doc.

You point it at the clubs you want. It interviews you, pulls the real questions off
each application, tells you exactly what it needs from you and nothing more, drafts
in your voice, then reads the whole packet back to you as the person who actually
receives it.

**It never invents anything about you.** Every fact in a draft either came out of your
mouth or is marked `[NEED: ...]` until you fill it in.

## Setup, about ten minutes

1. **Install Claude Code.** [claude.com/product/claude-code](https://claude.com/product/claude-code).
   Sign in with a Claude account, free tier works to start.
2. **Download this repo.** Green "Code" button, then "Download ZIP", then unzip it
   somewhere you will find again. Desktop is fine.
3. **Open your terminal** (Mac: Cmd+Space, type Terminal). Type `cd `, then drag the
   unzipped folder onto the terminal window, then hit enter.
4. Type `claude` and hit enter.
5. Type `/start` and hit enter.

That last command explains the whole thing and tells you what to do first. You do not
need to read the rest of this file.

## What the commands do

Type these inside Claude Code. Order matters for the first four.

| Command      | What happens                                                                 |
| ------------ | ---------------------------------------------------------------------------- |
| `/start`     | Orients you, checks what is done, tells you the single next thing            |
| `/intake`    | Interviews you about your life. Builds your story bank. Do this first        |
| `/voice`     | Reads writing you have already done so drafts sound like you, not like an AI |
| `/targets`   | Builds and researches your club list                                         |
| `/extract`   | Pulls the real questions off one club's application into a file              |
| `/unasked`   | Writes the question each prompt is really asking, under the one it states    |
| `/gaps`      | Asks only the questions that are actually blocking a draft                   |
| `/picks`     | Gives you multiple choice built from your own material. Answer with letters  |
| `/draft`     | Writes one club's answers                                                    |
| `/truth`     | Checks every factual claim against what you actually told it                 |
| `/slop`      | Finds the sentences that read as AI-written or as generic filler             |
| `/reader`    | Reads your packet as the tired human scoring it at 11pm                      |
| `/rank`      | Ranks every answer best to worst so you know where the last hour goes        |
| `/cut`       | Gets an answer under its word limit without gutting it                       |
| `/resume`    | Scans your resume against every club's format rules and your own drafts      |
| `/proven`    | Saves answers that already worked, and breaks down why they worked           |
| `/interview` | Runs mock interviews with real follow-ups                                    |
| `/status`    | What is drafted, what is blocked, what is due                                |
| `/submit`    | Final check before you paste an application in                               |

## The part that makes it work

Most people use AI on applications by pasting a question and taking what comes back.
That produces answers that are grammatical, on-topic, and completely interchangeable
with 200 others.

This kit does the opposite. It spends most of its effort **getting material out of you**
and almost none of it generating from nothing. `/intake` and `/picks` exist because the
bottleneck was never writing. It was that nobody ever asked you the right question about
your own life.

Two commands do most of the work.

`/picks` hands you multiple choice built from things you already said, and you answer
with letters. Four minutes, and it is the difference between a real answer and a
generic one.

`/unasked` writes, under every prompt, the question that prompt is really asking. A
club asks "tell us about a time you worked on a team" and is deciding whether you can
be told you are wrong. Applications ask ten things and score two. Knowing which two
usually changes which story you tell, not just how you tell it.

## Clubs that ban AI

Some do, explicitly, in the application. Tell the agent and it switches modes: it will
interview you, argue with your thinking, and quiz you for the interview, but it will not
write a sentence you submit. That is in [AI-POLICY.md](AI-POLICY.md) and the agent
checks it before drafting anything.

## Where things live

```
you/            Everything about you. Profile, story bank, voice, uploads
applications/   One file per club: their real questions, unasked questions, format rules
drafts/         Your answers, one file per club
review/         Output of /truth, /slop, /reader, /rank, /resume, /interview
examples/       One filled-in club file so you can see what good looks like
TARGETS.md      The club list
DEADLINES.md    Dates
```

Your material stays on your computer. Nothing gets pushed anywhere unless you push it.

---

All glory to God! ✝️❤️
