# Using CoworkOS with Other AI Tools

This template was built against Claude Cowork, and that is still the tool it is documented for by default. But nothing about `CLAUDE.md`, `MEMORY.md`, or any other file here is Claude-specific in format. They are plain markdown. Any AI tool that can read files in a folder and follow written instructions can run this template, whether or not that tool was built by Anthropic.

## The one idea that makes this work

Claude Cowork happens to auto-read a file named `CLAUDE.md` at the start of a session, by its own convention. Most other tools do not share that convention, and do not look for a file by that specific name on their own. So the trick is not reformatting this template once per tool. It is telling whichever tool you are using, explicitly, in your first message to it: read `CLAUDE.md` and follow it. That single instruction is what the copy-paste setup prompt in the main `README.md` does. Once a tool has read `CLAUDE.md`, everything downstream, routing, memory, file creation rules, works exactly as described there, regardless of which company built the tool reading it.

This is why the template does not need a separate version per platform. The instruction-based approach is the compatibility layer.

## What to check before you rely on a given tool

Not every AI tool has the same underlying capabilities, and the template depends on a few of them:

- **It can read and write files in a folder you control**, not just hold a conversation. Without this, there is nothing for `CLAUDE.md` to route or for `MEMORY.md` to record.
- **It can be told a standing instruction at the start of a session** and act on it for the rest of that session, rather than only responding to the single most recent message.
- **Its own built-in memory feature can be pointed at, or turned off for, facts this template already tracks.** Several tools now ship their own automatic memory (separate from anything in this folder). If both are active, you can end up with two different, drifting records of the same fact. When a tool offers this, either rely on `MEMORY.md` as the single source of truth and treat the tool's native memory as redundant, or explicitly tell the tool not to duplicate what is already in these files.

## Notes on specific tools

These are notes, not guarantees. Tool behavior changes, and the exact mechanism each product uses to read a local file was not always documented publicly at the time this was written. Verify against the tool's own current documentation before assuming a detail below still holds.

| Tool | What to know |
| :--- | :--- |
| **Claude Cowork** | Auto-reads `CLAUDE.md` from a connected folder by convention. This is what the template was designed and tested against. |
| **ChatGPT Work Mode** | Reads files inside a Project and supports persistent per-Project custom instructions, alongside its own separate automatic memory. Point it at `CLAUDE.md` explicitly at the start of a session, and decide whether to rely on its native memory or turn to it off in favor of `MEMORY.md`. |
| **Codex CLI (OpenAI)** | Run from a terminal in a real, persistent folder on your machine, the same one every time you run `codex` there, so the folder-confirmation step above is less of a concern here. It auto-reads its own instruction file, `AGENTS.md` (checked at `~/.codex/AGENTS.md` globally and at the project root, merged), the same way Claude Cowork auto-reads `CLAUDE.md`. A one-line `AGENTS.md` at this workspace's root that just says "Read CLAUDE.md and follow it" gets you the same automatic behavior without retyping the install prompt each session. It also has a real local skill mechanism: skills are read from `.agents/skills/` in the repository or `~/.agents/skills/` for your account, and `$skill-installer` can fetch curated ones, so "install `session-audit` as a skill" has a literal, verifiable answer here rather than only a description of the concept. |
| **Codex in the ChatGPT web app** | A different surface from Codex CLI above, and this is the one this template was actually caught out by: each conversation appears to run in its own per-task cloud sandbox rather than a folder you chose, which is where the folder-confirmation step at the top of this file matters most. OpenAI's public documentation does not clearly state whether files persist or how to return to them across sessions, so treat this surface as session-scoped until you have confirmed otherwise for yourself: get the AI tool to confirm the exact save path per the install prompt, and if you cannot find or return to that path afterward, assume you cannot and plan accordingly (Codex CLI, above, is the better fit if you want a workspace that reliably persists). |
| **Kimi Work (Moonshot AI)** | A local desktop agent with local file access. Point it at the folder containing this template and tell it to read `CLAUDE.md` first. |
| **OpenClaw** | An open-source local AI assistant with workspace/file access and its own configuration file. Point it at `CLAUDE.md` the same way; it does not read that filename automatically. |
| **Hermes Agent (Nous Research)** | A self-hosted agent with its own persistent memory and local file access. As with the others, tell it explicitly to read `CLAUDE.md`, and be deliberate about whether its native memory or this template's `MEMORY.md` is the source of truth for a given fact. |
| **Anything else** | If it reads local files and takes a standing instruction, the same approach applies: point it at this folder, tell it to read `CLAUDE.md`, and let the template's own rules take it from there. |

Sources for the Codex row: [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [Codex skills](https://learn.chatgpt.com/codex/build-skills).

## Tools that run in a session-scoped sandbox, not a folder you chose

A growing category of agentic tools, Codex in the ChatGPT web app above is one example, run each conversation in its own disposable cloud environment rather than a folder on your machine that you can point back to. This template's whole memory system depends on `MEMORY.md` and workstation files still being there next time, so a tool like this needs one extra check before you trust it with anything: at the end of your first session, close the tool entirely, reopen it, and confirm you can still reach the exact same files at the exact same path. If you cannot, nothing else in this file will save you, the workspace effectively resets every conversation, and you should either find that tool's actual persistent-storage mechanism (a linked repository, a mounted drive, whatever it calls it) or pick a different tool for this.

## If a tool cannot do this at all

Some AI products are chat-only, with no file access to a folder you control. This template will not work with a tool like that, because there is nowhere for it to write `MEMORY.md` updates or read the Routing Map. That is a real limitation of the tool, not something to work around by pasting file contents into the chat by hand; a copy-pasted snapshot goes stale the moment anything changes.
