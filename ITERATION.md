# Iteration

## What went wrong
Basically the checker gave completely different reports on the same repo and there was no way to compare the runs.

## Why
Since v1 just said "break the requirements into items", each model just decided by itself how to actually split them.

## What I changed
I had it build the list from the deliverables section, only one item per line, and no sub-numbers.

## Result after rerunning
After the fix, I got the same list with two separate runs, but only with Sonnet. It's still a little split with haiku but it's mostly fixed.