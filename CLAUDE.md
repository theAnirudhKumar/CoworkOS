# CLAUDE.md

This is a workstation-based AI workspace: each folder under the root represents one area of life or work, with its own identity, workflow, and accumulated context. It was designed and tested against Claude Cowork, but nothing about this file's format is Claude-specific; read this file at the start of every session, whichever AI tool is reading it. See 00_Resources/Using CoworkOS with Other AI Tools.md for notes on other tools.

---

## Memory System

At the start of every session: read MEMORY.md before responding. Use what you find to inform your work, without announcing it.

Memory writes require approval. Propose an entry when something memory-worthy happens, but never write to MEMORY.md without confirmation first. Entries can also be triggered directly: phrases like "remember this," "make a note," "from now on," or "always."

All memory entries are persistent. They stay in MEMORY.md until the user asks to remove or change them.

Flag contradictions. If a new instruction conflicts with an existing memory entry, do not silently overwrite it. Say what conflicts and ask how to reconcile it.

Full mechanics (capture triggers, entry format, archiving) are in 00_Reference/Memory System.md.

At the end of a session, run the session-audit skill (00_Skills/Custom/session-audit/SKILL.md) rather than relying on memory writes caught mid-conversation. It scans the whole session for corrections, preferences, and decisions that were never written down, proposes where each belongs, and applies only what is approved. This is what keeps this file and MEMORY.md actually current instead of slowly drifting stale.

**Where things go.** Apply two tests when deciding where to save something. Test 1: does it prescribe behavior (look for "always," "never," "before doing X, do Y")? If so, it belongs in this file, under the right section. Test 2: does it describe a fact about the world that could change (status, a decision, a preference, something the user asked to be remembered)? If so, it belongs in MEMORY.md. When neither test clearly applies, say which file seems right and ask for confirmation before writing.

---

## Routing Protocol

Before starting any task, identify the relevant workstation from the Routing Map below, read its CLAUDE.md and MEMORY.md, and state which files were loaded before responding.

### First-time setup

Run this the first time this workspace is used. On a fresh copy of this template the Routing Map below already has one row in it, the shipped Example Workstation sample: treat that as empty for this purpose, since no real workstation exists yet. Bootstrapping the workspace this way does not need a workstation identified first the way the Routing Protocol above otherwise requires, since none exists yet; that requirement applies once at least one real workstation has been created.

Say up front, once, that this setup can be paused at any point and picked up again later: nothing here has to happen in one sitting. Any step answered with a clear no, such as declining GitHub sync outright, is a settled decision and needs no log. Any step put off rather than decided, "not now," "later," "skip this for now," or left alone when offered, gets logged in root MEMORY.md's Open Items section (see 00_Reference/Memory System.md) with a one-line note on what is lost by leaving it that way, so a deferred step stays visible instead of quietly disappearing. Apply this the same way to every step below, including the GitHub sync question, not only the ones that call it out by name.

0. If this AI tool is not Claude Cowork, read 00_Resources/Using CoworkOS with Other AI Tools.md before anything else, including whether this tool works from a stable folder at all. If where these files were saved is at all unclear, ask now, before creating anything, and confirm the answer back so it is on record.
1. Offer the full Starter Workstations list below, not a short handful of examples. Show each area's name and its one-line gist, in order, and ask which ones to remove, if any, rather than asking the user to generate a list from nothing: most people default to two or three areas when asked to name their own, which undersells what this system is for. Make clear they can also add an area that is not on the list, rename any of these, or remove as many as they want, down to zero. Whatever is left after removals is what step 2 creates.
2. For each area kept, create a workstation following 00_Resources/Workstation Setup Guide.md: a folder with a CLAUDE.md and a MEMORY.md, nothing else until it is needed. If the area is one of the Starter Workstations below, write its Identity paragraph from that area's gist and covers list, what routes here and what does not. MEMORY.md still starts genuinely empty either way, per step 4.
3. Add a row to the Routing Map for each new workstation, describing when to route there in the user's own words.
4. Do not create a workstation the user did not ask for, and do not pre-populate content inside one. Start empty and let it fill in through use.
5. Offer, right here rather than leaving it to be discovered later, to rename or delete Example Workstation now that real workstations exist, and to remove its row from the Routing Map. If the user would rather leave it for now, that is fine, per the deferral rule above.
6. Ask whether the user wants this workspace synced to a GitHub repository they own. This is optional and off by default; explain the reason briefly, mainly reaching the workspace from a phone or another device while away from the primary computer, and point to 00_Resources/GitHub Sync Guide.md if they say yes. Do not set this up without an explicit yes.
7. Offer, do not wait to be asked, to set up the skills this template ships archived copies of (00_Skills/Skills Inventory.md), starting with session-audit since first-time setup already leaned on the memory system it maintains. What "set up" means depends on whether this AI tool has a real installable-skill mechanism at all; if it does, attempt it directly rather than only describing how; if it does not, or you are not sure, say so plainly and explain how the workspace still gets the same behavior without a formal install, by reading the SKILL.md file directly when triggered. Either way, this step actually happens now, not only when the user thinks to ask about skills.
8. Offer a short, clearly skippable round of questions about how the user wants written output to sound (tone, formality, anything they already know they dislike), and save what they give you to 00_Resources/voice-principles.md. Three questions at most. If they would rather skip it and let this fill in through use instead, that is a completely fine answer, per the deferral rule above, not something to push further on.

### Starter Workstations

This is what step 1 offers. It exists so a first-time user is choosing from a real, complete list rather than inventing one from a blank page, since most people default to two or three areas when asked to name their own. It is a starting menu, not a ceiling: anyone can add an area not listed here, rename any of these, or remove as many as they want. Sub-items listed under "Covers" are what each area typically holds, not workstations of their own; use them to write the new workstation's Identity paragraph in step 2, not as a checklist to fill in.

1. **Self.** Who you are, underneath every other area. Covers: identity, values, preferences, principles, vision, personal operating system.
2. **Career.** Where your career is headed, across jobs. Covers: career direction, skills, opportunities, professional development. Does not cover the current job's day to day, that is Work.
3. **Work.** Your current job. Covers: current company, role, team, projects, meetings, processes. Does not cover long-term career direction, that is Career.
4. **Finances.** Money in, money out, and the recurring obligations around it. Covers: income, expenses, investments, taxes, financial goals, insurance, subscriptions, renewals.
5. **Home.** Where you live and what it takes to run it. Covers: housing, household, purchases, renting, maintenance.
6. **Relationships.** The people in your life. Covers: family, friends, partner, network.
7. **Health and Wellbeing.** Body and mind. Covers: exercise, nutrition, sleep, healthcare, habits, medical. "Habits" here means health routines specifically, sleep, exercise, eating; a general productivity habit belongs in Personal Growth instead.
8. **Learning.** What you are studying or building knowledge on. Covers: books, courses, research, notes, skills, knowledge.
9. **Projects.** Things you are building or experimenting with outside of work. Covers: personal projects, AI projects, experiments.
10. **Content and Personal Brand.** What you publish and how you show up publicly. Covers: LinkedIn, Instagram, writing, content ideas.
11. **Personal Growth.** How you are actively working on yourself. Covers: self improvement, productivity, habits. "Habits" here means productivity and self-improvement routines; a health routine belongs in Health and Wellbeing instead.
12. **Travel and Experiences.** Where you have been and where you want to go. Covers: trips, places, experiences, bucket list.
13. **Interests.** What you follow for its own sake, not for work or growth. Covers: AI, technology, hobbies, media.
14. **Personal Admin.** The paperwork and errands. Covers: documents, legal, personal tasks, chores.
15. **Life Planning.** The long view. Covers: goals, long-term vision, major decisions, future plans.

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
- **00_Resources/** owns: supporting material loaded on demand, such as setup guides, templates, the tool-compatibility notes, and the GitHub sync guide.
- **Workstation CLAUDE.md files** own: domain-specific identity and workflow. They layer on top of this file and never restate it.
- **Workstation MEMORY.md files** own: domain-specific facts and decisions.
- **ARCHIVE.md** owns: the permanent historical record of completed work, the Workspace Changelog. Never read at session start, only pulled up on demand.
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
| 00_Resources/Workstation Setup Guide.md | Creating a new workstation |
| 00_Skills/Skills Inventory.md | Closing out a session (points to the session-audit skill), or understanding how account skills are archived in this workspace |
| 00_Resources/Using CoworkOS with Other AI Tools.md | Running this workspace on an AI tool other than Claude Cowork |
| 00_Resources/GitHub Sync Guide.md | Setting up the optional GitHub sync, or understanding what it involves before agreeing to it |
| 00_Resources/Troubleshooting.md | Setup or installation isn't going the way this file describes |
