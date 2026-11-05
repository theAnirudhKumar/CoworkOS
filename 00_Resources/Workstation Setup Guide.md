# Workstation Setup Guide

## How to create a new workstation

When creating a new workstation, make a subfolder named for it and add these inside:

### 1. CLAUDE.md

Sections, in this order:

- **Identity.** One paragraph: who you are in this workstation, what routes here, what does not. If this workstation is one of the Starter Workstations listed at the end of this guide, write it from that area's gist and covers list rather than inventing one.
- **Resources.** A table with "Resource" and "Read when..." columns, added the first time the workstation has a reference file worth pointing to. Leave the section out until then, since Governance Rules omits sections with nothing in them.
- **Workflow.** Numbered steps for how work in this area usually goes. A brand-new workstation rarely has any yet, so start with one step, "Ask what the user wants help with in this area, and add steps here as a pattern repeats," rather than inventing a process.
- **Editorial Rules** (only if this workstation produces written output). Domain-specific writing rules that layer on top of the workspace-wide voice guidance in 00_Resources/voice-principles.md.

### 2. MEMORY.md

- A header naming the workstation.
- Three living sections every workstation starts with: **Next Actions** (tasks for this area, one per line, as `- [ ] What to do (due YYYY-MM-DD)`), **People** (who matters here and their role, such as a manager, a doctor or a contractor), and **Key Decisions** (choices made in this area, with the reason). Add others only when the area needs them.
- Write the three headings with no entries yet. The daily brief, the weekly review and the dashboard look for these exact names.
- Populate it over time as work happens. Do not write it manually up front.

### 3. A Resources subfolder, when needed

`<Workstation>/Resources/` holds notes saved for later in this area, such as a distilled article or a summary of a document. Create it the first time something needs to go in it, and follow rule 26 in 00_Reference/File Creation Rules.md for what a saved note looks like.

## After creating the workstation

Add a row to the Routing Map in root CLAUDE.md, describing when to route here in plain language, so future sessions load it automatically.

## Starter Workstations

A menu of common life areas. First-run setup offers the whole list so a first-time user is choosing from a real, complete menu rather than inventing one from a blank page, since most people default to two or three areas when asked to name their own. It stays here afterward so a new area added later can start from the same gists. It is a starting menu, not a ceiling: anyone can add an area not listed here, rename any of these, or remove as many as they want. Sub-items listed under "Covers" are what each area typically holds, not workstations of their own; use them to write the new workstation's Identity paragraph, not as a checklist to fill in.

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
