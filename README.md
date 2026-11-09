# hw8-agent-toolkit

This repo contains a submission checker skill as well as an MCP server for prompt history finding.

### `submission-check` (skill)
The submission-check skill essentially checks an assignment repo against the assignments list of deliverables. This skill only reports and never actually edits anything. This skill is triggered when there are phrases such as "what are we still missing", "did we follow all instructions", "is this ready to turn in", etc. It does not trigger on a plain code review. 

### `prompt-history` (MCP server)

`find_my_prompts` basically just returns exactly what you prompted in past claude code sessions verbatim, and includes timestamps as well. I chose to register an MCP server for this instead of making a skill because the agent cannot see past sessions, and it cant even see the current session after compaction. 

## Why I built these (evidence from my logs)

### Checker
I built these because sometimes I would accidentally miss something small in the assignment writeup and then I'll have to go through and double check it, or tell claude to double check it and then it needs context
> "What are we still missing? These are the instructions:" (Signal, 2026-09-27)
> "Did you follow these directions for the README?" (rosetta, 2026-10-27)

### MCP tool
I built this because I found it very difficult to get prompt logs because I don't keep track of it along the way, and it's kinda lost when claude does compaction as well. So to have this as an MCP tool is extremely useful.
> "prompts 1-3 definitely does NOT look verbatim, the rest of the prompts are definitely me" (handoff, 2026-10-08)
> "is the prompt log verbatim? it should be" (inherited-game, 2026-11-02)

## Install

### Skill
Copy `skills/submission-check/` to one of:
- `~/.claude/skills/submission-check/` (all projects)
- `<your-project>/.claude/skills/submission-check/` (one project)

The checker reads the assignment from `ASSIGNMENT.md` in the project root. Paste the assignment's text there, or paste it into chat.

### MCP server
```bash
cd mcp-server
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```
`requirements.txt` pins `mcp<2`. The FastMCP example from class breaks on mcp 2.x.

Register with Claude Code (**replace both paths with absolute paths on your machine**):
```bash
claude mcp add --scope user prompt-history -- \
  /ABSOLUTE/PATH/TO/mcp-server/.venv/bin/python \
  /ABSOLUTE/PATH/TO/mcp-server/prompt_history_server.py
```
Or as JSON config:
```json
{
  "mcpServers": {
    "prompt-history": {
      "command": "/ABSOLUTE/PATH/TO/mcp-server/.venv/bin/python",
      "args": ["/ABSOLUTE/PATH/TO/mcp-server/prompt_history_server.py"]
    }
  }
}
```
It reads `~/.claude/projects` by default. Set `CLAUDE_PROJECTS_DIR` to point it elsewhere.

## Where I confirmed it works
- Claude Code CLI 2.1.319, Linux, headless (`claude -p`): server connected and tool called (transcript 01)
- doer on Opus 5.5, checker on Sonnet 5.5 and Haiku 5.5
- macOS Claude Code:

## Borrowed / adapted
The skill structure comes from the course's `spec-check` example
The server skeleton comes from the course's FastMCP example; the log parsing is original.

## How I used AI
Claude Opus 5.5 helped with construction of the skill, the MCP server scripts.

See [DEMONSTRATION.md](DEMONSTRATION.md) for the runs and [ITERATION.md](ITERATION.md) for what broke and how it was fixed.