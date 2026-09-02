# Targets

**`/targets` fills this in.** You supply the org list. The agent researches it and
does not argue with it.

## The list

| Org | Type | What they do | Deadline | Meeting | Admit rate | Verified |
| --- | ---- | ------------ | -------- | ------- | ---------- | -------- |
|     |      |              |          |         |            |          |

Type is one of `student-org`, `job`, `fellowship`, `grad-school`, `grant`,
`accelerator`. It decides which file in `reference/` the agent reads before writing
anything, so it is not decoration.

## Clusters

Orgs whose prompts are similar enough that one strong core answer adapts across all
of them. Write the first one in each cluster properly, then run `/adapt` for the rest.

**Clusters do not cross types.** A story adapts from one club essay to another easily.
The same story going from a club essay into a cover letter is a rewrite, because the
reader changed.

### Cluster 1: [name]

- Orgs:
- Write first:
- Why they group:

## Conflicts

Overlapping mandatory meeting times. You can accept exactly one out of each group, and
an interviewer will ask which you would pick, so have the honest answer ready.

| Time slot | Orgs | Mandatory |
| --------- | ----- | --------- |
|           |       |           |

## Not what they looked like

Things on the list that turn out to be a different type than assumed: an incubator
rather than a club, a fellowship rather than a job, a program with prerequisites and its
own cycle. Each needs its own plan and its own `reference/` brief.

## Flags

Anything worth one sentence and then dropping: an org whose stated focus sits oddly
against something you said, an org that rejected you before (which changes what one of
its prompts is really asking), an org whose recruitment could not be confirmed.

<!-- TEMPLATE: unfilled. Delete this line the moment you write real content here. -->
