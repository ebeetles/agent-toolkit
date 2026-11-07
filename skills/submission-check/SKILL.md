---
name: submission-check
description: Audits a course assignment repo against the assignment's own deliverables list before submission. Reports each deliverable as MET, PARTIAL, or MISSING with file evidence, and lists the parts I must write myself. Use when asked "what are we still missing", "did we follow the instructions", "is this ready to turn in", or before pushing/submitting an assignment.
---

# Submission Check

## What to do

1. Find the assignment text: `ASSIGNMENT.md` in the repo root, or text the user pasted. If neither exists, stop and ask for it. Never reconstruct requirements from memory.
2. Build the checklist from the **deliverables section only** (headed something like "What to Submit", "Deliverables", or "GitHub repository containing"). Grading tables, tips, and "avoid these shortcuts" notes are not deliverables.
3. One item per line or bullet in that section, in document order, numbered `#1, #2, #3…` with no sub-numbers. A line with several sentences is still one item. Do not merge, split, reorder, or add items. Two runs on the same assignment must produce the same numbered list.
4. A line that only says who must write something ("write the first four items yourself", "written by you") is not an item. Apply it as the `(you write)` tag on the items it covers.
5. For each item, find the file and line that satisfies it. Do not fix anything.

## Output format

One line per item, nothing before the list except one sentence naming the assignment file you used:

`[MET | PARTIAL | MISSING] #<n>: <item, short> — <evidence: file:line, or what is absent>` and append ` (you write)` if the assignment says the student must write it.

Then:

- **Top 3 gaps** to fix before submitting, most costly first.
- **You write these:** each `(you write)` item with its location. Do not guess who wrote the current text.

## Rules

- Do not modify, create, or delete any file. Do not draft missing text.
- Cite a file and line for every MET. No citation, not MET.
- Judge the repo, not what the README claims. If the README says `python app.py`, check that `app.py` exists.
- Status is about coverage only. Authorship is the `(you write)` tag. You cannot tell who wrote a passage, so never call text "AI-drafted" or "in your voice", and never mark authorship itself as MET. Only literal placeholder markers (TODO, `[write this]`, "rewrite in my own words") count against a `(you write)` item.
- Verbatim prompt logs: only text presented as a quoted prompt must match. If the `find_my_prompts` tool is available, check at least five quotes against it and list any that don't match word for word. Narrative and summaries between quotes are fine.
- Items that live outside the repo (video link, Google form) are MISSING with "can't verify from repo" unless the repo links them.
