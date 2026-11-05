---
name: chat-context
description: >
  Use when the user says "hand off this chat," "save chat context," "wrap this chat," "I'm moving to a new chat," or "write the handoff" (handoff mode), or "resume," "pick up where we left off," "load chat context," or "continue from the last chat" (resume mode). Carries the state of one chat into the next so the user can start a fresh chat without re-explaining anything. Handoff writes a structured context file into the workstation's Chat Context folder and registers it in a rolling index. Resume reads the matching handoff and the files it names, says what was loaded, then continues the work. Use this in place of summarising a chat back to the user in conversation.
---

# Chat Context

Long chats get slow and costly, because every new message carries the whole conversation with it. This skill lets the user close a chat and open a fresh one without losing anything. It writes a structured context file at the end of a session and reads it back at the start of the next one.

This skill owns the handoff procedure only. Root CLAUDE.md owns routing, and 00_Reference/File Creation Rules.md owns placement and naming. Read those where the steps below point to them.

This skill also owns two kinds of file: the handoff files in each workstation's Chat Context folder, and the index at `00_Resources/Chat Context Index.md`. Because it owns them, it may rewrite them in place without the usual overwrite confirmation from File Creation Rules. Each time it does, it says what changed.

---

## Mode A: Handoff

Handoff mode runs when the user signals the chat is ending. Write the file the first time they ask, and do not offer a conversational summary in its place.

### Step A1: Pick the workstation

Read the Routing Map in root CLAUDE.md and pick the workstation this chat belongs to. If the chat spanned more than one, pick the one where most of the work happened and name the others under Context Loaded. If no workstation fits, ask the user where the handoff should live. Tell the user which workstation you picked before writing.

### Step A2: Create the folder if needed

Handoffs live in `<Workstation>/Chat Context/`. Create that folder the first time a workstation needs it, and never ahead of time.

### Step A3: Write the handoff file

Name the file `YYYY-MM-DD-<topic-of-the-work>.md`, using today's date and hyphens in place of spaces. The topic describes the work itself. For example, `2026-03-14-spring-trip-itinerary.md` is a good name, and `2026-03-14-chat-handoff.md` is a poor one.

If a handoff on the same topic already exists, refresh that file in place and add a line inside it noting the refresh and its date. Keep its filename, since the index and other files refer to it by name. Two handoffs on one topic would make the next chat read the wrong one.

Use this structure exactly. Keep every section, and write "None" where a section has nothing in it.

```markdown
# Chat Context: [Topic]

**Workstation:** [Name]
**Date:** [YYYY-MM-DD]
**Status:** Active

---

## Goal

One line on what this thread of work is trying to achieve.

## Current State

Two or three sentences on where things stand, written so a reader with
no prior context knows what exists and what does not.

## Decisions Made

- Each decision, with its reason in one clause.

## Open Questions and Blockers

- What is unresolved, and who or what it is waiting on.

## Files Created or Modified

| File | Path | What it holds |
| :--- | :--- | :--- |

## Rejected Approaches

- What was considered and dropped, and why. This stops the next chat
  from proposing it again.

## Approved Wording

Copy, headlines or phrasing the user signed off on, quoted verbatim.

## Context Loaded

Files read during this session that the next chat should read again,
with full paths.

## Next Action

One sentence naming the single next step, specific enough to act on
without asking a question first.
```

### Step A4: Register it in the index

The index lives at `00_Resources/Chat Context Index.md`. If it does not exist yet, create it with the H1 "# Chat Context Index", one line explaining that it lists every chat handoff in the workspace, and this table:

```markdown
| Date | Workstation | Topic | File | Status |
| :--- | :--- | :--- | :--- | :--- |
```

Add one row per new handoff, with the newest row at the bottom. Status is Active, Superseded or Closed. A refresh from Step A3 edits that file's existing row with the new date and leaves the status as it was. It never adds a second row, because two rows pointing at one file would leave a later resume guessing between them.

The index is a rolling register, so it keeps its name and never takes a date prefix, the same as other files in 00_Resources.

When a handoff's work is finished, mark it Closed in both the index row and the file header. Never delete a handoff file, since the trail is part of its value.

### Step A5: Give the opener and confirm

End by printing one line the user can paste into the next chat:

> Resume the [topic] handoff in [Workstation].

Then confirm the full path of the file written or refreshed, and the index row added or edited.

---

## Mode B: Resume

Resume mode runs at the start of a new chat. Read the index before anything else in that message, including before answering any question the user asked alongside it. This is the one place the usual routing order in root CLAUDE.md bends: the handoff names the workstation, so read it first, then load that workstation's files as Step B3 says.

### Step B1: Find the handoff

Read `00_Resources/Chat Context Index.md`. If the user named a topic or a workstation, match on that. If they said only "resume," take the latest row with status Active. If two rows could match, ask which one they mean. If the index does not exist or no row matches, say so plainly and ask what they want to pick up.

### Step B2: Read the handoff

Read the handoff file in full, rather than skipping ahead to the Next Action.

### Step B3: Read the workstation files

Read the CLAUDE.md and MEMORY.md of the workstation named in the handoff. Then read every file listed under Context Loaded.

### Step B4: Report and ask

In three lines or fewer, tell the user which handoff was read, which files were loaded, and what the recorded Next Action is. Then ask whether to continue with that action or something else. This is the only place where a recap belongs, so keep it short.

---

## Rules

### What goes in a handoff

A handoff holds decisions, current state, blockers, file paths, rejected approaches and approved wording. Write it for a reader with zero context. Use full file paths every time, never a phrase like "the file we made." Name the people or things the work is waiting on.

### What stays out

Leave out the transcript and any blow-by-blow of the conversation. Leave out anything already recorded in root MEMORY.md or a workstation MEMORY.md, and point to that file instead, so each fact lives in one place. Leave out reasoning that led nowhere and changed nothing.

### Size

Keep a handoff under 120 lines. If it runs longer, move the detail into a workstation file and link to it from the handoff.

### Relationship to MEMORY.md

A handoff is session state, so it needs no approval to write and it never goes into MEMORY.md. Some findings outlast the thread of work, such as a decision with lasting effect or a new working convention. Propose those separately as memory entries, following the memory rules in root CLAUDE.md, and wait for approval. When both apply, do both.

### When to skip

If the chat was short and nothing was decided, say so and skip the file. If the user wants a summary to read now, that is a different request, and a handoff is the wrong tool for it.
