# Memory System

*Full reference for how memory works in this workspace. The core rules (read MEMORY.md, get approval before writing, flag contradictions) live in root CLAUDE.md. This file holds the detailed mechanics.*

---

**Operational bookkeeping exemption.** Active Projects updates, Scheduled Tasks updates, and entries to an archive or changelog file are not subject to the "memory writes require approval" rule. These are operational bookkeeping, not personal memories, so write them as part of the natural workflow when the triggering event happens.

---

## Archive or Changelog (optional)

If you keep an archive file, treat it as a permanent, append-only log of structural milestones and completed work, organized by month and week with the most recent first, and read on demand rather than at session start. Active Projects in root MEMORY.md gives session-start orientation; the archive is where a completed project's entry moves once it is done.

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

Root MEMORY.md holds two living sections that need upkeep: Active Projects and Scheduled Tasks. They give session-start orientation without needing to read every workstation.

**Active Projects:** track project name, which workstation it belongs to, current status in one or two sentences, and the date it was last active. Remove an entry once the project completes, moving it to an archive file if you keep one.

**Scheduled Tasks:** track task name, workstation, schedule or cadence, what it does, and the date it was created. Mark it paused or retired rather than deleting it outright if it stops running.

---

## Size Ceilings

MEMORY.md files grow silently, and without a limit they degrade performance by consuming context on every session (root) or every workstation visit.

**Root MEMORY.md: 150-line ceiling.** Loaded every session, so bloat here costs the most. Check the line count periodically and compress before it grows unmanageable.

**Workstation MEMORY.md: 200-line ceiling.** Loaded on routing to that workstation, so bloat is scoped but still costly for a frequently visited one.

**Archive files: no ceiling.** Reference-only, loaded on demand.

When a ceiling is breached: compress verbose entries to the two-sentence cap first, then archive entries that are no longer current-state. If still over the ceiling after both steps, flag it for a manual decision rather than raising the limit.
