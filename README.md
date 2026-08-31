# CoworkOS

A minimal, installable framework for running Claude as a persistent, structured assistant across every area of your life or work.

Instead of one long system prompt, CoworkOS gives Claude a small set of markdown files that work together: a routing protocol that sends each task to the right context, a memory system that persists across sessions, and one governance rule that keeps every fact and every instruction in exactly one place.

## What this is

Two root files, plus two short reference folders:

- `CLAUDE.md` - the constitution. How Claude reads memory, routes tasks, and decides where new information belongs.
- `MEMORY.md` - the notepad. Facts, decisions, and active work that should carry forward between sessions.
- `00_Reference/` - the mechanics behind the rules in `CLAUDE.md`, loaded on demand rather than every session.
- `00_Resources/` - supporting material, such as the guide for creating a new workstation.

A "workstation" is a folder for one area of life or work: a job, a side project, health, finances, relationships, anything that deserves its own context. Each one gets its own `CLAUDE.md` and `MEMORY.md`, scoped to that domain, so the root files never have to hold everything at once.

## How it works

At the start of a session, Claude reads root `MEMORY.md` for orientation, then routes the task to the right workstation using the Routing Map in `CLAUDE.md`. It reads that workstation's own `CLAUDE.md` and `MEMORY.md`, does the work, and proposes any new memory entries for approval before writing them. Every rule about where a new file or a new fact belongs comes down to one test, spelled out in the Governance section of `CLAUDE.md`: does it prescribe behavior, or does it describe a fact about the world that could change.

## Getting started

1. Copy this repository's files into a folder Claude can read and write to.
2. Start a session and say what you want to track. `CLAUDE.md` includes a first-run setup flow: Claude suggests common areas (work, personal finances, health, relationships, projects, and so on) and only creates the workstations you actually pick.
3. Work normally. Correct Claude when it gets something wrong, and it will propose a memory entry so the correction sticks.

Nothing is pre-populated. The Routing Map starts empty and fills in as you create workstations.

## Session audit: closing out a session properly

The memory system above only works if MEMORY.md and CLAUDE.md stay current, and that depends on something noticing, mid-conversation, that a correction or a decision is worth saving. Plenty of what should be captured is not that explicit: a small correction that got fixed and moved past, a preference mentioned in passing, a decision buried inside an unrelated task. Nothing surfaces those unless something deliberately looks back over the whole conversation before it ends.

`skills/session-audit/SKILL.md` is that deliberate look back. Run it, or a skill like it, at the end of a session: it scans the conversation for uncaptured corrections, preferences, decisions, and new context, proposes exactly where each one belongs, writes only what you approve, and, if the workspace is a git repository, syncs everything to the remote as the last step. Install it as a skill in your Claude account, or reference it directly if your setup loads skills from a folder, and trigger it with "audit this session," "session audit," "what did we miss," "end of session check," or "close out the session." Without a habit like this, the memory system slowly drifts out of date instead of actually staying current.

## Structure

| Path | Purpose |
| :--- | :--- |
| `CLAUDE.md` | Memory system, routing protocol, governance, first-run setup |
| `MEMORY.md` | Template for persistent, cross-session facts |
| `00_Reference/Governance Rules.md` | Section ordering, size caps, and the rules for where content goes |
| `00_Reference/File Creation Rules.md` | Naming, placement, and approval rules for new files |
| `00_Reference/Memory System.md` | Full mechanics: capture triggers, entry format, archiving |
| `00_Resources/Workstation Setup Guide.md` | How to create a new workstation |
| `skills/session-audit/SKILL.md` | End-of-session audit: capture what was learned, sync the workspace |

## Credits

This architecture is adapted from Jeff Su's Claude Cowork tutorials, in particular ["Claude Cowork for Beginners: Build Your Own Jarvis"](https://www.jeffsu.org/claude-cowork-build-your-own-jarvis/) and the video ["Learn 80% of Claude Cowork in Under 20 Minutes"](https://www.youtube.com/watch?v=z9rdrNrkvDY). If you are new to this pattern, start there.

## License

MIT. See `LICENSE`.
