---
name: set-goals
description: >
  Use when the user says "set my goals," "review my goals," "quarterly review," "plan my year," "plan my quarter," or names something they want to achieve this year. Turns a few big goals into something the week can act on: each goal gets a target date, a measurable milestone for this quarter, the obstacle most likely to get in the way with an if-then plan for it, and a next action in the right workstation. It writes them to the Goals section of root MEMORY.md in a fixed form the dashboard, start-my-day and plan-my-week read. At a quarter's end it scores each milestone honestly with the user, logs the result in ARCHIVE.md, and sets the next. It keeps the list short, proposes rather than decides, and writes only what the user approves.
---

# Set Goals

Most goals fail in the gap between "this year" and "this week". A yearly goal is too far away to act on, so the week fills with whatever is urgent instead. This skill closes the gap: each goal is cut into a milestone for the current quarter, the milestone feeds the week's focus in plan-my-week, and the week's focus becomes tasks.

It draws on three well-tested ideas. Specific, challenging goals tend to be reached more often than "do your best" goals. Cutting a year into shorter stretches, as OKRs and the 12 Week Year do, makes the deadline close enough to feel. And naming the obstacle in advance, with an if-then plan for it, helps people keep going when it shows up.

This skill owns the Goals section. Root CLAUDE.md owns the memory rules and the task format. The plan-my-week skill owns the week. Read those where the steps below point to them.

## The Goals section

Goals live in the Goals section of root MEMORY.md, in exactly this form, so the dashboard and the other skills can read them:

```
- [YYYY-MM-DD] Goal: [result] (by YYYY-MM-DD; [Workstation])
  - Quarter: [measurable milestone] (by YYYY-MM-DD)
  - If-then: If [obstacle], I will [response].
```

The date in brackets is when the goal was set. The Goal line names a result, not an activity: "Run a half marathon", not "Run more". The Quarter line is what will be true at the end of this quarter, and someone else could check it: "Run 10 km without stopping", not "Train regularly". The If-then line is optional. The workstation is the area the goal belongs to; leave it out only if no workstation fits.

Keep three goals or fewer at a time, and never more than five. More than that, and none of them gets the time it needs. A goal with a finished end belongs here; an ongoing area of life is a workstation, and a single piece of work with a near end is an Active Project.

## Setting goals

### Step 1: Read what is there

Read root MEMORY.md in full: Goals, Active Projects and Core Memory, which may still hold goals from setup written as plain entries. Read the Next Actions of the workstations the goals belong to. Use today's date in the user's time zone from Core Memory.

### Step 2: Ask

Ask, in one message, what the user most wants to be true by the end of the year, or by a date they choose. If they already have goals recorded, start from those instead and ask whether they still hold.

### Step 3: Shape each goal

For each goal, propose, and let the user change:

1. **The result**, worded as something finished, with a target date.
2. **This quarter's milestone:** the part that would put them on track by the quarter's last day. Make it measurable. If the quarter has less than four weeks left, set the milestone for the end of next quarter instead, and say so.
3. **The obstacle:** ask "What is most likely to get in the way?" and turn the answer into an if-then plan, such as "If work runs late on a run day, I will run before breakfast the next morning."
4. **The next action:** the first concrete step, as a task in the workstation's Next Actions, in the task form from root CLAUDE.md, with a due date if there is a natural one.

If the user names more than five goals, ask which three matter most this quarter. Keep the others as a one-line note under Open Items in root MEMORY.md, "Goals parked for later: ...", so nothing is lost.

### Step 4: Write, on a yes

Show the Goals section as it would read, and write it on a yes, replacing what was there. Move any goal found in Core Memory into Goals in the same step, and remove the old entry, so each goal lives in one place. Add the next-action tasks. Then say in one line where everything went.

## The quarterly review

Run this when the user asks for a quarterly review, or offer it once, in one line, when a session starts and a Quarter line's date has passed. Keep it to about fifteen minutes.

1. **Score each milestone with the user:** done, partly done, or not done. Ask what helped and what got in the way, one line each. Score honestly; a missed milestone is information about the plan, not about the person.
2. **Log it.** Add one line to ARCHIVE.md for the quarter, under the current month and week headings in the form ARCHIVE.md shows, starting "Quarterly review", such as "Quarterly review: 10 km without stopping done; savings milestone partly done (two of three months)." This is bookkeeping under the memory rules.
3. **Decide each goal:** keep it with a new milestone, change it, or drop it on purpose. A goal dropped is a decision, so it goes in the ARCHIVE line too.
4. **Set the next quarter's milestones** and next actions, as in Step 3 of setting goals, and write them on a yes.

## Linking goals to the week

Goals do no work on their own. The plan-my-week skill chooses focus outcomes from the Quarter lines, start-my-day offers a next step for any goal with no open task in its workstation, and the weekly review checks that every goal has one. If a goal has had no open task for two weeks, say so in one line the next time this skill runs, and ask whether it still matters.

## What this deliberately does not do

It does not invent goals, decide what the user should want, or add goals to make the list look complete. It does not track habits day by day or score the user. It does not break a goal into a full project plan; that is an Active Project, proposed in one line if the goal clearly needs one.
