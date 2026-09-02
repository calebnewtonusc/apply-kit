# Apply Kit

A working setup for doing applications with a coding agent instead of a blank Google
Doc.

Clubs, jobs and internships, fellowships and scholarships, grad school, grants,
accelerators. You point it at what you are applying to. It interviews you, pulls the
real questions off each application, tells you exactly what it needs from you and
nothing more, drafts in your voice, then reads the whole packet back to you as the
person who actually receives it.

**It never invents anything.** Not about you, and not about the org you are applying
to. Every fact in a draft either came out of your mouth or is marked `[NEED: ...]`
until you fill it in. Every claim about the org carries a source and the date it was
checked.

## Setup, about ten minutes

1. **Install Claude Code.** [claude.com/product/claude-code](https://claude.com/product/claude-code).
   Sign in with a Claude account, free tier works to start.
2. **Download this repo.** Green "Code" button, then "Download ZIP", then unzip it
   somewhere you will find again. Desktop is fine.
3. **Open your terminal.** Mac: Cmd+Space, type Terminal. Windows: install
   [Git for Windows](https://gitforwindows.org) and open Git Bash, which the word
   counter needs.
4. Type `cd `, then drag the unzipped folder onto the terminal window, then hit enter.
5. Type `claude` and hit enter.
6. Type `/start` and hit enter.

That last command explains the whole thing and tells you what to do first. You do not
need to read the rest of this file.

## The six kinds of application

The method is the same for all of them. The reader is not, so the kit keeps a separate
brief on each in [reference/](reference/) and reads the right one before it writes
anything.

| Type | Covers | What carries the application |
| ---- | ------ | ---------------------------- |
| `student-org` | Clubs, campus orgs, Greek life, student government | The essays |
| `job` | Jobs, internships, co-ops, apprenticeships | The resume |
| `fellowship` | Fellowships, scholarships, awards, funded programs | Essays plus letters |
| `grad-school` | Masters, PhD, REUs, research placements | Statement plus letters |
| `grant` | Research, project, nonprofit, arts, community funding | The plan |
| `accelerator` | Accelerators, incubators, pitch competitions | Traction plus team |

Advice tuned for a club officer at 11pm produces a bad grant application. The kit knows
the difference and will ask which one you mean if it cannot tell.

## The commands

Type these inside Claude Code. Order matters for the first four.

**Getting your material out of you**

| Command | What happens |
| ------- | ------------ |
| `/start` | Orients you, checks what is done, tells you the single next thing |
| `/intake` | Interviews you about your life. Builds your story bank. Do this first |
| `/voice` | Reads writing you have already done so drafts sound like you, not like an AI |
| `/gaps` | Asks only the questions that are actually blocking a draft |
| `/picks` | Gives you multiple choice built from your own material. Answer with letters |

**Working out what they actually want**

| Command | What happens |
| ------- | ------------ |
| `/targets` | Builds and researches your list, sets the type for each, finds the clusters |
| `/extract` | Pulls the real questions off one application into a file |
| `/unasked` | Writes the question each prompt is really asking, under the one it states |
| `/whyus` | Researches one org deeply enough to write something nobody else could |
| `/chat` | Preps you for talking to a member, then captures what you learned |

**Writing**

| Command | What happens |
| ------- | ------------ |
| `/draft` | Writes one org's answers |
| `/adapt` | Turns a finished answer into another org's without it reading recycled |
| `/cover` | Writes a cover letter that is not a prose version of your resume |
| `/expand` | Gets a short answer up to its limit without padding it |
| `/cut` | Gets a long answer under its limit without gutting it |

**Checking**

| Command | What happens |
| ------- | ------------ |
| `/truth` | Checks every factual claim against what you actually told it |
| `/slop` | Finds the sentences that read as AI-written or as generic filler |
| `/reader` | Reads your packet as the three people who actually receive it |
| `/rank` | Ranks every answer best to worst so you know where the last hour goes |
| `/resume` | Scans your resume against every org's rules and against your drafts |
| `/submit` | Final check before you send it |

**The parts that are not prose**

| Command | What happens |
| ------- | ------------ |
| `/recommenders` | Picks them, asks them well, tracks the dates that actually bind |
| `/materials` | Videos, portfolios, writing samples, take-homes, transcripts |

**Across time**

| Command | What happens |
| ------- | ------------ |
| `/plan` | Turns your deadlines into a dated work plan, working backward |
| `/status` | What is drafted, what is blocked, what is due |
| `/panic` | Deadline is close and it is not done. Triage, then move |
| `/interview` | Runs mock interviews with real follow-ups |
| `/reapply` | Handles applying somewhere that already said no |
| `/outcome` | Records what happened, so next cycle starts from evidence |
| `/proven` | Saves answers that already worked, and breaks down why |

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
with letters. Four minutes, and it is the difference between a real answer and a generic
one.

`/unasked` writes, under every prompt, the question that prompt is really asking. An org
asks "tell us about a time you worked on a team" and is deciding whether you can be told
you are wrong. Applications ask ten things and score two. Knowing which two usually
changes which story you tell, not just how you tell it.

## It counts for real

Word limits are the one thing an agent is genuinely bad at. `tools/count.sh` parses
every drafted answer, counts it against the limit written in its own heading, and
reports what is over, what is under 90 percent, how many `[NEED:]` markers are still
open, and where the em dashes are.

```
tools/count.sh                 every draft
tools/count.sh drafts/RISE.md  one file
```

Nothing in the kit reports a count it did not get from there.

## Orgs that ban AI

Some do, explicitly, in the application. It is most common with student orgs. Tell the
agent and it switches modes: it will interview you, argue with your thinking, and quiz
you for the interview, but it will not write a sentence you submit. That is in
[AI-POLICY.md](AI-POLICY.md) and the agent checks it before drafting anything.

## Where things live

```
you/            Everything about you. Profile, story bank, voice, chats, outcomes, uploads
applications/   One file per org: their real questions, unasked questions, format rules
drafts/         Your answers, one file per org
review/         Output of /truth, /slop, /reader, /rank, /resume, /interview
reference/      One brief per application type. The agent reads the one that applies
tools/          The word counter
examples/       Two filled-in org files, a student org and a job, to show the difference
TARGETS.md      The list
DEADLINES.md    Dates, including the ones that depend on other people
```

Your material stays on your computer. Nothing gets pushed anywhere unless you push it.
If you plan to make your own copy public, uncomment the `you/` line in `.gitignore`
first.

## Troubleshooting

**`tools/count.sh: permission denied`.** Run `chmod +x tools/count.sh` once.

**The counter finds no answers.** It reads headings shaped like `## Q1. The prompt (250
words)`. `/draft` writes them that way. If you wrote a draft by hand, match that shape.

**It asks me something I already told it.** Say so. That is a bug in how it read your
files, not something you should have to repeat. Point it at the file the answer is in.

**It wrote something that is not true about me.** Tell it. You were there and it was
not. It is built to correct the file and drop the claim rather than argue.

**A command says my draft is short but I like it.** It is one opinion from a machine
that has read your material. `/expand` will tell you when a short answer should stay
short.

---

All glory to God! ✝️❤️
