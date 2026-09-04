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

## Setup, about five minutes

1. **Install Claude Code.** [claude.com/product/claude-code](https://claude.com/product/claude-code).
   Sign in with a Claude account, free tier works to start.
2. **Download this repo.** Green "Code" button, then "Download ZIP", then unzip it
   somewhere you will find again. Desktop is fine.
3. **Open your terminal.** Mac: Cmd+Space, type Terminal. Windows: install
   [Git for Windows](https://gitforwindows.org) and open Git Bash.
4. Type `cd `, then drag the unzipped folder onto the terminal window, then hit enter.
5. Type `claude` and hit enter.
6. **Tell it what you are applying to.**

That is the whole setup. Step 6 is a sentence in your own words:

> I need to apply to three clubs by Friday

> applying for data engineering internships, first deadline is in two weeks

> PhD applications, six programs, December 15

It takes it from there. It will ask you questions, one small batch at a time, and write
everything down as you go. **You never have to know what to ask for and you never have
to type a command.**

## You do not have to learn anything

The thing that makes application tools useless is that they hand you a blank box and
wait. This one asks you questions instead, and it asks them in an order that builds on
itself.

- **It asks, you answer.** Fragments are fine. One line is fine. "idk" is fine, and it
  will ask a better question.
- **When you get tired, it switches to multiple choice** built out of things you already
  said, and you answer with letters. Four minutes, and it produces a better answer than
  an hour of staring at a text box.
- **It remembers.** Close your laptop, come back in three days, and it picks up exactly
  where you were. You will never be asked the same thing twice.
- **It never waits for permission.** It does the work and tells you what it found.

There are commands under the hood if you ever want them, listed at the bottom. Most
people will never type one.

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

## The part that makes it work

Most people use AI on applications by pasting a question and taking what comes back.
That produces answers that are grammatical, on-topic, and completely interchangeable
with 200 others.

This kit does the opposite. It spends most of its effort **getting material out of you**
and almost none of it generating from nothing. The bottleneck was never writing. It was
that nobody ever asked you the right question about your own life.

Two things do most of the work, and both happen without you asking for them.

**It hands you multiple choice** built from things you already said, and you answer with
letters. Four minutes, and it is the difference between a real answer and a generic one.
This is what it does the moment your answers get short, which is exactly when a blank
text box would have beaten you.

**It writes the question under the question.** An org asks "tell us about a time you
worked on a team" and is deciding whether you can be told you are wrong. Applications
ask ten things and score two. Knowing which two usually changes which story you tell,
not just how you tell it.

## It counts for real

Word limits are the one thing an agent is genuinely bad at. `tools/count.sh` parses
every drafted answer, counts it against the limit written in its own heading, and
reports what is over, what is under 90 percent, how many `[NEED:]` markers are still
open, and where the em dashes are.

It runs on its own and fixes the lengths before you ever see a draft. If you want it
yourself:

```
sh tools/count.sh                 every draft
sh tools/count.sh drafts/RISE.md  one file
```

Nothing in the kit reports a count it did not get from there.

## It notices when a fact goes out of date

This is the mistake that actually gets people, and almost nothing is built to catch it.

You tell it in week one that you are taking eighteen units. You drop a class at
add/drop. Six weeks later four applications say eighteen units. Nobody lied, nothing was
invented, and every check passes, because the number was true when it was written. Then
an interviewer asks what you are taking this term and your answer does not match the
form you sent.

So every fact about you carries the date it was last confirmed, and the kit reads them
back before a submission:

```
sh tools/stale.sh      anything unconfirmed for three weeks
sh tools/stale.sh 45   a different window
```

You get one short message with the four or five things worth re-checking, you answer in
a line, and it fixes the value everywhere it already appears rather than just in one
file. It will not ask about anything it confirmed recently, and it will not do this on
your first day, when nothing has had time to change.

The things that move: GPA, graduation date, course load, hours per week, and whether a
role you listed is still active. Every application asks about at least three of those.

## Orgs that ban AI

Some do, explicitly, in the application. It is most common with student orgs. Tell the
agent and it switches modes: it will interview you, argue with your thinking, and quiz
you for the interview, but it will not write a sentence you submit. That is in
[AI-POLICY.md](AI-POLICY.md) and the agent checks it before drafting anything.

## Where things live

```
PROGRESS.md     Where you are. Claude keeps it current so you can close the laptop
you/            Everything about you. Profile, story bank, voice, chats, outcomes, uploads
applications/   One file per org: their real questions, unasked questions, format rules
drafts/         Your answers, one file per org
review/         What the checking passes found
reference/      One brief per application type. The agent reads the one that applies
tools/          The word counter and the staleness checker
examples/       Two filled-in org files, a student org and a job, to show the difference
TARGETS.md      The list
DEADLINES.md    Dates, including the ones that depend on other people
```

Every one of these is a plain text file you can open and edit yourself. Nothing is
hidden in a database. If Claude writes something wrong about you, open the file and fix
it, and it will use your version.

Your material stays on your computer. Nothing gets pushed anywhere unless you push it.
If you plan to make your own copy public, uncomment the `you/` line in `.gitignore`
first.

## Troubleshooting

**`permission denied` on anything in `tools/`.** Run `chmod +x tools/*.sh` once. This
happens when you downloaded the ZIP instead of cloning, which strips the executable bit.
Running them as `sh tools/count.sh` works either way.

**It keeps asking me to confirm facts I already gave it.** It should only ask about
things unconfirmed for three weeks, and never about anything current. If it is asking
about something you just told it, the date did not get written down: say so, and tell it
to stamp the `Checked` column.

**The counter finds no answers.** It reads headings shaped like `## Q1. The prompt (250
words)`. Claude writes them that way. If you wrote a draft by hand, match that shape.

**It asks me something I already told it.** Say so. That is a bug in how it read your
files, not something you should have to repeat. Point it at the file the answer is in.

**It wrote something that is not true about me.** Tell it. You were there and it was
not. It is built to correct the file and drop the claim rather than argue.

**It says my draft is short but I like it.** It is one opinion from a machine that has
read your material. Say so and it will tell you when a short answer should stay short.

**It keeps asking me things instead of writing.** That is deliberate for the first
stretch, and it is where the quality comes from. If you are short on time, say how long
you actually have and it will cut straight to drafting and tell you what it skipped.

**I forgot where I was.** Just say "where am I." It reads `PROGRESS.md` and tells you.

## Appendix: the commands

**You do not need this section.** These are what the agent runs on its own as the
conversation moves. They are here for people who want to jump straight to a specific
step, and because seeing the list explains what the thing actually does.

**Getting your material out of you**

| Command | What happens |
| ------- | ------------ |
| `/start` | Says where you are and what happens next. You get this automatically anyway |
| `/intake` | Interviews you about your life. Builds your story bank. Do this first |
| `/voice` | Reads writing you have already done so drafts sound like you, not like an AI |
| `/gaps` | Asks only the questions that are actually blocking a draft |
| `/picks` | Gives you multiple choice built from your own material. Answer with letters |
| `/refresh` | Reads back the facts that have gone stale and confirms each is still true |

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

---

All glory to God! ✝️❤️
