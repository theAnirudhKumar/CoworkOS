---
name: plan-my-week
description: >
  Use when the user says "plan my week," "plan the week," "time block my week," "help me plan my calendar," "schedule my week," "block time for this," or "time block my day." Builds a draft plan for the week, or for one day, from the workspace files: Next Actions and due dates in each workstation's MEMORY.md, Active Projects and Goals in root MEMORY.md, and a connected calendar when there is one, read-only. It looks back at last week's plan first, then proposes three focus outcomes, an if-then plan for each, and time blocks with slack, placed around fixed commitments and shaped by the planning style in Core Memory (00_Resources/Planning Methods.md). On a yes, it writes the plan to the This Week section of root MEMORY.md. It creates calendar events only for the blocks the user approves, never with other people invited, and never changes or deletes an existing event. Nothing is invented: every block traces to a task, a project or a goal the user confirmed.
---

# Plan My Week

Knowing what to do is half the job. The other half is knowing when, because a task with no time set aside tends to wait until it is urgent. This skill turns the tasks, projects and goals already in the workspace into a week the user can actually follow, placed around what is already on their calendar.

The plan is a draft. The AI proposes it, the user changes it, and nothing is written or put on a calendar until they say yes.

This skill owns the week plan. `00_Resources/Planning Methods.md` owns the methods and the principles every plan follows. Root CLAUDE.md owns routing and the memory rules. `00_Resources/Connectors Guide.md` owns the safety rules for connected apps. Read those where the steps below point to them.

## Step 1: Set the frame

Use today's date in the user's time zone, from Core Memory in root MEMORY.md. If no time zone is recorded, ask once and propose saving it.

Decide the span. "Plan my week" covers today through Sunday if it is Monday to Wednesday, and the next Monday to Sunday if it is Thursday or later, unless the user names the days. "Time block my day" covers today only, and skips Step 2 and the focus outcomes in Step 4.

Read the planning style from Core Memory ("Planning style: ..."). If none is recorded, use Big Three, and at the end offer once, in one line, to choose a style from `00_Resources/Planning Methods.md`. Read that file's section for the chosen style, and its closing principles, before going further.

## Step 2: Look back at last week

Read the This Week section of root MEMORY.md. If it holds a plan from an earlier week, compare it with what happened:

- Which focus outcomes are done? Check the matching tasks in Next Actions, marked `- [x]` or gone.
- Which blocks were kept, if a calendar is connected and shows them?

Say the result in two lines at most, without judgement, such as "Last week: 2 of 3 focus outcomes done. The proposal took longer than planned, so this week's blocks for writing are longer." If the plan was mostly missed, ask in one line what got in the way, and use the answer when placing this week's blocks.

If This Week is empty or still holds its placeholder, skip this step.

## Step 3: Gather what the week holds

Read each of these in full:

1. Root MEMORY.md: Goals, especially each Quarter milestone, then Active Projects, Open Items and Core Memory.
2. The MEMORY.md of every workstation, Next Actions first: every open task (`- [ ]`), with its due date if it has one.
3. A connected calendar, if there is one, read-only: every event in the span, with its times. Treat these as fixed. If no calendar is connected, ask the user for their fixed commitments in one question ("Anything fixed this week, like meetings, appointments or travel?"), and say once that connecting a calendar would save this step (`00_Resources/Connectors Guide.md`).
4. A connected task manager, if there is one, read-only: tasks due in the span.

Ask in the same question, if Core Memory does not already say, what hours the user likes to work or keep free. Propose saving the answer to Core Memory, such as "Working hours: weekdays 9:00 to 17:30; evenings kept free." Writing it needs their yes.

## Step 4: Draft the plan

**Focus outcomes.** Propose three outcomes for the week, worded as finished results ("proposal sent", "three quotes in hand"), not as activity. Choose them in this order: a task due in the span or overdue; something another person is waiting on; a step that moves a Quarter milestone from Goals, or an Active Project, forward. Try to give every goal some time in the week unless the user chooses otherwise. Each one names its source. If fewer than three real candidates exist, propose fewer, and offer to set a next step for any goal or project that has none. Never invent one.

**If-then plans.** For each focus outcome, write one line saying when and where it will happen, in the form "When [time or situation], I will [action] [where]", such as "When I sit down on Tuesday at 9:00, I will draft the proposal before opening email." Base it on the blocks below.

**Blocks.** Place time for the focus outcomes first, then for other tasks due in the span. Follow these rules:

- **Fixed commitments first.** Never place a block over a calendar event or a commitment the user named.
- **Only inside the hours the user works or keeps open.** If none are recorded, assume weekday working hours and say so.
- **Add slack.** Make each block about half as long again as the task seems to need, and keep part of every day unplanned, so one thing running late does not break the rest. Leave at least a quarter of each working day unblocked.
- **Protect the morning for hard work** if the style is Eat the frog, or the user has said mornings are when they focus.
- **Group small tasks** into one block, such as "Errands and admin".
- **Shape it to the style**, as its section in `00_Resources/Planning Methods.md` describes: one main thing a day for Big Three, a frog first for Eat the frog, a big task each day for 1-3-5, important but not urgent work first for Eisenhower, sizes in sessions for Pomodoro.

Keep the week to the blocks that matter. A plan with every hour filled is a plan that will be abandoned by Wednesday.

## Step 5: Show the draft

Show the plan in this shape, and keep it short:

```
**Week of [Monday's date]**. Style: [style]. Sources: workspace files, [calendar or "no calendar connected"].

**Last week:** [one or two lines, if Step 2 ran]

**Focus**
1. [Outcome] ([source])
   When [time or situation], I will [action] [where].
2. ...

**Blocks**
- Mon [date]: 09:00-11:00 [what] ([focus number or source])
- Tue [date]: ...

**Fixed:** [count] calendar events kept as they are.
**Left unplanned:** [tasks due later, or not this week, in one line]
```

Then ask one question: what to change, or whether to save it. Revise as often as the user wants.

## Step 6: Save and schedule, on a yes

**Save the plan.** On a yes, replace everything under the This Week heading of root MEMORY.md, keeping the heading and its italic guidance line, with the plan in exactly this form, so the dashboard and the daily brief can read it:

```
Week of: YYYY-MM-DD.
- Focus: [outcome] ([workstation])
- If-then: When [time or situation], I will [action] [where].
- Block: YYYY-MM-DD HH:MM-HH:MM [what] ([workstation])
```

The date after "Week of" is the first day of the span. Write one Focus line per outcome, each followed by its If-then line, then one Block line per block, in date order. Times are 24-hour, in the user's time zone. Replace the old plan rather than adding to it; the look back in Step 2 is the only record of last week this skill needs.

**Add tasks that are missing.** If a focus outcome has no matching task in its workstation's Next Actions, add one there in the usual form, with a due date that matches the plan.

**Put blocks on the calendar, only if asked.** If a calendar connector is connected and allows creating events, offer once: "Want these blocks on your calendar?" On a yes, create one event for each block the user approved, titled with what it is for. Follow these rules:

- Create events only. Never move, change, accept, decline or delete an existing event.
- Never invite anyone. An event with guests sends invitations, which needs a separate yes for each one under the Connectors Guide.
- Read the calendar again just before creating the events. If a new event now overlaps a block, skip that block and say so.
- After creating them, list what was created, and ask the user to check it in their calendar app, since a success message from a tool is not proof.

If no calendar is connected, the plan in MEMORY.md and on the dashboard is the plan. Say so in one line.

## Step 7: Close

End with one line naming where the plan lives, using the dashboard's name in Core Memory ("Dashboard name: ...") if there is one, such as "Your week is on Basecamp now: double-click Dashboard.html in your workspace folder." Leave out the line if the user has said they do not want this reminder.

If no planning style was recorded, add one line offering to choose one from `00_Resources/Planning Methods.md`.

## Unattended runs

If this skill runs on a schedule with nobody watching, draft the plan only: write it to `98_Temp/YYYY-MM-DD-week-plan-draft.md`, with the H1 "# Week Plan Draft [YYYY-MM-DD]", and change nothing else. Do not write to MEMORY.md, add tasks or create calendar events. The user reviews the draft in their next session.

## What this deliberately does not do

It does not decide what matters for the user: every focus outcome is a proposal from what is written down. It does not reschedule or delete anything on a calendar, and it does not send invitations. It does not track hours or score the user. It does not replace the weekly review, which tidies the workspace; this plans the time. Run the review first when both are due, since a tidy task list makes a better plan.
