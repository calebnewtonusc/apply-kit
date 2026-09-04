---
description: Check every factual claim against what they actually told you
---

Load `honesty-guard`. Write `review/TRUTH.md`.

## 1. Unsourced claims

Go through every draft. For each factual claim, find where it came from:
`you/PROFILE.md`, `you/STORY-BANK.md`, an upload, or a direct answer.

Anything you cannot trace gets listed with the file, the quoted sentence, and a
question. If you wrote it and cannot source it, say so plainly. That is a mistake to
fix, not to explain.

## 2. Numbers that drift

Pull every number, title, and date from `you/PROFILE.md`, the resume in
`you/uploads/`, and every file in `drafts/`. Group by claim. Any claim with more than
one value goes in a table:

| Claim           | Profile | Resume | Drafts       |
| --------------- | ------- | ------ | ------------ |
| Org membership | 70+     | 90+    | 80+ (BTG Q1) |

Then ask which is defensible and what exactly it counts. Two different countings of
the same thing can both be true and are not the same claim. Once they choose, write it
into **Canonical numbers** in `you/PROFILE.md` and update every draft to match. Set
that row's `Checked` date to today, since they just confirmed it.

## 3. Claims that read bigger than the thing

Flag, with reasoning, for them to decide:

- A plan written in the past tense
- A round accuracy or success figure on a small sample
- A multiplier with no baseline
- A title whose scope has changed
- A skill listed that they would not want to be quizzed on

Say each once. **They know their own work better than any file here.** If they say a
claim is accurate, it is accurate: update `you/PROFILE.md` to match and drop it.

## 4. Dead lines

Grep every draft for the phrases listed as dead in `you/STORY-BANK.md` and in each
org file. Report hits with file and line.

## 5. Disclosure check

Read `you/DISCLOSURE.md`, then check every draft against it. Report any place a draft
crosses a boundary they set, including implied references that point at something they
said they did not want in.

## Report

Blocking items first, then decisions, then notes. End with the count of things that
must be resolved before anything can be submitted.
