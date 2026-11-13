# CLAUDE.md Change Log

*A permanent record of every substantive change to root CLAUDE.md. Read it when you are about to change root CLAUDE.md, or when you need to know why a rule says what it says. It is never read at session start.*

Root CLAUDE.md is read first in every session, so one careless line changes how every future session behaves, and nobody reads the file again closely enough to notice. This log is how a change stays visible after the session that made it is gone.

---

## Which changes need an entry

A change is substantive when it adds, removes or reverses a rule, changes routing (a new workstation row, a changed route), changes which file owns something, or changes an approval step. Every substantive change gets an entry here, written in the same session as the change.

A change is mechanical when it fixes a typo or formatting, updates a path after a confirmed rename, reorders text without changing meaning, or shortens wording while keeping every rule. Mechanical changes need no entry.

When unsure, treat the change as substantive.

Before a substantive change, copy root CLAUDE.md into `.backups/YYYY-MM-DD-<short-name>/` so the previous version can be restored. If the workspace syncs to GitHub, a substantive change can also go through an issue and a pull request, with this log entry in the same commit, so there is a diff to read before it lands. That part is optional.

---

## Entry format

Newest entry first. Never delete or rewrite an old entry; add a new one that corrects it.

```
## [YYYY-MM-DD] Short name of the change

**Added / Changed / Removed:** which section, and the wording itself,
quoted, so the change can be found and undone.

**Why:** what happened or what was asked for that made this necessary.

**Scope:** what the change covers, and what it deliberately does not.

**Backup:** the .backups/ path holding the previous version.
```

---

## Entries

## [2026-11-13] Rulebooks table and Global Conventions folder

**Added:** a "Rulebooks" subsection under the Routing Protocol, with a table of tool, rulebook and when to read it. A line in the 00_Reference/ entry of the MECE list saying its Global Conventions folder holds one rulebook per connected tool. A row in the Memory & Governance table for 00_Reference/Global Conventions/Global Conventions.md.

**Why:** rules for each connected tool were heading for root CLAUDE.md, which every session reads in full. A separate rulebook per tool keeps root CLAUDE.md short and loads only what a task needs.

**Scope:** the structure only. The one rulebook shipped is a sample that the user replaces. It does not change any existing rule.

**Backup:** none, since the change went through a pull request with a diff (issue #64).
