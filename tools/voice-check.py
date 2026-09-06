#!/usr/bin/env python3
"""Check drafted answers for the tells that make writing read as not-yours.

count.sh checks word limits. Slop detectors check generic AI phrasing. Neither
checks the specific things a reader flags when a draft stops sounding like the
person who is supposedly writing it, so those end up getting checked by eye,
which is how the same note gets given four times.

Usage:
  tools/voice-check.py drafts/*.md
  tools/voice-check.py --verbose "drafts/SOMECLUB.md"

Reads the answer under each ## / ### heading, stopping at a **123 words.** line,
a --- rule, or the next heading. Exits 1 if anything scores HIGH.

FACT GUARD: put one regex per line in a file called .factguard next to your
drafts, for every claim you have checked and found false. Numbers and names
propagate across drafts faster than anyone re-checks them, and a false specific
is the single most expensive thing you can put in something going out under
your name. Lines starting with # are comments.
"""
import re, sys, statistics, glob

VERBOSE = "--verbose" in sys.argv
FILES = [a for a in sys.argv[1:] if not a.startswith("--")]

# Caleb named every one of these himself. Weight = how fast he catches it.
RULES = [
    ("x-not-y", 3, [
        r"\b(is|was|are|were|it's|its)\s+not\s+[^.!?]{3,60}?,\s*(it'?s|it is|they'?re|but)\b",
        r"\b(isn't|wasn't|aren't|weren't)\s+[^.!?]{3,60}?,?\s+(it'?s|it is|they'?re)\b",
        r"\bnot\s+(just|only|merely)\s+[^.!?]{3,50}?,\s*but\b",
        r"\bthe (question|point|problem|issue|thing) (isn't|is not)\b",
    ]),
    ("announced-turn", 3, [
        r"\bwhat changed (isn't|is not|wasn'?t)\b",
        r"\bthat'?s? when I (understood|realized|knew|learned)\b",
        r"\bwhat I (realized|learned) (was|is)\b",
        r"\bhere'?s the thing\b", r"\bthe truth is\b", r"\blet me be clear\b",
        r"\bwhat nobody tells you\b", r"\bmost people (get this wrong|think)\b",
        r"\bisn'?t on my resume\b", r"\bwhat I bring\b.{0,20}\bresume\b",
    ]),
    ("banned-word", 3, [
        r"\b(delve|foster|leverage|utiliz\w+|facilitat\w+|empower\w*|streamlin\w+|"
        r"robust|seamless|cutting-edge|game changer|paradigm shift|transformative|"
        r"elevat\w+|harness\w*|meticulous\w*|intricate|realm|tapestry|ever-evolving)\b",
    ]),
    ("em-dash", 3, [r"—", r"–", r"(?<=\w) - (?=\w)"]),
    ("empty-phrase", 2, [
        r"\bit'?s worth noting\b", r"\bat the end of the day\b",
        r"\bwhen it comes to\b", r"\bin today'?s world\b", r"\bthe reality is\b",
        r"\blet'?s dive in\b", r"\bfor obvious reasons\b", r"\bneedless to say\b",
        r"\bin conclusion\b", r"\bultimately,", r"\boverall,",
    ]),
    ("puffery", 2, [
        r"\ba testament to\b", r"\bunderscor\w+\b", r"\bpivotal moment\b",
        r"\bspeaks volumes\b", r"\bhighlight\w+ (the|my|his|her|their) commitment\b",
        r",\s*\w+ing (the|my|his|her|their|our) (team|commitment|importance|value)\b",
    ]),
    ("weasel-attribution", 2, [r"\bexperts agree\b", r"\bstudies show\b", r"\bresearch shows\b"]),
    # Claims you have checked and found false. Loaded from .factguard below.
    ("unverified-fact", 3, []),
    ("pre-defense", 2, [
        r"\bscales? down\b", r"\bI can still\b.{0,30}\bcommit\b",
        r"\bwon'?t (be a problem|affect)\b", r"\brest assured\b",
    ]),
]

def load_factguard():
    """Read .factguard from the working dir or any draft's directory."""
    import os
    seen, pats = set(), []
    dirs = ["."] + [os.path.dirname(f) or "." for f in FILES]
    for d in dict.fromkeys(dirs):
        for cand in (os.path.join(d, ".factguard"), os.path.join(d, "..", ".factguard")):
            cand = os.path.normpath(cand)
            if cand in seen or not os.path.exists(cand):
                continue
            seen.add(cand)
            for ln in open(cand, encoding="utf-8"):
                ln = ln.strip()
                if ln and not ln.startswith("#"):
                    pats.append(ln)
    return pats


for _name, _w, _pats in RULES:
    if _name == "unverified-fact":
        _pats.extend(load_factguard())

FORMAL = re.compile(r"\b(do not|does not|did not|cannot|can not|will not|would not|"
                    r"is not|are not|was not|were not|it is|I am|they are|that is|"
                    r"have not|has not|could not|should not)\b", re.I)
CONTRACTION = re.compile(r"\b\w+'(t|s|re|ve|ll|d|m)\b", re.I)


IS_PROMPT = re.compile(
    r"^(Q\d|Why|What|How|Tell us|Describe|Please describe|Your life|You'?re teaching"
    r"|If someone|Optional)|\(\d+\s*(words?|characters?)|\?", re.I)


def is_prompt(head):
    """Only lint real prompts. My own editorial headings are not answers."""
    skip = ("before you submit", "for the interview", "what changed", "standard fields",
            "what i changed", "rebuilt", "prompt clauses, counted", "two things to check",
            "before you send", "one decision", "notes", "and why",
            "prompt clauses", "resume upload", "logistics", "short fields", "delivery",
            "one decision", "if the form", "script", "material", "how to work")
    h = head.lower()
    if any(s in h for s in skip):
        return False
    return bool(IS_PROMPT.search(head))


def answers(text):
    """Yield (heading, body) for each ## or ### prompt heading."""
    parts = re.split(r"\n#{2,3} ", "\n" + text)
    for p in parts[1:]:
        lines = p.split("\n")
        head, rest = lines[0].strip(), []
        for ln in lines[1:]:
            if re.match(r"^\*\*\d+ words?\.?\*\*", ln) or ln.strip() == "---":
                break
            rest.append(ln)
        body = "\n".join(rest)
        # strip blockquote markers, file paths, and bold editorial notes
        body = re.sub(r"^> ?", "", body, flags=re.M)
        body = re.sub(r"^`[^`]*`\s*$", "", body, flags=re.M)
        body = re.sub(r"^\*\*(Cut per|Rebuilt|Corrected|Fixed|Note|I pulled|One decision)[^\n]*", "", body, flags=re.M)
        if body.strip() and is_prompt(head):
            yield head, body.strip()


def prompt_clauses(head):
    """A prompt with three verbs is three questions. Count the asks."""
    h = re.sub(r"\(\d+\s*(words?|characters?)[^)]*\)", "", head, flags=re.I)
    n = len(re.findall(r"\?", h))
    n += len(re.findall(r"\b(and|then)\s+(what|how|why|who|when|describe|tell|explain)\b", h, re.I))
    n += len(re.findall(r"\bhow (has|have|did|do|will|would|are|is)\b", h, re.I))
    return max(n, 1)


def sentences(body):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", body) if s.strip()]


def check(path):
    text = open(path, encoding="utf-8").read()
    findings, worst = [], 0
    for head, body in answers(text):
        words = len(body.split())
        if words < 25:
            continue
        for name, weight, pats in RULES:
            for pat in pats:
                for m in re.finditer(pat, body, re.I):
                    frag = body[max(0, m.start() - 35):m.end() + 35].replace("\n", " ")
                    findings.append((weight, name, head[:44], frag.strip()))
                    worst = max(worst, weight)

        sents = sentences(body)
        lens = [len(s.split()) for s in sents]
        if len(lens) >= 4:
            sd = statistics.pstdev(lens)
            if sd < 4.0:
                findings.append((2, "flat-rhythm", head[:44],
                                 f"stdev {sd:.1f} over {len(lens)} sentences, mean {statistics.mean(lens):.0f}. "
                                 f"Real writing varies hard: mostly long, with a short one for the hit."))
                worst = max(worst, 2)
            # Stacked short sentences. One short line after a long one is a hit;
            # two or three in a row is the rhythm people mean by "punchy," and it
            # is the single most common note a writer gives back on a draft.
            runs, run = [], 0
            for n in lens:
                run = run + 1 if n <= 6 else 0
                runs.append(run)
            if max(runs) >= 2:
                worst_i = runs.index(max(runs))
                frag = " / ".join(sents[max(0, worst_i - max(runs) + 1):worst_i + 1])
                findings.append((3, "stacked-fragments", head[:44],
                                 f"{max(runs)} sentences of 6 words or fewer back to back: {frag[:90]}"))
                worst = 3

            if statistics.mean(lens) < 9:
                findings.append((3, "third-grader", head[:44],
                                 f"mean sentence {statistics.mean(lens):.0f} words. "
                                 'Uniformly short sentences read as flat and juvenile.'))
                worst = 3

        f, c = len(FORMAL.findall(body)), len(CONTRACTION.findall(body))
        if words > 70 and f >= 4 and f > c * 1.5:
            findings.append((3, "formal-voice", head[:44],
                             f"{c} contractions to {f} formal constructions. "
                             f"Most people write with far more contractions than this."))
            worst = 3

        # Portability: no proper noun and no number means anybody could have sent it.
        proper = re.findall(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-z]{2,}\b", body)
        nums = re.findall(r"\b\d|\b(one|two|three|four|five|six|ten|twenty|thirty|forty|fifty|hundred|thousand|million)\b", body, re.I)
        if words > 60 and len(proper) < 2 and not nums:
            findings.append((3, "anyone-could-say-this", head[:44],
                             "no named person, place, org or number in the whole answer. "
                             "If anyone else could submit this answer, it fails."))
            worst = 3

        # A closing aphorism: short final sentence with nothing concrete in it.
        if len(sents) >= 3:
            last = sents[-1]
            if (len(last.split()) <= 13 and not re.search(r"\d", last)
                    and len(re.findall(r"(?<!^)\b[A-Z][a-z]{2,}\b", last)) == 0
                    and not last.rstrip().endswith("?")):
                findings.append((1, "possible-kicker", head[:44], last))
                worst = max(worst, 1)

        cl = prompt_clauses(head)
        if cl > 1 and VERBOSE:
            findings.append((0, "clauses", head[:44],
                             f"{cl} asks in this prompt. Confirm each is answered."))

    return findings, worst


LABEL = {3: "HIGH", 2: "MED", 1: "LOW", 0: "INFO"}
overall = 0
for path in FILES:
    fs, worst = check(path)
    fs.sort(key=lambda x: -x[0])
    name = path.split("/")[-1]
    if not fs:
        print(f"\n  CLEAN  {name}")
        continue
    print(f"\n  {LABEL[worst]:5s}  {name}   ({len(fs)} finding(s))")
    for w, rule, head, frag in fs:
        if w == 0 and not VERBOSE:
            continue
        print(f"    [{LABEL[w]:4s}] {rule:22s} {head}")
        print(f"           {frag[:150]}")
    overall = max(overall, worst)

print()
sys.exit(1 if overall >= 3 else 0)
