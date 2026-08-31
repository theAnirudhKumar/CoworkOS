# Changelog

All notable changes to this template are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

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
