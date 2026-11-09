# Skills Inventory

A register of the skills your AI tool's account actually has, plus an archived recovery copy of the ones you built yourself. The "skill" concept as a named, invokable, account-level file is specific to a handful of tools, Claude Cowork among them (see 00_Resources/Using CoworkOS with Other AI Tools.md); if your tool has no equivalent, treat the files in Custom/ as plain reference documentation instead.

## Why this folder exists, and what it is not

Where your AI tool has a skill installed, the installed copy is the one that runs. Where it does not, the Skills table in root CLAUDE.md sends the AI to the file in this folder, and it follows that file directly. Either way, this folder matters: the account copy is the only other place a skill lives. So why keep a copy here at all? Because the account is the only place the live version exists, and if it is ever lost, edited by accident, or you switch machines, there is nothing to recover it from unless a copy also lives somewhere durable. This folder is that recovery path, and this file is the index of what should be in it.

**The rule:** when you create or meaningfully change a custom skill on your account, copy its source into `Custom/` in the same session. If you are archiving someone else's skill rather than one you wrote, it goes in `Third-Party/` instead, with its original LICENSE and README kept alongside it.

**Turning one of these files into an actual, invokable skill is a separate step from having the file**, and the exact mechanics vary by tool and change over time, so this file will not try to keep pace with a specific tool's UI. The reliable move: ask your AI tool directly, in your own words, to read the file and set it up as a skill. It knows its own current steps better than any doc can. This is also not a step to leave until you happen to think of it; first-run setup (SETUP.md, while it still exists) offers it proactively, and it should actually be attempted then, not only described.

Codex CLI specifically has a documented, literal answer rather than only "ask your tool": skills load from `.agents/skills/` in the repository or `~/.agents/skills/` for your account, and `$skill-installer` can fetch curated ones. See the Codex row in 00_Resources/Using CoworkOS with Other AI Tools.md.

## Inventory

| Skill | Type | Archived at | Notes |
| :--- | :--- | :--- | :--- |
| session-audit | Custom | `Custom/session-audit/SKILL.md` | End-of-session capture and sync. See its own file for what it does. |
| travel-mode | Custom | `Custom/travel-mode/SKILL.md` | Working from the GitHub copy when the primary computer is unreachable. Requires the optional GitHub sync (00_Resources/GitHub Sync Guide.md). |
| chat-context | Custom | `Custom/chat-context/SKILL.md` | Hands a long chat off to a fresh one through a structured handoff file, and resumes from it. Keeps its index at `00_Resources/Chat Context Index.md`. |
| weekly-review | Custom | `Custom/weekly-review/SKILL.md` | A 20 to 30 minute weekly upkeep: files 98_Temp, decides Open Items, archives finished projects, checks memory size and drift. |
| start-my-day | Custom | `Custom/start-my-day/SKILL.md` | A short daily brief from workspace files, plus any connected calendar, email or task tool, read-only. |
| plan-my-week | Custom | `Custom/plan-my-week/SKILL.md` | A draft week plan: three focus outcomes, if-then plans and time blocks around the calendar, in the user's planning style. Writes This Week in root MEMORY.md and creates calendar events only on a yes. |
| notion-sync | Custom | `Custom/notion-sync/SKILL.md` | Builds a Notion Command Center from the workspace files and carries changes both ways on request, never deleting and never touching other Notion pages. |
| wrap-up-my-day | Custom | `Custom/wrap-up-my-day/SKILL.md` | A five-minute end-of-day routine: ticks off what got done, moves or drops the rest, captures loose thoughts, and sets tomorrow's first thing. |
| set-goals | Custom | `Custom/set-goals/SKILL.md` | A few yearly goals, each with a measurable quarter milestone, an if-then plan for the likely obstacle and a next action; plus the quarterly review. Writes the Goals section of root MEMORY.md. |
| make-a-skill | Custom | `Custom/make-a-skill/SKILL.md` | Turns a repeated piece of work into a reusable skill, archived here with an inventory row. |
| optimize-tokens | Custom | `Custom/optimize-tokens/SKILL.md` | Spots requests that cost far more than they need to, and suggests a leaner version without lowering quality. |

Add a row here every time you archive a skill, so this table stays a true index rather than a folder someone has to browse to understand.

## Custom/

Skills you wrote yourself, archived here as the recovery source if the account copy is ever lost or found to have drifted from what is here.

## Third-Party/

Skills someone else wrote that you use, kept with their original LICENSE and README. Before recording anything here as usable, check what its license actually permits; an MIT license, for example, requires the original copyright notice to travel with it.
