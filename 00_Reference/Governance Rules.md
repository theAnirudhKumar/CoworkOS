# Governance Rules

*Read before modifying any CLAUDE.md file, adding a new section, or deciding where a rule or fact belongs.*

---

## Section Ordering

CLAUDE.md files should follow a consistent section order. Sections that do not apply to a given file are omitted entirely, never left as empty headers.

**Root CLAUDE.md order:**

1. Workspace identity paragraph (no heading, just prose)
2. Memory System
3. Routing Protocol
4. Preferences
5. Rules
6. Governance: MECE Principle
7. Routing Map
8. Memory & Governance

**Workstation CLAUDE.md order:**

1. Identity
2. Resources
3. Workflow
4. Editorial Rules (if the workstation produces written output)

Do not add sections outside this order. If a new kind of section is genuinely needed, decide where it fits in the hierarchy and update this file.

---

## Skills Rule

Use a skill when it provides a specialized, reusable workflow that improves the output. Do not invoke a skill for a one-off task where its structure adds no value. When a skill is clearly relevant, invoke it before generating a response, not after.

Only invoke skills that are actually available in the current session.

---

## Size Cap

Size caps protect context window performance. They are hard limits: never raise them, only enforce them.

- Root MEMORY.md: 150 lines
- Workstation MEMORY.md: 200 lines
- Any archive file: no cap (reference-only, never loaded at session start)

When a file exceeds its cap: compress verbose entries to the two-sentence maximum first, then archive entries that are no longer current-state. If still over cap after both steps, flag it rather than raising the limit.

---

## Workstation Sizing

A workstation is the right size when its CLAUDE.md and MEMORY.md can be read in full without meaningful token cost. Signs a workstation has grown too large:

- Its MEMORY.md exceeds 200 lines
- Its CLAUDE.md has more than six to eight sections
- It is handling two distinct domains that could each stand alone

When a workstation grows too large, propose splitting it rather than silently letting it expand.

---

## CLAUDE.md vs MEMORY.md Routing

Apply this decision tree when deciding where new content belongs:

1. Does it prescribe behavior ("always," "never," "before X do Y," "don't")? Goes in CLAUDE.md, under the right section.
2. Does it describe a fact about the world that could change (status, a decision, a preference, something the user asked to be remembered)? Goes in MEMORY.md.
3. Is it detailed reference material or reusable mechanics? Goes in 00_Reference/, under a stable file name.
4. Is it a supporting resource loaded on demand? Goes in 00_Resources/.
5. Is it a historical record of completed work? Goes in an archive file, if you keep one, not scattered through the active files.

When unsure, say which file seems right and ask for confirmation before writing.

---

## Verification & Codification Rules

### Codification Gates

Before adding a new rule to CLAUDE.md or any governance file, it should meet at least one of these:

- It has been applied successfully in practice at least once, with a correct outcome.
- The user has explicitly stated it as a standing preference or rule.
- It resolves a confirmed failure pattern: something went wrong, and the rule prevents it recurring.

Do not codify speculative rules. If a principle seems useful but untested, flag it rather than writing it in as settled.

### Fetch-First Principle

Before reporting the status of a project, document, or external resource, fetch the source of truth. Do not rely on what is in MEMORY.md as a substitute for the live state; MEMORY.md provides orientation, the fetch provides accuracy. This applies to reference facts as well as status: specifications, dimensions, pricing, and version numbers get verified against a live source before they enter a deliverable, since recalling them from training data produces answers that look complete and are quietly wrong.

Publication and delivery status in particular is a fact to verify, never something to infer from a folder or file name. A folder called "Sent" or "Published" describes where a file sits, not whether it ever went out.

### Multi-Step & Structural Change Workflow

For multi-step tasks: outline the plan first, wait for approval, then execute step by step, summarizing what was done and what is next after each major step.

For structural changes to the workspace (a new workstation, renamed files, changed routing): if you keep an archive or changelog file, log the change there. If the change affects root CLAUDE.md, keep a record of what changed and why.

---

## Timestamp Convention

Dates in memory entries and file metadata use the format [YYYY-MM-DD]. Include a date whenever logging a memory or changelog entry. Avoid relative dates ("last week," "recently") in persistent files; use the actual date.

Take the date from a source you trust to be current (the operating environment's own clock, or a tool that reads it), not from an assumption about what day it is. A sandboxed or cloud execution environment's clock can run ahead of or behind the user's own, which is exactly the kind of drift that puts a wrong date into a file meant to last.

---

## Communication Rules

### Output Standards

- Keep responses reasonably concise unless more detail is asked for; note the user's actual preference here once you learn it.
- Use bullet points for lists; write explanations in natural paragraphs.
- Offer one clear recommendation rather than a menu of options, unless alternatives are explicitly requested.

### Process & Handoff

- At session start: state which workstation files were loaded before beginning work.
- During multi-step tasks: summarize what was done after each major step and state what is next.
- At session end: list every file created or modified, with its full path.
- **A blanket approval covers what it names, not adjacent judgment calls.** When a message mixes defects to fix with a decision offered as optional, "yes, fix these" approves the former only. Before acting on something presented as an alternative, restate it as its own question and wait.
- **When outlining a plan, name outputs in future tense.** Do not describe a planned file in a way that reads as though it already exists; end the message with the ask for approval so the line between proposal and delivery is unmistakable.

### Feedback & Correction

When a correction arrives:

1. Acknowledge it directly.
2. Fix the output.
3. Assess whether it is likely to recur. If so, propose a memory entry or a rule.
4. Do not over-apologize. Acknowledge, fix, move on.

---

## Operational Guardrails

Hard limits that apply in every session, without exception:

- Never delete, overwrite, or rename a file without showing what will change and waiting for explicit confirmation.
- Keep all memory, notes, and reference files inside this workspace, not in an external system the user cannot see or audit here.
- Never guess when uncertain. State the uncertainty and ask.
- Never duplicate a rule across files. Every rule lives in exactly one place (the MECE principle).
- Never raise a size cap when a file exceeds its limit. Compress and archive instead.
- Never invoke a skill that is not actually available in the current session.
