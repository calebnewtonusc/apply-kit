#!/bin/sh
# Count every drafted answer against the limit in its own heading.
#
# The agent cannot count words reliably. This can. Everything in this kit that
# depends on an exact count runs through here: /draft, /cut, /expand, /status,
# /submit.
#
# Usage:
#   tools/count.sh                 every file in drafts/
#   tools/count.sh drafts/RISE.md  one file
#
# Reads headings shaped like:
#   ## Q1. Why do you want to join? (250 words)
#   ## Q4. Tell us about yourself (500 characters)
#
# The answer is everything between that heading and the first line starting
# with **Count:, **Story, **Needs, **123 words.**, ---, or the next ## heading.
#
# If any line in that span is a blockquote, the blockquote is treated as the
# answer and the surrounding prose as commentary. Both draft shapes work:
#
#   ## Q1. Why us? (200 words)        ## Q1. Why us? (200 words)
#   The answer text.                  > The answer text.
#   **Count:** 000 / 200              **185 words.** Notes about it.
#
# Exit 1 if anything is over its limit or still has a [NEED:] marker, so it
# can be used as a submission gate.

set -e

TARGET="${1:-drafts}"

if [ -d "$TARGET" ]; then
  FILES=$(find "$TARGET" -name '*.md' ! -name '_TEMPLATE.md' | sort)
else
  FILES="$TARGET"
fi

if [ -z "$FILES" ]; then
  echo "No draft files found in $TARGET."
  exit 0
fi

# shellcheck disable=SC2086
awk '
function trim(s) { gsub(/^[ \t\r\n]+|[ \t\r\n]+$/, "", s); return s }

function words(s,   n, a) {
  s = trim(s)
  if (s == "") return 0
  n = split(s, a, /[ \t\r\n]+/)
  return n
}

function chars(s) {
  gsub(/[ \t\r\n]+/, " ", s)
  return length(trim(s))
}

function quoted(s,   i, n, a, out, line) {
  # If any line is a blockquote, the blockquote is the answer and everything
  # else in the section is commentary written by the agent. Counting that prose
  # is how a 185-word answer gets reported as 252 and then wrongly cut.
  n = split(s, a, /\n/)
  out = ""
  for (i = 1; i <= n; i++) {
    line = a[i]
    if (line ~ /^[ \t]*>/) {
      sub(/^[ \t]*>[ ]?/, "", line)
      out = out "\n" line
    }
  }
  return out
}

function finish(   body, n, pct, flag, i, w, lower, tok, q) {
  if (!inq) return
  body = buf
  q = quoted(body)
  if (trim(q) != "") body = q
  needs_here = gsub(/\[NEED:[^]]*\]/, "X", body)
  total_needs += needs_here
  gsub(/\*\*/, "", body)

  if (trim(body) == "") { inq = 0; buf = ""; return }

  answers++
  if (unit == "chars") n = chars(body); else n = words(body)

  flag = "ok"
  if (limit > 0) {
    pct = n * 100 / limit
    if (n > limit)          { flag = "OVER";  over++;  }
    else if (pct < 90)      { flag = "short"; short++; }
    printf "  %-6s %5d / %-5d %-6s  %3d%%  %s\n", qid, n, limit, unit, pct, flag
  } else {
    printf "  %-6s %5d %-13s        no stated limit\n", qid, n, unit
  }

  if (needs_here > 0) printf "         %d [NEED:] marker(s) still open\n", needs_here

  # tics that are binary enough to check mechanically
  if (index(body, "\xe2\x80\x94") > 0) { printf "         em dash present\n"; tics++ }
  lower = tolower(body)
  gsub(/[^a-z -]/, " ", lower)
  n = split(lower, w, /[ ]+/)
  for (i = 1; i <= n; i++) {
    tok = w[i]
    if (tok in banned) { printf "         banned word: %s\n", tok; tics++ }
  }

  inq = 0; buf = ""
}

BEGIN {
  split("delve delves delved delving foster fostered fostering leverage leveraged leveraging utilize utilized utilizes utilizing facilitate facilitated facilitating empower empowered empowering streamline streamlined streamlining robust seamless seamlessly transformative elevate elevated elevating harness harnessed meticulous meticulously intricate realm tapestry myriad testament invaluable pivotal", b, " ")
  for (i in b) banned[b[i]] = 1
  print ""
}

FNR == 1 {
  finish()
  file = FILENAME
  sub(/^.*\//, "", file)
  printf "%s\n", file
  files++
}

/^## *[Qq][0-9]+[.:) ]/ {
  finish()
  head = $0
  qid = head
  sub(/^## */, "", qid)
  sub(/[.:) ].*$/, "", qid)
  limit = 0
  unit = "words"
  if (match(head, /[0-9]+ *(words?|characters?|chars?)/)) {
    spec = substr(head, RSTART, RLENGTH)
    limit = spec + 0
    if (spec ~ /char/) unit = "chars"
  }
  inq = 1
  buf = ""
  next
}

/^\*\*(Count|Story|Needs)/                     { finish(); next }
/^\*\*[0-9]+ *(words?|characters?|chars?)[.,]?\*\*/ { finish(); next }
/^---[ \t]*$/             { finish(); next }
/^## /                    { finish(); next }

inq { buf = buf "\n" $0 }

END {
  finish()
  printf "\n%d file(s), %d answer(s). ", files, answers
  printf "%d over limit, %d under 90%%, %d [NEED:] open, %d mechanical tic(s).\n", over+0, short+0, total_needs+0, tics+0
  if (over > 0 || total_needs > 0) {
    print "Blocking: an answer is over its limit or a fact is still missing."
    exit 1
  }
  print ""
}
' $FILES
