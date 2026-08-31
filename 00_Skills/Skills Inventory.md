# Skills Inventory

A register of the skills your Claude account actually has, plus an archived recovery copy of the ones you built yourself.

## Why this folder exists, and what it is not

A skill runs from your Claude account, not from a file in this workspace. Nothing in this folder is read by Claude as a live skill; invoking a skill always uses the account copy, the same way any other Claude session would. So why keep a copy here at all? Because the account is the only place the live version exists, and if it is ever lost, edited by accident, or you switch machines, there is nothing to recover it from unless a copy also lives somewhere durable. This folder is that recovery path, and this file is the index of what should be in it.

**The rule:** when you create or meaningfully change a custom skill on your account, copy its source into `Custom/` in the same session. If you are archiving someone else's skill rather than one you wrote, it goes in `Third-Party/` instead, with its original LICENSE and README kept alongside it.

## Inventory

| Skill | Type | Archived at | Notes |
| :--- | :--- | :--- | :--- |
| session-audit | Custom | `Custom/session-audit/SKILL.md` | End-of-session capture and sync. See its own file for what it does. |

Add a row here every time you archive a skill, so this table stays a true index rather than a folder someone has to browse to understand.

## Custom/

Skills you wrote yourself, archived here as the recovery source if the account copy is ever lost or found to have drifted from what is here.

## Third-Party/

Skills someone else wrote that you use, kept with their original LICENSE and README. Before recording anything here as usable, check what its license actually permits; an MIT license, for example, requires the original copyright notice to travel with it.
