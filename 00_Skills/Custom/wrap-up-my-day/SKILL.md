---
name: wrap-up-my-day
description: >
  Use when the user says "wrap up my day," "shut down for the day," "end my day," "close out the day," or "what's left for tomorrow." A five-minute end-of-day routine built on the workspace files. It reads today's tasks and due dates from each workstation's Next Actions, today's blocks from the This Week section of root MEMORY.md, and a connected calendar when there is one, read-only. It ticks off what the user says got done, gives every unfinished task or block a new day or drops it on purpose, captures loose thoughts to the inbox, and makes sure tomorrow's first thing is a task due tomorrow, so the next daily brief leads with it. It changes only what the user confirms, never touches a calendar, and ends by offering the session audit if anything was decided today.
---

# Wrap Up My Day

A day without an ending leaks into the evening. Finished tasks stay unticked, unfinished ones quietly slide past their dates, and the next morning starts with working out where things stood. Five minutes at the end of the day fixes all three, and makes tomorrow's daily brief accurate.

This skill owns the end-of-day routine. Root CLAUDE.md owns the task and capture formats and the memory rules. The plan-my-week skill (`00_Skills/Custom/plan-my-week/SKILL.md`) owns the form of the This Week section. Read those where the steps below point to them.

Keep it short. The whole routine is a handful of questions, asked together where possible, and should take about five minutes.

## Step 1: Fix the date

Use today's date in the user's time zone, from Core Memory in root MEMORY.md. If the time is after midnight but the user is clearly ending the previous day, ask once which day they are wrapping up.

## Step 2: Gather today

Read:

1. Every workstation's Next Actions: open tasks due today or overdue, and tasks marked `- [x]`, so you know what is already ticked.
2. The This Week section of root MEMORY.md: today's Block lines and the Focus lines, if the plan's span covers today.
3. Today's top three from the daily brief, if start-my-day ran in this session, or from today's `YYYY-MM-DD-daily-brief.md` file if one exists. These are often the most important things to ask about, such as the day's frog.
4. A connected calendar, if there is one, read-only: what is on it tomorrow, so the first thing tomorrow fits around it.

## Step 3: What got done

Show the open items from Step 2 in one short list, without repeats: today's top three, then today's blocks, then tasks due today, then overdue tasks. Ask one question: "Which of these got done?" The user can answer in a few words, such as "the first two" or "all but the report."

Mark each finished task `- [x]` in its workstation's Next Actions. Tasks are bookkeeping under the memory rules, and the user just confirmed them, so no further approval is needed. A block that got done needs no change; it stays in the plan as a record for next week's look back.

If the user mentions something they finished that was never a task, it needs no entry. If it was part of an Active Project, update that project's status line and date in root MEMORY.md, which is bookkeeping too.

## Step 4: What did not

For each unfinished item, propose one of three things, in one list the user can answer in one reply:

- **Move it.** A new day, most often tomorrow or the next free day in the plan. For a task, change its `(due YYYY-MM-DD)` date. For a block, change the date and time in its Block line in This Week, and only to a day that still has room. Keep the two in step: when a task moves, move any Block line for the same work to a day on or before its new due date, and when a block moves past a task's due date, move the due date too.
- **Drop it.** Some things no longer matter. Remove the task, or the block, on purpose. Dropping is a real choice, not a failure.
- **Leave it.** Keep it as it is, for an item with no real deadline.

Do not move the same task again and again without saying so. If a task has already been moved more than twice, say so in one line and ask whether it should be broken into a smaller first step, handed to someone else, or dropped.

Moving a block changes the plan, not the calendar. If blocks were put on a connected calendar, say which ones the user may want to move there, and leave the calendar alone.

## Step 5: Empty your head

Ask once: "Anything on your mind to jot down before you stop?" Append each thought to `98_Temp/Inbox.md` in the capture form from root CLAUDE.md, one line each. Do not file them now; the weekly review does that.

## Step 6: Tomorrow's first thing

Propose the one task to start with tomorrow, chosen in this order: something due tomorrow or overdue; a Focus outcome from This Week that has a block tomorrow; the next step of a quarter milestone in the Goals section of root MEMORY.md. If the planning style in Core Memory is Eat the frog, choose the hardest of these. Fit it around tomorrow's calendar if one is connected.

On a yes, make sure it exists as a task due tomorrow in the right workstation's Next Actions, adding one or changing the due date as needed. The daily brief puts tasks due today first, so tomorrow it leads.

## Step 7: Close

Give a three-line summary at most: how many things were done, what moved and where, and tomorrow's first thing. Name nothing that did not change.

If anything was decided, corrected or written this session beyond these task updates, offer the session-audit skill (`00_Skills/Custom/session-audit/SKILL.md`) in one line, as root CLAUDE.md asks at the end of a session.

## What this deliberately does not do

It does not judge the day, score the user or count hours. It does not reschedule, accept, decline or delete anything on a calendar. It does not file the inbox, clear finished tasks or tidy the workspace; the weekly review does that. It does not plan the rest of the week; if most of the plan has slipped, it offers the plan-my-week skill in one line instead of patching day by day.
