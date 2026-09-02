# EXAMPLE: Northline Robotics, Data Engineering Intern

**A filled-in example of a `job` file, so you can see how it differs from
[EXAMPLE-student-org.md](EXAMPLE-student-org.md), which is a `student-org`. The company
is made up. Your files go in `applications/`.**

The thing to notice: there are barely any essay prompts, the resume carries the
application, and most of the work is in the posting-match and the format traps.

---

**Verified 2026-09-02 against northline.example.com/careers/de-intern-2027.**

|                |                                                              |
| -------------- | ------------------------------------------------------------ |
| **Type**       | `job`                                                        |
| What they do   | Warehouse robotics, fleet telemetry, Series B                |
| Deadline       | Rolling, posting opened Aug 18. Early applications reviewed first |
| Meeting        | n/a                                                          |
| Info sessions  | Campus career fair, Sept 18                                  |
| Admit rate     | Not published                                                |
| Applied before | No                                                           |
| **AI policy**  | `unstated`                                                   |

## Specifics

- Runs their whole telemetry pipeline on Airflow into BigQuery, per their Aug 2026
  engineering blog post. Source: northline.example.com/blog/telemetry-v2, checked
  2026-09-02.
- Posting names dbt, Airflow, and "ETL" specifically, and asks for SQL over Python
  depth. Source: the posting itself, checked 2026-09-02.
- Hiring manager is named in the posting as the Data Platform lead. Source: posting.

### Unverified, do not use

- Possibly opening a second office. Saw it in a comment thread, could not confirm. Do
  not reference.

## Format requirements

- File type: PDF, uploaded to Greenhouse
- Exact filename required: none specified, so `Lastname_Firstname_Resume.pdf`
- Page limit: one page
- Link permissions: GitHub link in the resume. **Open in a private window.** Two repos
  pinned, both with a README saying what they are
- Video length: n/a

## Posting match

Terms in the posting, and whether the applicant has actually done them. Anything in the
"no" column stays off the resume.

| Their word | Applicant has done it | Resume currently says |
| ---------- | --------------------- | --------------------- |
| ETL        | Yes                   | "data pipelines" → change to their word |
| Airflow    | Yes, in the bootcamp project | Not mentioned → add |
| dbt        | No                    | Leave off. Do not claim it |
| SQL        | Yes                   | Present, but buried in line 4 of a bullet |

## The angle

The resume is the application here. Two prompts exist and both are short. The work is
getting Airflow and ETL onto the page in their vocabulary, moving SQL up, and making
sure the GitHub link is public with the two relevant repos pinned.

Rolling review means applying in week one is worth more than a better application in
week five.

## Questions

### Q1. Why are you interested in this role at Northline? (150 words, required)

> **Unasked:** Have you read anything about us, or is this application number sixty.
> For a rolling posting with no essay tradition, this box mostly screens for whether
> the applicant knows what the company does. Naming the telemetry pipeline is worth
> more than a paragraph about growth and learning.

**Pull from:** the bootcamp pipeline project, connected to their Airflow post.

### Q2. Anything else we should know? (optional, no limit stated)

> **Unasked:** Do you take the free opportunity or not. Optional here is not filler:
> it is the only place a non-obvious background gets explained before a parser makes
> the decision. Leaving it blank answers it badly.

**Pull from:** the reason the coursework looks non-linear.

## Dead lines for this application

- "passionate about the intersection of data and robotics"
- "I thrive in fast-paced environments"
- Any claim involving dbt

## Open items

- GitHub is currently private. Blocking, and it is a two-minute fix.
- Confirm whether the career fair on Sept 18 is before or after they start reviewing.
  If after, apply now and go anyway.
