"""Turn a `claude -p --output-format stream-json` log into a trimmed markdown transcript."""
import json, sys

def trim(s, n):
    s = s if isinstance(s, str) else json.dumps(s)
    return s if len(s) <= n else s[:n] + f" …[{len(s)-n} chars trimmed]"

src, n = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 600
for line in open(src):
    try: d = json.loads(line)
    except Exception: continue
    t = d.get("type")
    if t == "system" and d.get("subtype") == "init":
        mcp = [m for m in d.get("tools", []) if m.startswith("mcp__")]
        print(f"**session init** — model `{d.get('model')}`, MCP servers {d.get('mcp_servers')}, MCP tools {mcp}\n")
    elif t == "user" and isinstance(d["message"]["content"], str):
        print(f"**USER:** {d['message']['content']}\n")
    elif t == "assistant":
        for b in d["message"]["content"]:
            if b["type"] == "text" and b["text"].strip():
                print(f"**ASSISTANT:** {trim(b['text'], 4000)}\n")
            elif b["type"] == "tool_use":
                print(f"**TOOL CALL → `{b['name']}`** `{trim(b['input'], 400)}`\n")
    elif t == "user":
        for b in d["message"]["content"]:
            if isinstance(b, dict) and b.get("type") == "tool_result":
                c = b.get("content")
                if isinstance(c, list): c = "\n".join(x.get("text", "") for x in c if isinstance(x, dict))
                print("<details><summary>tool result</summary>\n\n```\n" + trim(c or "", n) + "\n```\n</details>\n")
    elif t == "result":
        print(f"\n---\n*result: {d.get('subtype')}, turns={d.get('num_turns')}, cost=${d.get('total_cost_usd', 0):.2f}, {d.get('duration_ms', 0)//1000}s*")
