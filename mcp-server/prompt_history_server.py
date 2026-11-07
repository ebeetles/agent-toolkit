"""prompt-history: an MCP server that gives an agent read access to the prompts
I actually typed in past Claude Code sessions.

Claude Code saves every session as JSONL under ~/.claude/projects/<encoded-path>/.
Those files are huge and mostly tool calls, tool output, skill bodies and
compaction summaries. This server pulls out only the human-typed prompts,
verbatim, so an agent can quote them instead of reconstructing them.
"""

import json
import os
import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP

PROJECTS_DIR = Path(
    os.environ.get("CLAUDE_PROJECTS_DIR", Path.home() / ".claude" / "projects")
).expanduser()

mcp = FastMCP("prompt-history")


def log(msg: str) -> None:
    # stdout is the MCP protocol stream; anything human-readable goes to stderr.
    print(f"[prompt-history] {msg}", file=sys.stderr)


def _text_of(content) -> str | None:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = [
            b.get("text", "")
            for b in content
            if isinstance(b, dict) and b.get("type") == "text"
        ]
        return "\n".join(parts) if parts else None
    return None


def _is_human_prompt(rec: dict, text: str) -> bool:
    if rec.get("type") != "user" or rec.get("isSidechain"):
        return False
    if rec.get("isMeta") or rec.get("isCompactSummary"):
        return False
    origin = rec.get("origin")
    if isinstance(origin, dict) and origin.get("kind") != "human":
        return False
    stripped = text.lstrip()
    machine_prefixes = (
        "<command-name>",
        "<local-command",
        "<task-notification>",
        "<system-reminder>",
        "Caveat:",
        "Base directory for this skill:",
        "This session is being continued from a previous conversation",
        "[Request interrupted by user",
    )
    return not stripped.startswith(machine_prefixes)


def _matching_projects(project: str) -> list[Path]:
    if not PROJECTS_DIR.is_dir():
        return []
    key = project.lower().replace("/", "-").replace(" ", "-")
    return sorted(
        d for d in PROJECTS_DIR.iterdir() if d.is_dir() and key in d.name.lower()
    )


@mcp.tool()
def find_my_prompts(
    project: str,
    contains: str = "",
    since: str = "",
    until: str = "",
    limit: int = 40,
    max_chars: int = 1500,
) -> str:
    """Return the prompts I (the human) actually typed in past Claude Code
    sessions for a project, word for word, oldest first, with timestamps.

    Use this whenever you need my exact past wording: writing or checking a
    prompt_log.md that must contain verbatim prompts, recalling what I asked
    for in an earlier session, or checking whether a quoted prompt is real.
    Do NOT paraphrase, summarize, or "clean up" what this returns; if you quote
    it, quote it exactly. Compaction summaries, skill text, tool output and
    slash commands are already filtered out, so everything returned is mine.

    Args:
        project: Part of the project folder name or path, e.g. "handoff" or
            "rosetta". Matched case-insensitively against Claude Code's
            per-project log folders. If nothing matches, the available
            projects are listed.
        contains: Optional case-insensitive substring; only prompts containing
            it are returned.
        since / until: Optional ISO date bounds like "2026-10-05".
        limit: Max prompts to return (default 40).
        max_chars: Long prompts (pasted specs) are cut at this length and
            marked [TRUNCATED]. Pass 0 for no limit.
    """
    dirs = _matching_projects(project)
    if not dirs:
        available = (
            ", ".join(sorted(d.name for d in PROJECTS_DIR.iterdir() if d.is_dir()))
            if PROJECTS_DIR.is_dir()
            else f"(log folder {PROJECTS_DIR} not found)"
        )
        return f"No project matching '{project}'. Available: {available}"

    prompts = []
    seen = set()
    for d in dirs:
        for f in sorted(d.glob("*.jsonl")):
            with f.open(errors="ignore") as fh:
                for line in fh:
                    try:
                        rec = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    text = _text_of(rec.get("message", {}).get("content"))
                    if not text or not _is_human_prompt(rec, text):
                        continue
                    ts = rec.get("timestamp", "")
                    if since and ts[: len(since)] < since:
                        continue
                    if until and ts[: len(until)] > until:
                        continue
                    if contains and contains.lower() not in text.lower():
                        continue
                    key = (rec.get("sessionId"), text.strip())
                    if key in seen:
                        continue
                    seen.add(key)
                    prompts.append((ts, rec.get("sessionId", "?")[:8], d.name, text.strip()))

    prompts.sort(key=lambda p: p[0])
    total = len(prompts)
    prompts = prompts[:limit]
    log(f"{project!r}: {total} prompts matched, returning {len(prompts)}")

    if not prompts:
        return f"No human prompts found for '{project}' with those filters."

    out = [f"{total} prompts matched in {', '.join(d.name for d in dirs)}; showing {len(prompts)}.\n"]
    for i, (ts, sid, proj, text) in enumerate(prompts, 1):
        if max_chars and len(text) > max_chars:
            text = text[:max_chars] + f"\n[TRUNCATED: {len(text) - max_chars} more chars]"
        out.append(f"--- #{i} | {ts[:16].replace('T', ' ')} UTC | session {sid} ---\n{text}\n")
    return "\n".join(out)


if __name__ == "__main__":
    log(f"reading logs from {PROJECTS_DIR}")
    mcp.run()
