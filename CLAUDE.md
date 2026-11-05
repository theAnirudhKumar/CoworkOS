# CLAUDE.md

This is a workstation-based AI workspace: each folder under the root represents one area of life or work, with its own identity, workflow, and accumulated context. It was designed and tested against Claude Cowork, but nothing about this file's format is Claude-specific; read this file at the start of every session, whichever AI tool is reading it. See 00_Resources/Using CoworkOS with Other AI Tools.md for notes on other tools.

---

## Memory System

At the start of every session: read MEMORY.md before responding. Use what you find to inform your work, without announcing it.

Memory writes require approval. Propose an entry when something memory-worthy happens, but never write to MEMORY.md without confirmation first. Entries can also be triggered directly: phrases like "remember this," "make a note," "don't forget," "log this," "from now on," or "always." Once a write is approved, make it right away and confirm it was done.

All memory entries are persistent. They stay in MEMORY.md until the user asks to remove or change them.

Flag contradictions. If a new instruction conflicts with an existing memory entry, do not silently overwrite it. Say what conflicts and ask how to reconcile it.

Full mechanics (capture triggers, entry format, archiving) are in 00_Reference/Memory System.md.

At the end of a session, run the session-audit skill (00_Skills/Custom/session-audit/SKILL.md) rather than relying on memory writes caught mid-conversation. It scans the whole session for corrections, preferences, and decisions that were never written down, proposes where each belongs, and applies only what is approved. This is what keeps this file and MEMORY.md actually current instead of slowly drifting stale.

**Where things go.** Apply two tests when deciding where to save something. Test 1: does it prescribe behavior (look for "always," "never," "before doing X, do Y")? If so, it belongs in this file, under the right section. Test 2: does it describe a fact about the world that could change (status, a decision, a preference, something the user asked to be remembered)? If so, it belongs in MEMORY.md. When neither test clearly applies, say which file seems right and ask for confirmation before writing.

---

## Routing Protocol

Before starting any task, identify the relevant workstation from the Routing Map below, read its CLAUDE.md and MEMORY.md, and state which files were loaded before responding.

Loading context is never skipped, and never shortened because the task looks small. Before the first draft, file or reply, also read every reference file those two files point to for that kind of work, such as 00_Resources/voice-principles.md before writing anything as or for the user, and 00_Reference/File Creation Rules.md before creating a file. This applies to a session continued from a summary too. If a file is too large to read in one go, read it in parts; a search inside a file is no substitute for reading it. Short requests are where this gets dropped, so start the first reply with the list of files loaded.

If this workspace syncs to GitHub (see 00_Resources/GitHub Sync Guide.md), check it is current before changing anything: fetch, then check the status. If the remote has commits this copy has not seen, usually from working on another device, say so and stop before editing. Close any app that keeps files open in memory, such as a note-taking app, before pulling, because it can write its old copy back over the pulled files.

### First-time setup

If SETUP.md exists at the root of this workspace, first-run setup has not been finished. Read it and follow it before anything else, including before the Routing Protocol above; it resumes from wherever a previous session left off. SETUP.md deletes itself as its last step, and removes this subsection along with it.

---

## Preferences

*Starter section. As you discover how the user likes to work (tone, response length, formatting habits, how they want choices presented), note it here. This file ships with no assumptions about that.*

---

## Rules

*Starter section, for standing behavioral rules the user states directly ("always," "never," "before X do Y"). This file ships with none. 00_Resources/Starter Rules.md holds a menu of tested rules the user can pick from. Add rules here as they come up, and apply the two placement tests above to decide whether something belongs here or in MEMORY.md.*

---

## Governance: MECE Principle

All instructions, rules, and context in this workspace should be mutually exclusive and collectively exhaustive: every rule lives in exactly one place. No duplication across this file, MEMORY.md, or workstation files.

- **This file (CLAUDE.md)** owns: workspace identity, routing, and behavior rules.
- **MEMORY.md** owns: cross-cutting facts that accumulate over time (decisions, preferences, status).
- **00_Reference/** owns: detailed, stable reference material and governance mechanics, loaded on demand.
- **00_Resources/** owns: supporting material loaded on demand, such as setup guides, templates, the tool-compatibility notes, and the GitHub sync guide.
- **Workstation CLAUDE.md files** own: domain-specific identity and workflow. They layer on top of this file and never restate it.
- **Workstation MEMORY.md files** own: domain-specific facts and decisions.
- **ARCHIVE.md** owns: the permanent historical record of completed work, the Workspace Changelog. Never read at session start, only pulled up on demand.
- **AGENTS.md** owns nothing. It is a one-line pointer to this file for AI tools that look for that name.
- **Dashboard.html** owns nothing. It is a page that reads these files and shows them in a browser, so the user can see, browse and edit their workspace outside the chat. Its name for the user lives in Core Memory in MEMORY.md.
- **98_Temp/ and 99_Archive/** own files, not rules: 98_Temp holds files whose home is not clear yet, and 99_Archive holds old files that are no longer current. Neither is a workstation.
- **00_Skills/** owns: the record of what skills exist on your AI tool's account, and the archived source of the custom ones. It is a register and a recovery path, never a live skill directory; invoking a skill always uses the account copy.

When adding a new rule, decide where it belongs using the two tests in the Memory System section. If unsure, ask.

---

## Routing Map

*Add a row here for every workstation you create. Your AI tool checks this table to decide which workstation folder to load for a given task.*

| Workstation | Route here when the user... |
| :--- | :--- |
| Example Workstation | *Sample row for the sample workstation shipped with this template.* Asks about budgeting, spending, subscriptions, or personal finances. Replace this row once you rename or remove the example. |

---

## Memory & Governance

| Resource | Read when... |
| :--- | :--- |
| 00_Reference/Governance Rules.md | Modifying this file, adding a new section, or deciding where a rule belongs |
| 00_Reference/File Creation Rules.md | Creating any new file in the workspace |
| 00_Reference/Memory System.md | Writing a memory entry, running an archive pass, or handling a contradiction |
| 00_Reference/Visual Standards.md | Producing anything with visual structure: steps, tables, diagrams, or a generated PDF, Word file or deck |
| 00_Reference/CLAUDE.md Change Log.md | Changing this file, or finding out why one of its rules says what it says |
| 00_Resources/voice-principles.md | Writing anything as or for the user |
| 00_Resources/Connectors Guide.md | Connecting another app such as a calendar, email or file storage, or deciding what a connector may do |
| 00_Resources/Starter Rules.md | The user asks how to make their AI tool more reliable, or wants to adopt more working rules |
| 00_Resources/Workstation Setup Guide.md | Creating a new workstation |
| 00_Skills/Skills Inventory.md | Closing out a session (points to the session-audit skill), or understanding how account skills are archived in this workspace |
| 00_Resources/Using CoworkOS with Other AI Tools.md | Running this workspace on an AI tool other than Claude Cowork |
| 00_Resources/GitHub Sync Guide.md | Setting up the optional GitHub sync, or understanding what it involves before agreeing to it |
| Dashboard.html | The user asks how to see, browse or edit their files outside the chat. Tell them to double-click Dashboard.html in the workspace folder and choose the folder when asked |
| 00_Resources/Troubleshooting.md | Setup or installation isn't going the way this file describes |
