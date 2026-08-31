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
| **Kimi Work (Moonshot AI)** | A local desktop agent with local file access. Point it at the folder containing this template and tell it to read `CLAUDE.md` first. |
| **OpenClaw** | An open-source local AI assistant with workspace/file access and its own configuration file. Point it at `CLAUDE.md` the same way; it does not read that filename automatically. |
| **Hermes Agent (Nous Research)** | A self-hosted agent with its own persistent memory and local file access. As with the others, tell it explicitly to read `CLAUDE.md`, and be deliberate about whether its native memory or this template's `MEMORY.md` is the source of truth for a given fact. |
| **Anything else** | If it reads local files and takes a standing instruction, the same approach applies: point it at this folder, tell it to read `CLAUDE.md`, and let the template's own rules take it from there. |

## If a tool cannot do this at all

Some AI products are chat-only, with no file access to a folder you control. This template will not work with a tool like that, because there is nowhere for it to write `MEMORY.md` updates or read the Routing Map. That is a real limitation of the tool, not something to work around by pasting file contents into the chat by hand; a copy-pasted snapshot goes stale the moment anything changes.
