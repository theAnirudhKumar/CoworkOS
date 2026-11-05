# File Creation Rules

*Read before creating any new file in the workspace.*

---

## Routing Rules

Where different types of content belong:

1. **Root level:** CLAUDE.md, MEMORY.md, ARCHIVE.md, AGENTS.md (a one-line pointer to CLAUDE.md for AI tools that look for that name), and Dashboard.html (a page that shows the workspace in a browser). The template's LICENSE, and the optional `.gitignore` and `.githooks/` for people who use git, also stay. No other files at root.
2. **00_Reference/:** permanent governance and mechanics files, using stable title-case names without date prefixes (for example, `Memory System.md`). These are pointed to by name from CLAUDE.md and should not be renamed casually.
3. **00_Resources/:** supporting resource files loaded on demand, such as templates and setup guides. Stable descriptive names, no date prefixes.
4. **Workstation folders:** each contains a CLAUDE.md and a MEMORY.md. Domain-specific reference or project files live inside the workstation folder, not at root.
5. **Historical records:** all completed work and structural history goes in ARCHIVE.md rather than in separate archive folders scattered around the workspace. Two folders are the only exceptions, and neither is a workstation. `98_Temp/` holds files whose home is not clear yet and is reviewed weekly. `99_Archive/` holds old files the user has confirmed are no longer current. Each folder's own index file says how to use it.

---

## Naming Rules

6. **Date-prefixed naming for outputs.** New output files (reports, drafts, notes, analysis) use the format `YYYY-MM-DD-descriptive-name`.
6a. **A refreshed document keeps its filename.** When a dated document is updated with new information, keep its original name, because other files refer to it by that name. Record the refresh inside the document instead, for example "Date: 2026-07-01, refreshed 2026-07-20". Rename only through rule 13.
7. **Stable naming for governance and resource files.** Files in 00_Reference/ and 00_Resources/ use stable title-case names without date prefixes. This is the one exception to rule 6, scoped to those two folders alone.
8. **Workstation file names are fixed.** Every workstation has exactly `CLAUDE.md` and `MEMORY.md`. Never rename these.
9. **No spaces in output file names.** Use hyphens as separators. Files in 00_Reference/ may use spaces to match their pointer names exactly.
10. **Descriptive names only.** A file name should describe its content clearly. Avoid generic names like `notes.md`, `draft.md`, or `temp.md`.

---

## Approval Rules

11. **Deletion requires confirmation.** Before deleting any file, show its path and a one-sentence description of what it contains. Wait for explicit confirmation.
12. **Overwrite requires confirmation.** Before overwriting an existing file, show what is changing, either the diff or a clear summary of it. Wait for explicit confirmation. This is about changes the user did not ask for, such as rewriting a file, replacing what they wrote, or cutting content. An edit the user just asked for, or adding a line to a list, is already approved by the request; make it and say what changed. One exception: a skill that owns a file and says how to update it, such as a handoff file or an index the skill maintains, may rewrite that file in place. It still says what it changed.
13. **Rename requires a reference check first.** Before renaming any file, search the workspace for references to its current name. Show the current name, the new name, and every file that references it. Wait for confirmation.
14. **Splitting a file requires confirmation.** Before splitting one file into two, show the proposed split and which content goes where. Wait for confirmation.

---

## Content Rules

15. **Every markdown file opens with an H1 title.** The first line is `# Title`, or the H1 sits immediately below a YAML frontmatter block if the file has one. Never start with body text or a lower-level heading.
16. **Proper heading hierarchy.** H1 for the file title, H2 for major sections, H3 for subsections. Never skip a level, and never write flat, unstructured notes.
17. **Two-sentence cap for memory entries.** Any entry written to MEMORY.md or ARCHIVE.md follows the cap: one sentence for the fact or what was done, an optional second sentence for why it matters.
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
25. **Strip workspace-only details before a file goes public.** When a workspace file becomes a public page, a shared document or a file in a public repository, remove anything that only means something inside this workspace: frontmatter, internal links, index footers, workspace paths. The workspace copy keeps them, since they are what make it easy to find things here.
26. **Save the point, not the pile.** When the user shares an article, a document or a long passage to keep, write a short note in `<Workstation>/Resources/`, named `YYYY-MM-DD-topic.md`, never a full copy. It holds four things, in this order: **Why it was saved** (one line, naming the project or area it helps), **Key points** (at most five, written in your own words, with the single most useful one in bold), **Source** (a link or a title and date), and **Use it for** (when a future session should bring it back up). Mark figures and claims as the source's own, such as "the article says", since they were not checked. Add a row for it to the Resources table in that workstation's CLAUDE.md, creating the table if this is the first one, so later sessions can find it without a search. A note nobody would read again should not be saved at all; say so instead. Collecting more than will ever be used is the most common reason a second brain is abandoned.
