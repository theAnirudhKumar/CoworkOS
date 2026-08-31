# Skills Inventory

A register of the skills your AI tool's account actually has, plus an archived recovery copy of the ones you built yourself. The "skill" concept as a named, invokable, account-level file is specific to a handful of tools, Claude Cowork among them (see 00_Resources/Using CoworkOS with Other AI Tools.md); if your tool has no equivalent, treat the files in Custom/ as plain reference documentation instead.

## Why this folder exists, and what it is not

A skill runs from your Claude account, not from a file in this workspace. Nothing in this folder is read by Claude as a live skill; invoking a skill always uses the account copy, the same way any other Claude session would. So why keep a copy here at all? Because the account is the only place the live version exists, and if it is ever lost, edited by accident, or you switch machines, there is nothing to recover it from unless a copy also lives somewhere durable. This folder is that recovery path, and this file is the index of what should be in it.

**The rule:** when you create or meaningfully change a custom skill on your account, copy its source into `Custom/` in the same session. If you are archiving someone else's skill rather than one you wrote, it goes in `Third-Party/` instead, with its original LICENSE and README kept alongside it.

**Turning one of these files into an actual, invokable skill is a separate step from having the file**, and the exact mechanics vary by tool and change over time, so this file will not try to keep pace with a specific tool's UI. The reliable move: ask your AI tool directly, in your own words, to read the file and set it up as a skill. It knows its own current steps better than any doc can.

## Inventory

| Skill | Type | Archived at | Notes |
| :--- | :--- | :--- | :--- |
| session-audit | Custom | `Custom/session-audit/SKILL.md` | End-of-session capture and sync. See its own file for what it does. |
| travel-mode | Custom | `Custom/travel-mode/SKILL.md` | Working from the GitHub copy when the primary computer is unreachable. Requires the optional GitHub sync (00_Resources/GitHub Sync Guide.md). |

Add a row here every time you archive a skill, so this table stays a true index rather than a folder someone has to browse to understand.

## Custom/

Skills you wrote yourself, archived here as the recovery source if the account copy is ever lost or found to have drifted from what is here.

## Third-Party/

Skills someone else wrote that you use, kept with their original LICENSE and README. Before recording anything here as usable, check what its license actually permits; an MIT license, for example, requires the original copyright notice to travel with it.
