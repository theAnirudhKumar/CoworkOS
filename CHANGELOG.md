# Changelog

All notable changes to this template are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- Capture: "jot this down" appends a dated line to a new `98_Temp/Inbox.md` straight away, and the weekly review empties it.
- Tasks: every workstation's MEMORY.md has a Next Actions section with tasks written as `- [ ] What to do (due YYYY-MM-DD)`. The daily brief puts overdue and due-soon tasks first, the weekly review clears finished ones and faces overdue ones, and the dashboard lists them across all areas with a tick box.
- Recall: before answering about the user's own past, the AI searches the whole workspace, names the file it found, and says plainly when nothing was recorded.
- File Creation Rule 26: a saved article becomes a short note in `<Workstation>/Resources/` (why it was saved, at most five key points, source, use it for), never a full copy. The example workstation ships one.
- A Skills table in root CLAUDE.md maps trigger phrases to skill files, so skills work in every session even where the AI tool cannot install them.
- Setup offers a Quick pace (essentials now, the rest when it first helps), asks which areas to keep, and leads the rules menu with five recommended rules.
- Dashboard: Next actions and Inbox cards with tick-to-complete and quick capture; "Deferred" replaces "Waiting on you"; dates and greeting follow the time zone in Core Memory.

### Changed
- An explicit "remember this" is saved straight away and confirmed in one line; only memories the AI suggests still wait for a yes.
- The "files loaded" note is one short line and can be switched off. Session-audit is offered when the user signals they are done. The first weekly review is offered a week after setup, not in the next session.
- Workstations start with Next Actions, People and Key Decisions; Resources tables and Workflow steps are no longer invented up front.
- Weekly review looks for untracked work and proposes projects for it; Memory System says when work should become a project.
- Rule clarifications: an edit the user asked for counts as confirmed; Starter Rules is a menu, so copied rules do not count as duplicates; the root-files rule names LICENSE and the git files.

### Fixed
- References that pointed at files removed during setup (README, CONTRIBUTING, validate.py).
- Skills listed in the Skills table can be used without being installed; root CLAUDE.md, Governance Rules and the Skills Inventory no longer say otherwise.
- The weekly review is offered at session start, because root CLAUDE.md now tells every session to check its date. Setup records "set up [date], not run yet", and the dashboard shows when the first review is due.
- The capture format is stated exactly (`- [YYYY-MM-DD] the thought`), so every capture reaches the dashboard.
- The weekly review asks about setup leftovers in one question instead of one at a time, every week.
- Setup is exempt from the CLAUDE.md change log; the other-tools guide no longer points at the deleted README; saved notes get a Resources table row; the daily brief offers a next step for goals that have none instead of padding; the dashboard never shows a negative "days ago".
- The example workstation's Resources table pointed at a file that did not exist.


### Changed
- README rewritten around what CoworkOS is to the person using it, an AI second brain: a one-line promise, a dashboard screenshot, the quick start, a "See it in action" section with illustrations of setup, the folder and a daily brief, what you get day to day, how it works, the skills, and the details folded away below. Light and dark images live in `.github/assets/`, which setup removes along with the rest of `.github/`.
- Root `CLAUDE.md`, `SETUP.md` and the dashboard's welcome screen now describe the workspace as the user's AI second brain.
- Dashboard: "1 file in 98_Temp needs a home" reads correctly, and dates in square brackets show without the brackets.


### Added
- `Dashboard.html` at the workspace root: open it in a browser, choose the workspace folder once, and see a dashboard of active projects, open items, scheduled tasks, memory size, workstations, handoffs and workspace health, plus a tree of every file, search and a reader. In Chrome and Edge it can edit any file and mark open items done, checking first that the file has not changed on disk. Light, dark or system theme. Runs locally with nothing to install and no outside requests.
- The dashboard carries a name the user chooses, saved as `Dashboard name:` in Core Memory. First-run setup has a new step 11 that introduces the dashboard and offers names (Atlas, Basecamp, Compass, Mission Control, North Star, Headquarters, The Desk, or the user's own). The about-me step now records `Name:` and `Time zone:` in a fixed form the dashboard reads. The hand-over is now step 12.
- `start-my-day` and `weekly-review` end with a one-line nudge to the dashboard, by its name.
- Troubleshooting covers a dashboard that will not save or shows an old file.

## [1.3.0] - 2026-11-05

Three habits that make the workspace a second brain you keep using: a weekly review, a daily brief and turning repeated work into skills. Plus an about-me step in setup and a guide to connecting your other apps safely.

### Added
- `weekly-review` skill: a 20 to 30 minute upkeep that files `98_Temp`, decides each Open Item, flags quiet or finished projects, checks memory for stale entries and size, and looks for drift. Offered once at session start when the last review, recorded under Scheduled Tasks in root `MEMORY.md`, is over a week old.
- `start-my-day` skill: a brief of about 12 lines from the workspace files, plus any connected calendar, email or task tool used read-only. Every item names its source, and an unattended run writes a dated file and sends nothing.
- `make-a-skill` skill: turns a repeated piece of work into a reusable skill, archived in `00_Skills/Custom/` with an inventory row. Governance Rules now offers it once when the same kind of work is asked for a third time.
- `00_Resources/Connectors Guide.md`: what a connector is, which to add first, eight safety rules, and how to record which connectors are in use.
- First-run setup step 1: a short, skippable "about me" round (name, time zone, what the user does, this year's goals) saved to Core Memory on approval. Later steps are renumbered.

## [1.2.0] - 2026-11-05

New skills for handing off chats and keeping requests lean, a much stronger session audit, and the structure and rules a workspace needs once it is used every day.

### Added
- `chat-context` skill: hands a long chat off to a fresh one through a structured handoff file in the workstation's `Chat Context/` folder, registered in `00_Resources/Chat Context Index.md`, and resumes from it in the next chat.
- `optimize-tokens` skill: flags requests that will cost far more than they need to and suggests a leaner version, with quality gates so published output is never cut.

- `00_Reference/Visual Standards.md`: rules for step-by-step instructions, tables, screenshots, diagrams and headings, and a check to render any generated PDF, Word file or deck before delivering it.
- `validate.py` checks that a skill's description stays under 1,024 characters and its SKILL.md under 500 lines.
- Troubleshooting covers three git traps: an ignore rule does not untrack a tracked file, a lock file must be confirmed stale before deleting it, and a finished command is not proof a push landed.
- `00_Resources/Starter Rules.md`: an optional menu of 31 working rules that held up in daily use, plus a plain-language writing list. First-run setup offers it in a new step 9, and nothing in it applies until the user picks it. The hand-over step is now step 10.
- `AGENTS.md` at the root, a one-line pointer to `CLAUDE.md` for AI tools that read that file. File Creation Rule 1 now allows it.
- `98_Temp/` for files with no clear home yet, reviewed weekly, and `99_Archive/` for old files the user confirms are no longer current. They are the only exceptions to File Creation Rule 5, and neither is a workstation.
- `00_Reference/CLAUDE.md Change Log.md`: the format and the substantive-or-mechanical test for recording changes to root `CLAUDE.md`.
- A Core Memory section in root `MEMORY.md` for lasting facts that belong to no single workstation.
- File Creation Rules 6a (a refreshed document keeps its filename) and 25 (strip workspace-only details before a file goes public), and an exception to rule 12 for files a skill owns.

### Fixed
- `.gitignore` matched `ssn` anywhere in a filename, so ordinary files such as `classnotes.md` were silently left out of git. It now matches only `ssn` as a separate word. Python caches, per-computer AI tool settings and agent worktrees are now ignored too.

### Changed
- Root `CLAUDE.md`: loading context is never shortened because a task looks small; a start-of-session freshness check when GitHub sync is on; more memory trigger phrases; table rows for the change log and voice-principles.
- Governance Rules: a backup into `.backups/` before editing more than a handful of files, and a rule to write instruction files in plain words.
- Memory System: Scheduled Tasks now records where a task's instructions and schedule live and whether it needs a particular computer to be on.
- `session-audit` now reads every file in full before filtering, counts the AI's own breach of an existing rule as a correction, quotes the stale line when a finding replaces an entry, checks root MEMORY.md against its line ceiling, checks that no other session is mid-write before writing or committing, backs up each file before editing, and dates entries in the user's own time zone. Its sync step gained a commit message format, a report format, identity-guard handling, a failure table and stronger safety rules.
- `travel-mode` accepts the token in the trigger message, handles refused pushes and degraded mode more clearly, checks every turn that nothing lives only in the chat, runs `chat-context` before close-out when the session carried a lot of thinking, and never tells the user to change a setting nobody has checked exists.

## [1.1.0] - 2026-09-25

Setup now hands over a clean workspace, and offers a full starter menu of life areas.

### Fixed
- A workspace set up on someone else's computer still carried the template author's material after setup: the full first-run script and Starter Workstations list in `CLAUDE.md`, the template's README, CHANGELOG, CONTRIBUTING, `validate.py` and `.github/`, placeholder example entries, and, for a git clone, the template's history and a remote pointing back at this repository, which session-audit's sync step would have tried to push to. Found by testing an install on a second person's machine.

### Changed
- First-run setup moved out of `CLAUDE.md` into a new root `SETUP.md`. `CLAUDE.md` keeps only a short pointer: if `SETUP.md` exists, setup is unfinished. `SETUP.md` ends with a hand-over step that removes the template-maintainer files, clears example entries, removes a template git remote and offers to drop the template's history, then deletes itself. `LICENSE` is kept, as the license requires.
- The Starter Workstations list moved from `CLAUDE.md` to `00_Resources/Workstation Setup Guide.md`, so it survives setup and is still there when adding an area later.
- `session-audit` refuses to push to a remote that is the CoworkOS template repository, and the GitHub Sync Guide checks for a template clone before `git init`.
- Docs that stay in an installed workspace (`Troubleshooting.md`, `GitHub Sync Guide.md`, `Using CoworkOS with Other AI Tools.md`) no longer point at README sections that setup now removes. `Troubleshooting.md` gains the cleanup request for workspaces set up before this change.

### Added
- A Starter Workstations list of 15 common life areas built directly into root `CLAUDE.md`, each with a one-line gist and what it covers. First-run setup now offers the full list and asks what to remove, instead of asking the user to invent areas from a blank page, since most people default to two or three when asked to name their own. Sub-items are not sub-workstations; they seed the Identity paragraph of whichever areas are kept. `00_Resources/Workstation Setup Guide.md` and `README.md` updated to match. No folders are created in the repo itself, only at install time for whatever the user keeps.

## [1.0.0] - 2026-09-01

First public release. Round-1 installer hardening and round-3 fixes from a real dogfood run, folded together.

### Fixed
- The install prompt in README never asked where to save the workspace, so a session-scoped AI tool could bury it somewhere the user could not find again. It now asks explicitly and confirms the exact path back before creating anything.
- `session-audit`'s description and its sync step read as if GitHub sync was expected or required. Found by a real user hitting exactly this confusion. Reworded so the local save is stated as always happening, and syncing is explicitly a bonus step that only runs if a git remote already exists.
- First-run setup in `CLAUDE.md` used to stop after the GitHub-sync question. It now also reads the multi-tool doc first on a non-Claude tool, offers to clean up `Example Workstation` immediately instead of leaving it for later, proactively offers to set up skills rather than waiting to be asked, and offers a short, skippable round of questions for `00_Resources/voice-principles.md`.
- `validate.py`'s "Open"+"AI" collision check flagged its own new, correct content: this template's compatibility doc has to name real AI companies, OpenAI included, to be useful. Removed; the other checks still run.

### Added
- An Open Items section in root `MEMORY.md` (and documented in `00_Reference/Memory System.md`) for anything deliberately deferred: a skipped setup step, a local fix an AI tool made to a shipped file that should be reported upstream. First-run setup now logs to it instead of silently dropping a skipped step.
- A real Codex section in `00_Resources/Using CoworkOS with Other AI Tools.md`, distinguishing Codex CLI (persistent folder, auto-reads its own `AGENTS.md`, real local skills via `.agents/skills/` and `$skill-installer`) from Codex in the ChatGPT web app (per-task cloud sandbox, undocumented persistence, the surface that actually surfaced the folder-placement bug above). Also a general "session-scoped sandbox" category and a one-time check for any tool that might be one, not just a Codex-specific note.
- A line in `CONTRIBUTING.md` asking users to report it as an issue when their AI tool patches a shipped file locally to work around confusing wording, rather than only fixing their own copy.

## [0.5.0] - 2026-08-31

### Fixed
- `CLAUDE.md`'s first-run setup trigger no longer implies the Routing Map must be empty before bootstrapping can start; it now says plainly to treat the shipped `Example Workstation` row as empty for that purpose.
- README's manual "by hand" install path now covers getting the files without git (GitHub's Download ZIP) and points to your AI tool for connecting a local folder, instead of assuming git and prior tool setup.
- `00_Resources/GitHub Sync Guide.md` no longer tells people they don't need to know git and then hands them six raw shell commands with no terminal instructions. The tested path (handing the guide to your AI tool) is now primary; typing the commands yourself is secondary, with a pointer to where a terminal actually is on Mac, Windows, and Linux.

### Added
- Concrete skill-install guidance in the README and `00_Skills/Skills Inventory.md`: what to actually say to your AI tool to turn an archived `SKILL.md` file into something you can invoke, since having the file was never the same as having a working skill.
- `00_Resources/Troubleshooting.md`, covering the problems people hit most often during install and first-run setup, found by actually running the install flow rather than guessing at it.

## [0.4.0] - 2026-08-31

### Added
- `CONTRIBUTING.md` describing how to propose changes to this repository through an issue and a pull request.
- Multi-tool support notes (`00_Resources/Using CoworkOS with Other AI Tools.md`) for running this template on AI tools other than Claude Cowork.
- Optional GitHub sync, off by default, offered once during first-run setup, with `00_Resources/GitHub Sync Guide.md` covering setup.
- Travel mode skill (`00_Skills/Custom/travel-mode/SKILL.md`) for working from the GitHub copy of a workspace away from your primary computer.

## [0.3.0] - 2026-08-31

### Added
- `ARCHIVE.md`, the permanent historical record for completed work.
- `00_Resources/voice-principles.md`, a starter file for how written output should sound.
- The identity guard: `.gitignore` and `.githooks/pre-commit`, scanning commits for the shape of government ID and financial account numbers before they land in git history.
- `00_Skills/Skills Inventory.md` and the `00_Skills/Custom/` and `00_Skills/Third-Party/` registry structure.
- `Example Workstation/`, a filled-in sample workstation.

## [0.2.0] - 2026-08-31

### Added
- The session-audit skill (`00_Skills/Custom/session-audit/SKILL.md`), which scans a session for uncaptured corrections, preferences, and decisions before it ends, and syncs the workspace to GitHub as its last step when one is configured.
- README and `CLAUDE.md` documentation for running it.

## [0.1.0] - 2026-08-31

### Added
- Initial template: root `CLAUDE.md`, `MEMORY.md`, routing protocol, memory system, and the MECE governance rule.
