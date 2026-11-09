# Demonstration

## Run 1: gathering evidence for this assignment

I ran the MCP tool on my past 113 project repos in order to get evidence to put into this assignment

**Doer** ([transcript](evidence/transcripts/02-run1-doer-opus.md))
```
find_my_prompts {"project": "15113", "limit": 100}   ← one of 16 calls, one per project
```
Wrote `notes/evidence.md` with quotes from my logs.

**Checker** ([transcript](evidence/transcripts/03-run1-checker-sonnet-v1.md)), prompt: "I'm about to submit this. What are we still missing?"
```
Skill {"skill": "submission-check"}
[MISSING] #3: README.md — no README.md at the repo root.
[PARTIAL] #6: Two demo runs ... There is no run 2.
[MISSING] #7: ITERATION.md — absent ...
```

I do agree with the checker, it was meant to be a test to see whether or not it will catch missing files and they were in fact missing.

## Run 2: fixing my HW6 (Rosetta) prompt log

One of my projects had a prompt log where some of them weren't verbatim before.

**Doer** ([transcript](evidence/transcripts/04-run2-doer-opus.md), [diff](evidence/run2-rosetta-prompt_log.diff))
```
find_my_prompts {"project": "rosetta", "limit": 200, "max_chars": 0}
```
All 16 quoted prompts were already verbatim; it added 2 missing ones.

**Checker** ([transcript](evidence/transcripts/05-run2-checker-sonnet-v1.md)), prompt: "did we follow all the instructions for this assignment? about to submit"
```
Skill {"skill": "submission-check"}
find_my_prompts {"project": "rosetta", "limit": 100}
[YOU-WRITE] #3 ... The brief asks for 1–2 sentences and this is about five, so trim it.
[PARTIAL] #13 Verbatim prompts ... I checked 16 quoted in the log, and each matched word for word.
#5 Add and search | Present and accurate, but it looks AI-drafted.
```

I agree with this, because I made sure to fix the prompt log and it was verbatim and the checker also revealed the same conclusion.
