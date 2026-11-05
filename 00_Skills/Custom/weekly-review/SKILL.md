---
name: weekly-review
description: >
  Use when the user says "weekly review," "review my week," "tidy the workspace," or "workspace check-up." Also offer it once, without running it, when a session starts and the last review recorded in root MEMORY.md is more than about seven days old. It is a 20 to 30 minute upkeep ritual for a CoworkOS-style workspace. It files what is sitting in 98_Temp, asks about each Open Item, flags quiet or finished Active Projects, checks MEMORY.md files for stale or conflicting entries and size, and looks for drift such as broken routing rows, missing files and rules written in two places. Every change is proposed first and only what the user approves is applied. It ends with one ARCHIVE.md line, a short report and one suggestion for the coming week. It does not reorganise the workspace, add structure or rewrite rules.
---

# Weekly Review

A workspace stays useful only if someone tidies it. Files pile up in 98_Temp. Open Items sit untouched for months. A project finishes and nobody moves it to ARCHIVE.md. A rule gets written in a second place and the two copies drift apart. None of this breaks anything on the day it happens, so nobody notices until a session acts on something stale.

This skill is a short, fixed check-up that catches those things once a week. It takes 20 to 30 minutes. It looks, proposes, and applies only what the user approves.

This skill owns the review procedure only. Root CLAUDE.md owns routing and the memory rules. `00_Reference/Memory System.md` owns entry format, archiving and size ceilings. `00_Reference/File Creation Rules.md` owns placement, naming and the approval rules for moving or deleting files. `00_Reference/Governance Rules.md` owns backups and the MECE principle. Read those where the steps below point to them.

## When to offer it

Run it when the user asks with any of the trigger phrases.

Also offer it once at the start of a session when the last review is more than about seven days old. The date comes from the "Weekly review" entry under Scheduled Tasks in root MEMORY.md, which every session already reads, so ARCHIVE.md stays out of session-start reading. If there is no such entry yet, offer it once the workspace has at least one workstation.

Offer it in one line, such as "It has been about ten days since the last weekly review. Want to run it now?" Then carry on with whatever the user asked. Do not offer it again in the same session, and do not start it without a yes.

## Before you start

If the workspace syncs to GitHub, follow the sync check in the Routing Protocol of root CLAUDE.md before changing anything. If the remote has commits this copy has not seen, stop and say so.

Take today's date from the user's own time zone. Many AI tools run on a server clock set to UTC, which can put you on the wrong day. If the time zone is not recorded in Core Memory in root MEMORY.md, ask once and propose saving it there.

Tell the user the plan in two lines: the eight steps below, and that nothing changes without their yes. Then begin.

## Step 1: Load the workspace

Read these files, each one in full:

1. Root CLAUDE.md and root MEMORY.md.
2. The CLAUDE.md and MEMORY.md of every workstation. A workstation is a top-level folder that holds a CLAUDE.md, plus any sub-workstation one level inside it. Folders starting with `00_`, `98_` or `99_` are not workstations.

These files can run long. If a tool cuts off a read or says the output is too large, read the file in parts until you reach the end. Never review a file you only partly read, because you will miss the stale line that needed replacing.

State the files you loaded before moving on.

## Step 2: File what is in 98_Temp

List every file in `98_Temp/` except its own index file, `98_Temp.md`. For each one, read its opening and propose one of two homes: the workstation it belongs to, or `99_Archive/` if it is no longer current. Give the file name, its date prefix, and one line on what it holds and why that home fits.

Present the whole list at once so the user can answer in one reply. Move only what they approve.

A move is a rename, so follow rule 13 in File Creation Rules: search the workspace for references to the old path first, and update them in the same pass. A file moving to `99_Archive/` keeps its original name, and anything important gets one line in ARCHIVE.md, as `99_Archive/99_Archive.md` says.

Never delete a file here. If the user wants one gone, follow rule 11 in File Creation Rules: show its path and a one-sentence description, and wait for an explicit yes.

If 98_Temp is empty, say so in one line and move on.

## Step 3: Decide each Open Item

Open Items in root MEMORY.md are things deferred on purpose. They are only useful if someone decides about them now and then. For each entry, quote it and ask the user to pick one:

- **Act now.** Do it during this review if it is quick, or name it as the suggestion for the coming week in Step 8.
- **Keep.** Leave it as it is. If its reason has changed, propose the new wording.
- **Drop on purpose.** Remove it, because deciding not to do it also resolves it.

Remove an entry only after the user picks "drop" or the thing is done. Workstation MEMORY.md files may have their own deferred items. Treat those the same way.

## Step 4: Check Active Projects

Each Active Projects entry in root MEMORY.md carries the date it was last active. Compare that date with today.

- **Quiet projects.** Flag any project not active in about two weeks. Ask whether it is still active, paused, or finished. If it is still active, propose an updated status line.
- **Finished projects.** Propose moving each finished project to ARCHIVE.md, under the right month and week, in the format `00_Reference/Memory System.md` describes. Then remove it from Active Projects.

Updating Active Projects and writing to ARCHIVE.md are operational bookkeeping under Memory System, so they need no memory-write approval. Still say what you are about to change before you change it, since the user is deciding which projects are finished.

## Step 5: Memory hygiene

Go through root MEMORY.md and every workstation MEMORY.md looking for two kinds of problem.

- **Contradictions.** Two entries that cannot both be true, or a memory entry that conflicts with a rule in a CLAUDE.md file.
- **Stale entries.** An entry that describes a state that has clearly moved on, such as a status from months ago or a decision a later entry reversed.

For each one, quote the current text exactly as it appears, name the file and section, and propose a replacement or a removal. Never add a second entry next to a stale one. When two entries conflict, say plainly what conflicts and ask which is right, as root CLAUDE.md requires.

Then check size. Count the lines in root MEMORY.md and in each workstation MEMORY.md, and compare each count with its ceiling in the Size Ceilings section of Memory System. For any file over its ceiling, propose the fix that section describes: compress verbose entries to the two-sentence cap first, then move entries that are no longer current to ARCHIVE.md. If a file is still over after both, flag it for a decision. Never raise a ceiling.

Memory edits need approval like any other memory write.

## Step 6: Drift check

Look for places where the workspace no longer matches itself. Report each finding with the exact file and line, and propose a fix.

- **Routing Map rows pointing nowhere.** A row in the Routing Map of root CLAUDE.md whose workstation folder does not exist.
- **Workstations with no row.** A workstation folder found in Step 1 that has no Routing Map row, so no session will ever route to it.
- **References to missing files.** A path named in any file loaded in Step 1, or in the Memory & Governance table of root CLAUDE.md, that does not exist on disk.
- **The same rule in two places.** A rule written in more than one file, which breaks the MECE principle in root CLAUDE.md. Propose keeping it in the one place it belongs, using the placement tests in root CLAUDE.md, and removing the other copy.
- **Old handoffs.** If `00_Resources/Chat Context Index.md` exists, any row marked Active whose date is more than about a month old. Ask whether the work is finished. If so, propose marking it Closed in both the index row and the handoff file header, as the chat-context skill describes.

If nothing turns up, say "No drift found" and move on.

## Applying approved changes

Apply only what the user approved: all, some, or none. Silence is not approval.

**Back up first when many files will change.** If the approved changes touch more than a handful of files, copy every file that will change into `.backups/YYYY-MM-DD-weekly-review/` before the first edit, as Governance Rules requires. Name that path in the report.

**Edit in place.** Change only the text being replaced, with an edit method that checks the old text was found exactly once. Never retype a whole file from what a tool showed you, because tool output can be cut short and the rest of the file would be lost.

**Confirm it landed.** Re-read the changed part of each file and check the new text is there.

You can apply changes at the end of each step or in one batch at the end. Ask the user which they prefer if it is not clear.

## Step 7: Log the review

Two small records, both operational bookkeeping under Memory System, so neither needs approval.

First, in root MEMORY.md under Scheduled Tasks, add or update one entry: "Weekly review, root, weekly, last run [YYYY-MM-DD]". This is the date the next session checks before offering the review.

Second, add one line to ARCHIVE.md.

Place it under the current month heading and the current week heading, most recent first. If this week already has a heading, use it. Otherwise add one dated the Monday of this week, in the format ARCHIVE.md shows. Use today's date in the user's time zone.

Start the line with "Weekly review" so the next session can find it. Keep it to the two-sentence cap. For example:

```
- [YYYY-MM-DD] Weekly review: 3 files filed from 98_Temp, 1 Open Item dropped, 1 project moved to the archive, 2 stale entries replaced. No drift found.
```

Log the review in both places even if nothing changed, since the date is what the next offer checks.

## Step 8: Report and suggest

End with a short report of five lines or fewer:

- What changed, grouped by step, with counts.
- Every file created, modified or moved, with its full path.
- The backup folder, if one was made.
- Anything left undecided, carried to next week.

Then give one suggestion for the coming week, in one sentence. Pick the single thing that would help most, such as an Open Item the user chose to act on, a quiet project worth one hour, or a recurring drift worth a rule. Give only one.

Close with one short line pointing to the dashboard, using the name in Core Memory ("Dashboard name: ...") if there is one, for example: "Your workspace health is also on Basecamp: double-click Dashboard.html in your workspace folder." One line only. If the user has said they do not want this reminder, it will be recorded in Core Memory, so skip it.

If the workspace syncs to GitHub, suggest running the session-audit skill (`00_Skills/Custom/session-audit/SKILL.md`) next, so the changes reach the remote.

## Keeping it to 20 to 30 minutes

The review is worth running only if it stays short enough to run every week. If a step turns up a long list, handle the most important items and carry the rest to next week. Say how many were carried. A long list in one step is itself a finding worth one line in the report.

Do not stop to research or fix something large during the review. Name it, and let the user decide whether it becomes its own task.

## What this deliberately does not do

It does not reorganise folders, rename workstations or change how the workspace is laid out. It does not create new structure, such as a new workstation, a new section or a new reference file. It does not rewrite rules in any CLAUDE.md beyond removing a duplicate the user approved. It does not run session-audit or sync to GitHub.

Each of those is a real piece of work that deserves its own session. Folding them into a weekly ritual is how a 20 minute check-up becomes a chore nobody wants to start.
