# Changelog

All notable changes to this template are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

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
