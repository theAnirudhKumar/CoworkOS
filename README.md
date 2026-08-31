# CoworkOS

A minimal, installable framework for running Claude as a persistent, structured assistant across every area of your life or work.

Instead of one long system prompt, CoworkOS gives Claude a small set of markdown files that work together: a routing protocol that sends each task to the right context, a memory system that persists across sessions, and one governance rule that keeps every fact and every instruction in exactly one place. It ships with a worked example so you can see the pattern filled in, not just described.

## What this is

- `CLAUDE.md`, `MEMORY.md`, `ARCHIVE.md` - the three root files. The constitution, the notepad, and the historical record.
- `00_Reference/` - the mechanics behind the rules in `CLAUDE.md`, loaded on demand rather than every session.
- `00_Resources/` - supporting material, such as the guide for creating a new workstation and a starter voice-principles file.
- `00_Skills/` - a register of the skills your Claude account actually has, and a recovery copy of the ones you build yourself. See "Skills live on your account, not in this folder" below.
- `Example Workstation/` - a filled-in sample so you can see what a real workstation looks like, not just read a description of one. Rename or delete it once the pattern clicks.
- `.gitignore` and `.githooks/pre-commit` - optional, if you put this workspace under version control. See "Protecting what goes in here" below.

A "workstation" is a folder for one area of life or work: a job, a side project, health, finances, relationships, anything that deserves its own context. Each one gets its own `CLAUDE.md` and `MEMORY.md`, scoped to that domain, so the root files never have to hold everything at once.

## How it works

At the start of a session, Claude reads root `MEMORY.md` for orientation, then routes the task to the right workstation using the Routing Map in `CLAUDE.md`. It reads that workstation's own `CLAUDE.md` and `MEMORY.md`, does the work, and proposes any new memory entries for approval before writing them. Every rule about where a new file or a new fact belongs comes down to one test, spelled out in the Governance section of `CLAUDE.md`: does it prescribe behavior, or does it describe a fact about the world that could change.

## Getting started

1. Copy this repository's files into a folder Claude can read and write to.
2. Look at `Example Workstation/` first. It is the fastest way to understand what "a workstation" actually means in practice, before you build your own.
3. Start a session and say what you want to track. `CLAUDE.md` includes a first-run setup flow: Claude suggests common areas (work, personal finances, health, relationships, projects, and so on) and only creates the workstations you actually pick.
4. Rename or delete `Example Workstation/` once you have created your own, and remove its row from the Routing Map.
5. Work normally. Correct Claude when it gets something wrong, and it will propose a memory entry so the correction sticks.

## Closing out a session properly

The memory system above only works if `MEMORY.md` and `CLAUDE.md` stay current, and that depends on something noticing, mid-conversation, that a correction or a decision is worth saving. Plenty of what should be captured is not that explicit: a small correction that got fixed and moved past, a preference mentioned in passing, a decision buried inside an unrelated task. Nothing surfaces those unless something deliberately looks back over the whole conversation before it ends.

`00_Skills/Custom/session-audit/SKILL.md` is that deliberate look back. Run it, or a skill like it, at the end of a session: it scans the conversation for uncaptured corrections, preferences, decisions, and new context, proposes exactly where each one belongs, writes only what you approve, and, if the workspace is a git repository, syncs everything to the remote as the last step. Trigger it with "audit this session," "session audit," "what did we miss," "end of session check," or "close out the session." Without a habit like this, the memory system slowly drifts out of date instead of actually staying current.

## Skills live on your account, not in this folder

A skill runs from your Claude account. Nothing in `00_Skills/` is read as a live skill; invoking one always uses the account copy. So this folder is not where skills execute from, it is where you keep a copy of them so they are not lost if the account version is ever edited by accident or you switch machines. `00_Skills/Skills Inventory.md` is the index, `Custom/` holds skills you wrote yourself, and `Third-Party/` holds someone else's, kept with their original license. The rule is simple: when you build or change a skill on your account, archive it here in the same session.

## Protecting what goes in here

This template assumes you will eventually put real personal information into it: budgets, health notes, contact details, whatever your workstations end up tracking. If you keep this workspace under version control, that information ends up in git history too, and git history is permanent by default.

`.gitignore` keeps common personal-document filenames out of the repository entirely. `.githooks/pre-commit` goes a step further: it scans every commit for the shape of a government ID number, a bank identifier, or a financial-account number, and refuses the commit if it finds one. It ships with a couple of example formats (Indian ID documents, a US Social Security Number) since those are what the author could write correctly; read the comments at the top of the file and adjust the patterns for whatever applies where you live. Neither of these does anything until you activate the hook once, from inside the workspace:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
```

Both are optional. If you never put this workspace under git, neither file does anything, and you can delete them.

## Structure

| Path | Purpose |
| :--- | :--- |
| `CLAUDE.md` | Memory system, routing protocol, governance, first-run setup |
| `MEMORY.md` | Template for persistent, cross-session facts |
| `ARCHIVE.md` | The historical record: completed work, read only on demand |
| `00_Reference/Governance Rules.md` | Section ordering, size caps, and the rules for where content goes |
| `00_Reference/File Creation Rules.md` | Naming, placement, and approval rules for new files |
| `00_Reference/Memory System.md` | Full mechanics: capture triggers, entry format, archiving |
| `00_Resources/Workstation Setup Guide.md` | How to create a new workstation |
| `00_Resources/voice-principles.md` | Starter file for how written output should sound; fills in through use |
| `00_Skills/Skills Inventory.md` | Index of skills archived from your account |
| `00_Skills/Custom/session-audit/SKILL.md` | The session-audit skill itself, and the worked example of the registry pattern |
| `00_Skills/Third-Party/` | Where someone else's archived skill goes |
| `Example Workstation/` | A filled-in sample workstation: `CLAUDE.md` and `MEMORY.md` with realistic content |
| `.gitignore`, `.githooks/pre-commit` | Optional protection if you version-control this workspace |

## Credits

This architecture is adapted from Jeff Su's Claude Cowork tutorials, in particular ["Claude Cowork for Beginners: Build Your Own Jarvis"](https://www.jeffsu.org/claude-cowork-build-your-own-jarvis/) and the video ["Learn 80% of Claude Cowork in Under 20 Minutes"](https://www.youtube.com/watch?v=z9rdrNrkvDY). If you are new to this pattern, start there.

## License

MIT. See `LICENSE`.
