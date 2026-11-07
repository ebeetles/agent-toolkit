# Evidence from past Claude Code logs

I pulled these with the `prompt-history` MCP tool (`find_my_prompts`). The tool returns only prompts I typed, word for word. I searched only my course projects: 15113, crossy, elwin-webpage, Signal, Reciplease, rosetta, handoff, Tether, inherited-game.
All timestamps are UTC. Quotes are exact, including typos. Text inside `<pasted_content>` is what I pasted from the assignment pages.

---

## (a) Pasting assignment instructions and asking what's covered or missing

### Best picks

**A1. Signal: "What are we still missing?"**
Project: `Signal` · 2026-09-27 00:10 UTC · session 24925843

> What are we still missing? These are the instructions:
>
> <pasted_content>
> * Backend code deployment: A public Render deployment link to your running backend service. (Note: If you wish to use a different service like Vercel, that's ok too, though we will be best equipped to help you with Render.)
> * Backend code on GitHub: A new public repository containing your backend code (Python using Flask or FastAPI is recommended) along with your readme and prompt log described below. Note that this repository is different from the repository you will use for your frontend.
>    * README: In your backend repo, add a README that briefly explains:
>       * What your backend does (what endpoints it has, what parameters it accepts, what it returns)
>       * How the frontend communicates with the backend (which endpoints it calls, when, and what it does with the response)
>       * How to set up and run the backend (including any environment variables or API keys needed locally)
>       * How authentication or secrets are handled (e.g., API keys stored on the backend, not in frontend code)
>    * Prompt log: In your backend repo, add a short note (in README or a separate file like prompt_log.md) listing which AI model(s)/tool(s) you used and the key prompts that shaped implementation.
> * Frontend code deployed and on GitHub: Add your frontend code to Github pages (either as a new feature on your portfolio or as a separate page, like [the Carnegie Chat example](https://www.cs.cmu.edu/~113/carnegie-chat.html)). This is the HTML/CSS/JavaScript that communicates with your backend. [...]
> </pasted_content>

Why it's good: this is the plainest example of the pattern, with the question first and the pasted deliverables list after it. 16 minutes later (00:26) I pasted the README sub-list again to restructure the README. 21 minutes later (00:31) I was still asking what one deliverable meant: *"when they say A public Render deployment link to your running backend service, is it just https://signal-yfj9.onrender.com/?"*

**A2. rosetta: "Did you follow these directions for the README? We will check this!"**
Project: `rosetta` · 2026-10-27 00:07 UTC · session 4687a82c

> Did you follow these directions for the README? We will check this!
>
> Must be named README.md and located at the repository root (or inside the project folder if you placed the project in your portfolio repo). Include:
> - What your app does and why you chose it (1–2 sentences)
> - What you store in the database: where the data came from, what counts as one item, how you broke it up if you did, roughly how many items you loaded, and what metadata (if any) you attach to each one
> - How a user adds new items, and how a user searches
> - Your two queries from the test above, the items they retrieve, and why a keyword search would miss them
> - How we would obtain and load the data ourselves, since the raw dataset shouldn't be committed to your repo
> - Which vector database and embedding model you used, and whether anything downloads on first run
> - How to run your app (what to install, what commands to use)

Why it's good: I had already pasted the full requirements an hour earlier (2026-10-26 23:09, "Here are the rest of the requirements for my assignment..."). I still pasted them a second time to ask whether the README met them, which means I didn't trust that the first pass had covered them. Note: in the log, my question sits inside the pasted block, so the log counts it as part of the paste.

**A3. inherited-game: "add everything that is not in these instructions"**
Project: `inherited-game` · 2026-11-02 00:38 UTC · session 6d72ac73

> okay lets just add a little thing about what I changed with the UI.js in the README, which is completely fair. as well as add everything that is not in these instructions:
>
> <pasted_content>
> * The initial commit must be the other student's unmodified work, committed before you change anything (see Phase 2 Step 0). This is the easiest thing here to forget and the most annoying to fix later.
> * Your subsequent commits, ideally several small ones rather than one large one
> * Their `SPEC.md`, kept as you received it. Put any additions you want to propose in a clearly marked section at the bottom rather than editing theirs.
> * An updated `README.md` containing your acceptance criteria report, plus run instructions and code map, revised so the next person could take over from you
> * `HANDOFF_REPORT.md`, your honest review of what you inherited
> * `prompt_log.md` for Phase 2, including at least one instance of your AI tool doing something you didn't want, and what you did about it
> * Credit the original author by name at the top of the README. They designed the game and built the foundation.
>
> These are all separate files. The spec, the README, the handoff report, and the prompt log each have a different audience and a different job. Don't merge them, and don't paste one into the bottom of another.
> </pasted_content>

Why it's good: it's the same "find what's missing" request in another form, a deliverables checklist I wanted reconciled against the repo. Two minutes earlier (00:36) I had pasted another section of the instructions and asked *"is this part true:"* (the 75% rule, below).

### Other instances (supporting)

- **inherited-game** · 2026-11-02 00:36 UTC
  > is this part true:
  >
  > <pasted_content>
  > You must keep at least 75% of the original work. You may reorganize, refactor, extend, and fix. You may not quietly discard the foundation and rebuild it in your own image. We compare your final submission against the initial commit of what you received.
  > [...]
  > </pasted_content>

  One minute before that (00:35): *"is at least 75% of the first commit intact"*

- **Tether** · 2026-11-02 01:01 UTC
  > can we add this if it isnt already in the README
  >
  > * Acceptance criteria. A numbered list of specific, checkable statements that define "done", like "the player moves with the arrow keys and jumps with the space bar." Your partner reports back against this list item by item, so write criteria someone can verify.

- **rosetta** · 2026-10-26 23:09 UTC. I pasted the full requirements and grading text, then asked:
  > Seems to work well so far. Here are the rest of the requirements for my assignment. Please update the README to include sample responses to everything I need to include, and I will write them in my own words because I am supposed to write those parts in my own words.

- **handoff** · 2026-10-07 21:46 UTC (followed by a pasted README requirements block):
  > Please update the README with the following criteria. I know I'm supposed to write this myself, but what I want you to do is write generally what is supposed to be included and I will rewrite it all in my own words:

- **Reciplease** · 2026-09-20 20:49 UTC. I pasted only the README requirement, with no question of my own:
  > 1. README: In the repo README, include 3–5 sentences that explain (at a high level) how the API is called [...] Also include brief instructions for running your code: what to install, and what command or file to run.

- **inherited-game**: the same "what's left" question asked against the project's spec rather than the assignment. I asked it 3 times in one session:
  - 2026-10-31 21:46: *"lets look at the things that we are missing from spec.md and continue implementation"*
  - 2026-11-01 22:34: *"What is left from the spec or the handoff that has yet to be implemented"*
  - 2026-11-02 00:14: *"What is left to do in the spec"*

Pattern: this happened in 5 of the 9 projects (Signal, rosetta, inherited-game, Tether, handoff). Reciplease adds a sixth with a pasted requirement and no question. It usually came near the deadline, and often I pasted the same requirements more than once in a session.

---

## (b) Prompt logs that weren't verbatim

### Best picks

**B1. handoff: "prompts 1-3 definitely does NOT look verbatim"** (the only direct callout)
Project: `handoff` · 2026-10-08 01:58 UTC · session 6f0ffaf8

> prompts 1-3 definitely does NOT look verbatim, the rest of the prompts are definitely me

Context, 10 minutes earlier. At 01:48 I asked *"are you able to write up the prompt log for me, theres no rule against AI doing this one. Here are the requirements:"* and at 01:49 I pasted the requirement, which says:
> [...] include important, non-trivial prompts verbatim rather than AI-written summaries of them.

So the agent had the "verbatim" requirement in front of it and still wrote summaries for the first three prompts. I caught it only because I recognized my own writing.

**B2. inherited-game: "is the prompt log verbatim? it should be"**
Project: `inherited-game` · 2026-11-02 00:43 UTC · session 6d72ac73

> is the prompt log verbatim? it should be

Why it's useful: three weeks after B1 I still couldn't trust a generated prompt log without asking. This is a check, not a confirmed catch. My prompt only shows that I didn't trust it. Whether the log was actually wrong is in the agent's reply, which this tool doesn't return. Check the session transcript before claiming it was.

**B3. Asking for "verbatim" up front (rosetta, Tether)**
- `rosetta` · 2026-10-26 23:46 UTC
  > Draft prompt_log.md with my verbatim prompts from this session, marking what I need to fill in or rewrite.
- `Tether` · 2026-11-02 01:37 UTC
  > can you also create a prompt_log.md with verbatim prompts and then commit/push

Why it's useful: after the handoff incident, I put "verbatim" into the request itself every time. It's a manual workaround, and a skill or tool could replace it.

### Honest caveat for the write-up
Across all 9 projects there is **one** explicit callout of a non-verbatim prompt log (B1). B2 is a follow-up check whose result isn't in my prompts, and B3 shows the habit I built because of B1. If the write-up says this happened "repeatedly", support it with B1 + B2 + B3 together as a pattern, not as several confirmed failures.

---

## Searches run (for reproducibility)
- Pulled every prompt for each of the 9 projects (`find_my_prompts`, project = each name).
- Searched all of them for `contains: "verbatim"` (6 hits, all listed above) and `"i never said"` (0 hits).
- Fetched full text (`max_chars: 0`) for every quote above.
