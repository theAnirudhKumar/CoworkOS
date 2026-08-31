# CLAUDE.md

This is a Claude Cowork workspace built on a workstation-based architecture: each folder under the root represents one area of life or work, with its own identity, workflow, and accumulated context. Read this file at the start of every session.

---

## Memory System

At the start of every session: read MEMORY.md before responding. Use what you find to inform your work, without announcing it.

Memory writes require approval. Propose an entry when something memory-worthy happens, but never write to MEMORY.md without confirmation first. Entries can also be triggered directly: phrases like "remember this," "make a note," "from now on," or "always."

All memory entries are persistent. They stay in MEMORY.md until the user asks to remove or change them.

Flag contradictions. If a new instruction conflicts with an existing memory entry, do not silently overwrite it. Say what conflicts and ask how to reconcile it.

Full mechanics (capture triggers, entry format, archiving) are in 00_Reference/Memory System.md.

At the end of a session, run the session-audit skill (skills/session-audit/SKILL.md) rather than relying on memory writes caught mid-conversation. It scans the whole session for corrections, preferences, and decisions that were never written down, proposes where each belongs, and applies only what is approved. This is what keeps this file and MEMORY.md actually current instead of slowly drifting stale.

**Where things go.** Apply two tests when deciding where to save something. Test 1: does it prescribe behavior (look for "always," "never," "before doing X, do Y")? If so, it belongs in this file, under the right section. Test 2: does it describe a fact about the world that could change (status, a decision, a preference, something the user asked to be remembered)? If so, it belongs in MEMORY.md. When neither test clearly applies, say which file seems right and ask for confirmation before writing.

---

## Routing Protocol

Before starting any task, identify the relevant workstation from the Routing Map below, read its CLAUDE.md and MEMORY.md, and state which files were loaded before responding.

### First-time setup

Run this the first time this workspace is used, or whenever the Routing Map below is still empty.

1. Ask what areas of life or work should be tracked here. Offer a short list of common starting points as suggestions, not a fixed menu: work or career, personal finances, health, relationships, home and admin, learning, side projects, communications. Make clear these are only examples.
2. For each area the user picks, create a workstation following 00_Resources/Workstation Setup Guide.md: a folder with a CLAUDE.md and a MEMORY.md, nothing else until it is needed.
3. Add a row to the Routing Map for each new workstation, describing when to route there in the user's own words.
4. Do not create a workstation the user did not ask for, and do not pre-populate content inside one. Start empty and let it fill in through use.

---

## Preferences

*Starter section. As you discover how the user likes to work (tone, response length, formatting habits, how they want choices presented), note it here. This file ships with no assumptions about that.*

---

## Rules

*Starter section, for standing behavioral rules the user states directly ("always," "never," "before X do Y"). This file ships with none. Add them here as they come up, and apply the two placement tests above to decide whether something belongs here or in MEMORY.md.*

---

## Governance: MECE Principle

All instructions, rules, and context in this workspace should be mutually exclusive and collectively exhaustive: every rule lives in exactly one place. No duplication across this file, MEMORY.md, or workstation files.

- **This file (CLAUDE.md)** owns: workspace identity, routing, and behavior rules.
- **MEMORY.md** owns: cross-cutting facts that accumulate over time (decisions, preferences, status).
- **00_Reference/** owns: detailed, stable reference material and governance mechanics, loaded on demand.
- **00_Resources/** owns: supporting material loaded on demand, such as setup guides and templates.
- **Workstation CLAUDE.md files** own: domain-specific identity and workflow. They layer on top of this file and never restate it.
- **Workstation MEMORY.md files** own: domain-specific facts and decisions.
- **ARCHIVE.md** owns: the permanent historical record of completed work, the Workspace Changelog. Never read at session start, only pulled up on demand.
- **00_Skills/** owns: the record of what skills exist on your Claude account, and the archived source of the custom ones. It is a register and a recovery path, never a live skill directory; invoking a skill always uses the account copy.

When adding a new rule, decide where it belongs using the two tests in the Memory System section. If unsure, ask.

---

## Routing Map

*Add a row here for every workstation you create. Cowork checks this table to decide which workstation folder to load for a given task.*

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
| 00_Resources/Workstation Setup Guide.md | Creating a new workstation |
| 00_Skills/Skills Inventory.md | Closing out a session (points to the session-audit skill), or understanding how account skills are archived in this workspace |
