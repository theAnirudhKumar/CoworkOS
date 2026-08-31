# File Creation Rules

*Read before creating any new file in the workspace.*

---

## Routing Rules

Where different types of content belong:

1. **Root level:** CLAUDE.md, MEMORY.md, and an archive file if you keep one. No other files at root.
2. **00_Reference/:** permanent governance and mechanics files, using stable title-case names without date prefixes (for example, `Memory System.md`). These are pointed to by name from CLAUDE.md and should not be renamed casually.
3. **00_Resources/:** supporting resource files loaded on demand, such as templates and setup guides. Stable descriptive names, no date prefixes.
4. **Workstation folders:** each contains a CLAUDE.md and a MEMORY.md. Domain-specific reference or project files live inside the workstation folder, not at root.
5. **Historical records:** if you keep an archive file, all completed work and structural history goes there rather than in separate archive folders scattered around the workspace.

---

## Naming Rules

6. **Date-prefixed naming for outputs.** New output files (reports, drafts, notes, analysis) use the format `YYYY-MM-DD-descriptive-name`.
7. **Stable naming for governance and resource files.** Files in 00_Reference/ and 00_Resources/ use stable title-case names without date prefixes. This is the one exception to rule 6, scoped to those two folders alone.
8. **Workstation file names are fixed.** Every workstation has exactly `CLAUDE.md` and `MEMORY.md`. Never rename these.
9. **No spaces in output file names.** Use hyphens as separators. Files in 00_Reference/ may use spaces to match their pointer names exactly.
10. **Descriptive names only.** A file name should describe its content clearly. Avoid generic names like `notes.md`, `draft.md`, or `temp.md`.

---

## Approval Rules

11. **Deletion requires confirmation.** Before deleting any file, show its path and a one-sentence description of what it contains. Wait for explicit confirmation.
12. **Overwrite requires confirmation.** Before overwriting an existing file, show what is changing, either the diff or a clear summary of it. Wait for explicit confirmation.
13. **Rename requires a reference check first.** Before renaming any file, search the workspace for references to its current name. Show the current name, the new name, and every file that references it. Wait for confirmation.
14. **Splitting a file requires confirmation.** Before splitting one file into two, show the proposed split and which content goes where. Wait for confirmation.

---

## Content Rules

15. **Every markdown file opens with an H1 title.** The first line is `# Title`, or the H1 sits immediately below a YAML frontmatter block if the file has one. Never start with body text or a lower-level heading.
16. **Proper heading hierarchy.** H1 for the file title, H2 for major sections, H3 for subsections. Never skip a level, and never write flat, unstructured notes.
17. **Two-sentence cap for memory entries.** Any entry written to MEMORY.md, or to an archive file, follows the cap: one sentence for the fact or what was done, an optional second sentence for why it matters.
18. **No duplicate content.** Before creating a new file, check whether an existing file already covers the same content. If one does, update it instead of creating a new one.

---

## Workstation Rules

19. **A new workstation needs two files only.** Create the folder with CLAUDE.md and MEMORY.md. Nothing else until the workstation actually needs it.
20. **Workstation CLAUDE.md follows the standard structure.** Sections in order: Identity, Resources, Workflow, Editorial Rules if it produces written output. See 00_Resources/Workstation Setup Guide.md before creating a new one.
21. **Workstation MEMORY.md follows the standard structure.** A short header, then whatever living sections that domain actually needs (contacts, key decisions, active work). Mirror the root MEMORY.md pattern at the workstation level rather than inventing a new shape each time.
22. **A sub-workstation is allowed, one level deep only.** A folder inside a workstation may carry its own CLAUDE.md and MEMORY.md when it represents a distinct domain that does not yet warrant a top-level workstation. It still needs the parent workstation's Resources section to point at its CLAUDE.md, and the Routing Map entry should name the parent and then direct to the sub-workstation. Do not nest a second level.

---

## Placement Verification

23. **Verify routing before creating.** Before creating any new file, confirm: the file type, the correct folder, the correct name format, and whether a similar file already exists. Only create the file once all four checks pass.

---

## Format Rules

24. **Markdown is the default output format.** Create a different format such as a Word document, spreadsheet, or slide deck only when explicitly asked for that format, never as an automatic translation of a generic request, and never because a folder happens to already contain files in that format.
