---
name: start-my-day
description: >
  Use when the user says "start my day," "what's on today," "morning brief," "what needs my attention," or "plan my day." Builds a short daily brief from the workspace files: Active Projects, Open Items, Scheduled Tasks and Goals in root MEMORY.md, open tasks and due dates in each workstation's Next Actions, the quick-capture inbox, the living sections of each workstation MEMORY.md, and Active handoffs in the Chat Context Index if it exists. If the AI tool has connected sources such as a calendar, an email connector or a task manager, it reads them and says which it used. It never sends, accepts, declines or changes anything in them. The brief is about 12 lines: today's fixed commitments, the top three things worth doing and why, what is waiting on the user, what is coming up, and anything stale. Every item names its source, and nothing is invented. On a scheduled or unattended run it writes the brief to a dated file and sends nothing.
---

# Start My Day

A short brief at the start of the day saves the first half hour of working out what matters. The workspace already holds most of what is needed: active projects, deferred items, scheduled tasks and the user's goals. This skill reads those, adds what connected sources show for today, and turns it into about twelve lines.

The brief only reports what is already written down somewhere. It never makes up a task, and every line says where it came from.

This skill owns the brief only. Root CLAUDE.md owns routing and the memory rules. `00_Reference/File Creation Rules.md` owns where a saved brief goes and how it is named. Read those where the steps below point to them.

## Step 1: Fix the date

"Today" means today in the user's own time zone. Many AI tools run on a server clock set to UTC, which can be a day ahead or behind. Look for the time zone in Core Memory in root MEMORY.md. If it is not there, ask once, and propose saving it to Core Memory. Saving it needs the user's approval, like any memory write.

Use the date and weekday in that time zone for everything below.

## Step 2: Read the workspace

Read each of these in full:

1. Root MEMORY.md. The sections that matter here are Active Projects, Goals, This Week, Open Items, Scheduled Tasks and Core Memory, especially the planning style ("Planning style: ...") recorded there.
2. The MEMORY.md of every workstation. A workstation is a top-level folder that holds a CLAUDE.md, plus any sub-workstation one level inside it. Read its Next Actions first: every open task (`- [ ]`) and its due date, if it has one. Then the other living sections, such as people, key dates and decisions.
3. `98_Temp/Inbox.md` and `98_Temp/Phone Inbox.md`, only to count the lines waiting there.
4. `00_Resources/Chat Context Index.md`, if it exists. Note each row marked Active, since that is unfinished work the user may want to pick up.

If a tool cuts off a read, read the file in parts until you reach the end. An item below the cut-off point is still real.

## Step 3: Read connected sources, read-only

Check which sources the AI tool has connected in this session. Common ones are a calendar, an email connector and a task manager. Use only what is actually connected. If none are, the brief works from the workspace files alone, and says so.

From each source, read only what the brief needs:

- **A calendar:** today's events with their times, and anything in the next few days that needs preparation.
- **An email connector:** recent threads where someone is waiting for a reply or a decision from the user.
- **A task manager:** tasks due today or overdue, and tasks due in the next few days.

These sources are read-only for this skill. Never send, reply to, accept, decline, reschedule, complete, archive or edit anything in them. Anything that needs a reply goes in the brief under "Waiting on you" for the user to handle.

If the user asks for a draft reply, write it in the conversation. Placing it anywhere else, such as in the email tool's drafts, is a separate request that the user has to make.

## Step 4: Choose what goes in

Every item must trace to a file or a connected source. If you cannot point to where an item came from, leave it out. Never guess at a task the user might have, and never fill a section to make the brief look complete. An empty section says "Nothing found."

**Top three** is the hardest part. Pick the three things most worth doing today. Weigh them roughly in this order:

1. A task that is overdue, or due today or tomorrow, from Next Actions or a connected source.
2. Something another person is waiting on.
3. Something that moves a Quarter milestone in Goals forward.
4. An Active Project that has gone quiet and needs one push to keep moving.

Each item gets one line saying what it is and why it made the list today.

If This Week holds a plan whose span covers today (from its "Week of" date to its last Block line), it comes first: today's Fixed and Block lines go under "Today" with the calendar events, and a Focus outcome scheduled for today is a strong candidate for the top three. If the plan's span has ended, or This Week is empty and it is Monday, add one line offering the plan-my-week skill.

Shape the top three to the planning style, as its section in `00_Resources/Planning Methods.md` describes: the frog first for Eat the frog, the day as 1, 3 and 5 for 1-3-5, the four groups for Eisenhower. With no style recorded, use the order above.

In the first weeks, there may be fewer than three real items. Do not invent any. Instead, if a goal or an Active Project has no open task, add one line after the brief offering to set its next step, for example: "Your 10k goal has no next step yet. Want to add one?" Write the task only on a yes.

**Stale** is one line for the most useful thing that looks forgotten. Examples are an Active Project not active in about two weeks, an Open Item that has sat for a month, or an Active handoff that nobody has touched. If several look stale, and the last weekly review is more than about seven days old, suggest the weekly-review skill in this line.

## Step 5: Write the brief

Keep it to about twelve lines. Use this shape:

```
**[Weekday, date]**. Sources: workspace files, [connected sources used, or "no connected sources"].

**Today**
- [time] [commitment] (calendar)

**Top three**
1. [Item]: [why today] ([source])
2. [Item]: [why today] ([source])
3. [Item]: [why today] ([source])

**Waiting on you**
- [Reply or decision owed, and to whom] ([source])

**Coming up**
- [Day]: [item] ([source])

**Stale:** [One line] ([source])

[If the inbox is not empty:] [N] quick captures are waiting in your inbox for the weekly review.
```

Sources are a few words each, such as "root MEMORY.md, Open Items", "Finances MEMORY.md", "calendar" or "email". Leave out "Today" when no calendar is connected and This Week has no Fixed or Block lines for today, and say so in the first line.

Then ask one question: whether to start on the first of the top three.

## Step 6: Scheduled or unattended runs

Sometimes this skill runs on a schedule with nobody watching. On those runs:

- **Send nothing to anyone.** No email, no chat message and no notification. The brief goes to a file only.
- **Ask nothing.** Use the time zone recorded in Core Memory. If none is recorded, use the tool's clock and say at the top of the file which time zone it assumed.
- **Write the brief to a dated file.** Name it `YYYY-MM-DD-daily-brief.md`, following the naming rules in File Creation Rules. Put it in the folder the Scheduled Tasks entry for this task names. If no folder is named, put it in `98_Temp/`, since a brief that spans the whole workspace has no clear workstation home. The file opens with the H1 "# Daily Brief [YYYY-MM-DD]".
- **Leave the closing question out.** Nobody is there to answer it.

If the user asks to set this up as a scheduled task, record it under Scheduled Tasks in root MEMORY.md, with the details Memory System asks for, including where the briefs are saved. That entry is operational bookkeeping and needs no approval. Check the tool's own list of scheduled tasks first, so the same brief is not set up twice.

## A soft nudge to the dashboard

After the brief, add one short line pointing to the dashboard, using the name in Core Memory ("Dashboard name: ...") if there is one. For example: "All of this is also on Basecamp: double-click Dashboard.html in your workspace folder." Keep it to one line, put it after the closing question, and leave it out on an unattended run. If the user has said they do not want this reminder, it will be recorded in Core Memory, so skip it.

## Rules

### Read-only by default

In a normal run this skill changes no workspace file and nothing in any connected source. The only writes it ever makes are the dated brief file on an unattended run, and a Core Memory or Scheduled Tasks entry the user approved or asked for.

### Short on purpose

The brief is meant to be read in under a minute. If there is more to say, say it after the user picks what to start on. Leave out project background, explanations of the workspace, and any recap of the files read.

### Facts over guesses

If a source fails to load or returns nothing, say so in the first line and carry on with the rest. A brief built from fewer sources is still useful, as long as it names the missing one.

## What this deliberately does not do

It does not change MEMORY.md entries, reorder projects or close Open Items. That is the weekly review's job. It does not reply to messages, accept invitations or move tasks. It does not plan the whole day hour by hour; if the user asks for that, use the plan-my-week skill for today.
