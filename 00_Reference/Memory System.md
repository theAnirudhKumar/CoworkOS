# Memory System

*Full reference for how memory works in this workspace. The core rules (read MEMORY.md, get approval before writing, flag contradictions) live in root CLAUDE.md. This file holds the detailed mechanics.*

---

**Operational bookkeeping exemption.** Active Projects updates, Scheduled Tasks updates, entries to ARCHIVE.md, lines captured to `98_Temp/Inbox.md`, and tasks in a Next Actions section are not subject to the "memory writes require approval" rule. These are operational bookkeeping, not personal memories, so write them as part of the natural workflow when the triggering event happens.

---

## Archive or Changelog

ARCHIVE.md is a permanent, append-only log of structural milestones and completed work, organized by month and week with the most recent first, and read on demand rather than at session start. Active Projects in root MEMORY.md gives session-start orientation; ARCHIVE.md is where a completed project's entry moves once it is done.

**Format:** one entry per completed item, following the two-sentence cap: first sentence states what was delivered or changed, optional second sentence states why it matters. Older entries are not rewritten retroactively once the cap changes, since an archive is not loaded every session and its length costs nothing at rest.

---

## Capture Triggers

Propose a memory entry when:

1. **A decision is made** that will shape future work: choosing a tool, committing to a format, settling on a strategy, ruling something out. Do not trigger for tentative or exploratory thinking.
2. **A correction or behavioral feedback arrives** in a way likely to recur: "don't do it that way," "always structure it like this." A one-time correction does not qualify; the signal is when it implies a standing preference.
3. **A project reaches a milestone or changes status**: it gets blocked, launches, or wraps.
4. **A new recurring relationship appears**: someone mentioned in a working context who has an ongoing role, not already in memory. Do not trigger for a one-off name mention.
5. **A preference is stated directly**: "always," "never," "from now on," "in the future," "I prefer."
6. **A structural change happens**: a new folder, a reorganized hierarchy, a new scheduled task, a changed domain structure.

**Do not propose an entry for:** one-off task details that will not recur, information already captured elsewhere, temporary states, or anything explicitly called a one-time exception.

---

## Entry Format

- One to two sentences, dated as [YYYY-MM-DD].
- Frame entries as principles with reasoning, not as incident narration. For example: "[YYYY-MM-DD] Client-facing summaries should lead with the outcome, not the process, because that is what gets read first." Not: "The summary format was wrong on this date."
- If a new entry contradicts an existing one, flag the conflict and propose replacing the old entry rather than silently overwriting it.

---

## Root MEMORY.md: Active Tracking

Root MEMORY.md holds six living sections: Active Projects, Goals, This Week, Scheduled Tasks, Open Items, and Core Memory. The first five need upkeep as work moves. They give session-start orientation without needing to read every workstation.

**Active Projects:** a project is a result with an end, such as "kitchen renovated" or "10k race run", rather than an ongoing area of life, which is what a workstation is for. Track the outcome, which workstation it belongs to, the target date if there is one, current status in one or two sentences, and the date it was last active. Its individual tasks live in that workstation's Next Actions. Propose a new project, in one line, whenever work clearly spans more than one session or has several steps toward a dated result, such as a handoff being written for it or a deadline being set. Remove an entry once the project completes, moving it to ARCHIVE.md.

**Goals:** a few results the user wants by a date, each with a measurable milestone for the current quarter and an optional if-then plan, in the form the set-goals skill (`00_Skills/Custom/set-goals/SKILL.md`) sets out. Three goals or fewer at a time, never more than five. Goals are written only on the user's yes, and a goal lives here rather than in Core Memory. A goal's tasks live in its workstation's Next Actions; a quarter's result is logged in ARCHIVE.md.

**This Week:** the current week's plan, in the form the plan-my-week skill (`00_Skills/Custom/plan-my-week/SKILL.md`) sets out: a "Week of" date, then Focus, If-then and Block lines. The user approves the plan before it is written, and it replaces the previous week's plan rather than adding to it, so this section never grows past about fifteen lines. Planning-style and working-hours preferences go in Core Memory, not here.

**Next Actions (in each workstation's MEMORY.md):** the concrete tasks for that area, one per line, in the form `- [ ] What to do (due YYYY-MM-DD)`. Keep each to one line. Mark a finished task `- [x]`; the weekly review removes finished tasks and logs anything worth keeping in ARCHIVE.md. A task list that keeps growing is a sign that something should become a project, or be dropped on purpose.

**Scheduled Tasks:** track task name, workstation, schedule or cadence, what it does, and the date it was created. Mark it paused or retired rather than deleting it outright if it stops running. Also record two facts that are easy to get wrong. First, where the task's instructions live and where its schedule lives, since many tools keep them in different places, so editing one does not change the other. Second, whether it runs only while a particular computer or app is open, or on a server whatever happens. Before creating a new task, check the tool's own list of scheduled tasks, so the same job is not set up twice. A task's instructions are worth keeping in the workspace too, the same way skills are archived in 00_Skills/, so they can be recovered.

**Open Items:** track anything deliberately deferred, not forgotten: a first-run setup step skipped for now, a decision put off, a local fix made to a shipped template file that should be reported as an issue rather than kept as private drift. State what was deferred, why, and what is lost by leaving it that way, so it stays visible instead of silently disappearing. This is where first-run setup should log a step the user chose to skip. Remove an entry once it is resolved, either by acting on it or by deciding on purpose to leave it.

**Core Memory:** durable facts about the user that are not tied to one workstation and are not a project, a task or a deferred item. This is usually where "remember this" lands when no workstation fits. Keep each entry to the two-sentence cap. A fact that belongs to one area of life goes in that workstation's MEMORY.md instead.

---

## Size Ceilings

MEMORY.md files grow silently, and without a limit they degrade performance by consuming context on every session (root) or every workstation visit.

**Root MEMORY.md: 150-line ceiling.** Loaded every session, so bloat here costs the most. Check the line count periodically and compress before it grows unmanageable.

**Workstation MEMORY.md: 200-line ceiling.** Loaded on routing to that workstation, so bloat is scoped but still costly for a frequently visited one.

**ARCHIVE.md: no ceiling.** Reference-only, loaded on demand.

When a ceiling is breached: compress verbose entries to the two-sentence cap first, then archive entries that are no longer current-state. If still over the ceiling after both steps, flag it for a manual decision rather than raising the limit.
