---
name: submission-check
description: Audits a course assignment repo against the assignment's own deliverables list before submission. Reports each requirement as MET, PARTIAL, MISSING, or YOU-WRITE, with file evidence. Use when asked "what are we still missing", "did we follow the instructions", or before pushing/submitting an assignment.
---

# Submission Check

## What to do

1. Find the assignment requirements. Look for `ASSIGNMENT.md` in the repo root, or use the requirements text the user pasted. If neither exists, stop and ask for it. Never reconstruct requirements from memory.
2. Break the requirements into numbered, individually checkable items. Keep the assignment's own wording.
3. For each item, find the file and line that satisfies it.
4. Do not fix anything. Report only.

## Output format

One line per requirement:

`[MET | PARTIAL | MISSING | YOU-WRITE] #<n>: <requirement, short> — <evidence: file:line, or what is absent>`

Then:

- **Top 3 gaps** to fix before submitting, most costly first.
- **You must write these yourself:** every item the assignment says must be in the student's own words, with its current state (missing / placeholder / looks AI-drafted).

## Rules

- Do not modify, create, or delete any file. Do not draft the missing text.
- Cite a file and line for every MET. No citation means it is not MET.
- Judge the repo, not what the README claims. If the README says `python app.py`, check that `app.py` exists.
- If the assignment says a section must be written by the student ("in your own words", "write this yourself"), mark it YOU-WRITE, never MET, even if text is present.
- Prompt logs that must be "verbatim": if the `find_my_prompts` tool is available, check at least five quoted prompts against it. Any quote not found word for word makes that item PARTIAL; list the quote.
- Treat "separate files" requirements literally (e.g. README and prompt log must not be merged).
