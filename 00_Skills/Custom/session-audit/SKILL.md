---
name: session-audit
description: >
  End-of-session audit that scans the conversation for corrections, stated preferences, and decisions that were never written down, proposes exactly where each one belongs in the workspace, and writes only what you approve to local files. That local save always happens. If, and only if, the workspace is already a git repository with a remote configured, it then also syncs everything to that remote as a last step; if it is not, or GitHub sync was never set up, the audit simply ends once local files are updated and confirmed, nothing about that is a failure or an incomplete run. Use this whenever you say "audit this session," "session audit," "what did we miss," "end of session check," or "close out the session." Works with any CoworkOS-style workspace that has a CLAUDE.md and MEMORY.md at its root.
---

# Session Audit

A short, repeatable close-out for the end of a session. It answers two questions only: did anything get said this session that should be remembered, and is the workspace safely backed up.

## Why this matters

The memory system in this template only works if MEMORY.md and CLAUDE.md actually stay current, and that depends on something noticing, mid-conversation, that a correction or a decision is worth saving. That works for anything explicit, but plenty of what should be captured is not: a small correction that got fixed and moved past, a preference stated in passing, a decision buried in the middle of an unrelated task. Nothing surfaces those unless something deliberately looks back over the whole conversation before it ends.

Running an audit at close-out is that deliberate look back. It treats memory capture as a session-end checkpoint rather than something that has to be caught perfectly in real time, which is a much easier bar to hit reliably. It also means drift gets caught inside the same session it happened in, rather than becoming a mystery three sessions later when a rule everyone assumed was written down turns out not to be.

## What it does

Three steps, in order, every time:

1. **Scans the conversation for uncaptured learnings:** corrections you made to the output, preferences you stated, decisions you reached, and new facts you shared that were not already in a workspace file.
2. **Proposes exactly where each finding belongs:** which file, which section, and the exact wording, checked against what is already saved so nothing gets proposed twice.
3. **Applies what you approve, then syncs.** Nothing gets written without approval. Once the approved writes are on disk, and only if the workspace is a git repository, it stages everything, commits with a message describing the session, and pushes.

No reorganizing, no cleanup pass, no progress tracking. Just: what was learned, and is it saved.

## How to use it

Install this as a skill in your Claude account, or reference it directly if your setup loads skills from a folder, then trigger it at the end of a session with any of: "audit this session," "session audit," "what did we miss," "end of session check," or "close out the session."

### Step 1: Load the workspace

Read whatever exists: root CLAUDE.md and MEMORY.md, plus the CLAUDE.md and MEMORY.md of every workstation actually touched this session. This is what Step 3 checks findings against, so it has to happen before the scan is filtered.

### Step 2: Scan for four kinds of signal

- **Corrections.** You edited, rejected, or rewrote something Claude produced. Ask what underlying rule drove the change. Changing "Best regards" to "Thanks" on a draft implies a sign-off preference, not just a one-time edit.
- **Explicit preferences.** Direct language: "always," "never," "I prefer," "from now on," "don't do that."
- **Decisions.** A choice that affects future work: one option over another, a deadline set, an ambiguity resolved.
- **New context.** A fact about you, your work, or your world that would help a future session if it were remembered.

### Step 3: Filter against what is already saved

Drop anything already written into a file loaded in Step 1. Only genuinely new findings make it to the next step.

### Step 4: Present findings for approval

For each finding, state the fact or rule in the exact wording to save, name the file and section it belongs in, and say in one sentence why it matters. Group findings into ones the right action is obvious for, and ones that need a judgment call. If there is nothing to report, say so plainly rather than manufacturing a finding: a clean session still runs Step 5.

### Step 5: Apply, then sync if there is somewhere to sync to

Write only what was approved, and confirm what landed where. This save to local files is the audit's real job, and it happens every time, regardless of git.

Syncing is a bonus step, not a requirement: only attempt it if the workspace is already a git repository with a remote configured (set up via `00_Resources/GitHub Sync Guide.md`). If it is not, say plainly that the audit is done, local files are saved, and stop there; do not treat the absence of GitHub sync as something to apologize for or work around.

When there is a remote to sync to: fetch first and stop if the remote has moved ahead of local, otherwise stage everything, not just what this step wrote, since anything else left uncommitted belongs in the same sync. Commit with a message naming the session's theme, push, then verify with a status check that local and remote actually match. Never force-push, never resolve a conflict by guessing which side is right, and never bypass a pre-commit guard without an explicit, confirmed false positive.

## What this deliberately does not do

It does not reorganize files, does not run a general cleanup pass, and does not track progress against a plan. Scope creep here is exactly how a two-question checklist turns into a chore nobody wants to run at the end of a long session. If the workspace needs restructuring, treat that as its own, separate task.
