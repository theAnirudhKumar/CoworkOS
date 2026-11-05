---
name: session-audit
description: >
  Use this whenever you say "audit this session," "session audit," "what did we miss," "end of session check," or "close out the session." It is an end-of-session audit. It scans the conversation for corrections, stated preferences, decisions and useful new context that were never written down. It proposes exactly where each one belongs, and writes only what you approve to local files. That local save is the real job and always happens. If the workspace is already a git repository with a remote you own, it then also checks that no other session is mid-write and syncs the whole workspace to that remote as a last step. If there is no remote, or GitHub sync was never set up, the audit ends once local files are saved and confirmed. That is a complete run. Works with any CoworkOS-style workspace that has a CLAUDE.md and MEMORY.md at its root.
---

# Session Audit

A short, repeatable close-out for the end of a session. It answers two questions only. Did anything get said this session that should be remembered? And is the workspace safely saved?

## Why this matters

The memory system in this template only works if MEMORY.md and CLAUDE.md stay current. That depends on something noticing, mid-conversation, that a correction or a decision is worth saving. Explicit requests get caught. Plenty of what should be captured is quieter: a small correction that got fixed and moved past, a preference stated in passing, a decision buried in the middle of an unrelated task. Nothing surfaces those unless something deliberately looks back over the whole conversation before it ends.

Running an audit at close-out is that deliberate look back. Memory capture becomes a checkpoint at the end of the session. That is a much easier bar to hit than catching everything perfectly in real time. Drift also gets caught inside the same session it happened in. Otherwise it becomes a mystery three sessions later, when a rule everyone assumed was written down turns out to be missing.

## What it does

Five things, in order, every time:

1. **Scans the conversation for uncaptured learnings:** corrections, stated preferences, decisions, and new context that is not already in a workspace file.
2. **Proposes exactly where each finding belongs:** which file, which section, and the exact wording, checked against what is already saved so nothing is proposed twice.
3. **Checks that no other session is mid-write**, if the workspace is a git repository. Several sessions can share one workspace.
4. **Applies only what you approve**, with a backup first and a check afterwards that the text landed.
5. **Syncs, if there is somewhere to sync to.** Only when the workspace is a git repository with a remote you own.

No reorganizing, no cleanup pass, no progress tracking. Just: what was learned, and is it saved.

## How to use it

Install this as a skill in your AI tool's account, or have your tool read this file directly when triggered if it has no skill mechanism. Then trigger it at the end of a session with any of: "audit this session," "session audit," "what did we miss," "end of session check," or "close out the session."

## Step 1: Load the workspace

Read whatever exists:

1. Root CLAUDE.md and root MEMORY.md.
2. The CLAUDE.md and MEMORY.md of every workstation touched this session.
3. Any reference file loaded during the session, such as `00_Resources/voice-principles.md`.

Step 3 checks findings against these files, so this has to happen first.

**Read every file in full.** These files run long. If a tool cuts off a read or says the output is too large, read the file in chunks (for example `sed -n '1,150p'`, then `151,300p`, and so on), or hand the read to a helper and ask for the section headings plus exact quotes on the topics this session touched. Never audit against a file you only partly read. If you do, you will "find" things that are already written down, and miss stale lines that need replacing.

## Step 2: Scan for four kinds of signal

Go through the whole conversation, top to bottom.

- **Corrections.** You edited, rejected, or rewrote something the AI produced. Ask what underlying rule drove the change. Changing "Best regards" to "Thanks" on a draft implies a sign-off preference. The one-time edit is the evidence. The rule is the finding.
- **Explicit preferences.** Direct language: "always," "never," "I prefer," "from now on," "don't do that."
- **Decisions.** A choice that affects future work: one option over another, a deadline set, an ambiguity resolved. Anything that should stop the same question being asked again.
- **New context.** A fact about you, your work, or your world that would help a future session if it were remembered.

Two things count that are easy to miss:

- **The AI's own breach of an existing rule is a correction.** If the session used a method a workspace file already forbids, or skipped a check one already requires, that is a finding even if nobody pointed it out. Propose one of two fixes: redo the work the documented way, or add a carve-out to the rule if the breach turned out to be the right call. Surface it. Do not quietly move on.
- **A technique that made something work is new context.** If the session found a workaround, a required setting, a trap in a tool's output, or a non-obvious way to get at some data, save the exact detail: the command, the setting name, the field, the limit. A vague note such as "used a different approach" forces the next session to rediscover it the slow way.

## Step 3: Filter against what is already saved

Drop anything already written into a file loaded in Step 1. Only genuinely new findings move on.

**When a finding updates an existing entry, quote the stale line.** Show the current text exactly as it appears in the file, and propose replacing it. Do not add a second entry next to it. A stale entry is worse than no entry, because a future session will act on it. If the new finding contradicts the old one, say plainly what conflicts and ask how to reconcile it, per the Memory System section of root CLAUDE.md.

Use the two placement tests in root CLAUDE.md to choose the file. A rule that prescribes behavior goes in CLAUDE.md. A fact that could change goes in MEMORY.md. Domain-specific findings go in that workstation's files.

## Step 4: Present findings for approval

Present each finding in this shape:

```
**[Number]. [What happened]**

- **The rule or fact:** [Exact wording to save]
- **Where it goes:** [File path and section name]
- **Replaces:** [The stale line, quoted exactly, or "nothing, this is new"]
- **Why:** [One sentence on why this matters for future sessions]
```

Group them into two sets:

- **Clear calls.** The right action is obvious.
- **Your call.** A judgment call, or wording worth deciding together.

Both groups need your approval before anything is written. The grouping only tells you where to spend your attention.

If nothing survives the filter, say so plainly: "Clean session. Nothing new to capture." Do not manufacture a finding to fill the report. A clean session still runs the close-out checks below and Step 7, because nothing to capture is different from nothing to save.

### Close-out check: root MEMORY.md size

Count the lines in root MEMORY.md and compare against the ceiling in `00_Reference/Memory System.md` (Size Ceilings). Include the lines your approved findings would add. If it is over, propose the fix that file describes: compress verbose entries to the two-sentence cap first, then move entries that are no longer current to ARCHIVE.md. If it is still over after both, flag it for a decision. Do not raise the limit. These proposals need approval like any other finding.

## Step 5: Check that no other session is mid-write

Skip this step if the workspace is not a git repository.

**Run this before the first write, not just before the commit.** More than one session can point at the same workspace at once. A session that is mid-sync runs `git add -A`, which sweeps up whatever half-written files it finds. Writing while another session is staging is how your finding lands in someone else's commit, or lands half-written.

From the workspace root, check all of these in one go:

```bash
cd "<workspace root>"
ls .git/index.lock .git/MERGE_HEAD .git/rebase-merge .git/rebase-apply 2>&1
git branch --show-current
git log -3 --format="%h | %ad | %s" --date=format:"%H:%M:%S"
date +%s
stat -f %m .git/index    # macOS
stat -c %Y .git/index    # Linux
```

Only one of the two `stat` lines will work on a given computer. That is expected. Subtract its result from `date +%s` to get the age of `.git/index` in seconds.

Hold if **any** of these is true:

- `.git/index.lock` exists.
- A merge or rebase is in progress (`MERGE_HEAD`, `rebase-merge` or `rebase-apply` exists).
- `.git/index` was modified in the last 75 seconds or so.
- The most recent commit landed in the last 75 seconds or so.
- The current branch is not the branch this workspace normally uses. A session on another branch is mid-task. Committing onto its branch, or switching branches out from under it, damages its work.

When holding, say so in one line naming what you saw. Then re-check about every 25 seconds, up to six times, rather than asking the user to wait. Proceed once there is no lock, no merge or rebase, and the index has been quiet for 75 seconds. On a Linux computer the loop looks like this (on macOS, swap `stat -c %Y` for `stat -f %m`):

```bash
cd "<workspace root>"
for i in 1 2 3 4 5 6; do
  M=$(stat -c %Y .git/index 2>/dev/null)
  L=$(ls .git/index.lock 2>/dev/null | wc -l)
  AGE=$(( $(date +%s) - M ))
  echo "check $i | index age ${AGE}s | lock=$L"
  if [ "$AGE" -ge 75 ] && [ "$L" -eq 0 ]; then echo "SETTLED"; break; fi
  sleep 25
done
git branch --show-current
```

If it is still busy after six checks, stop. Report what is holding it, write nothing, and let the user decide. **Never delete a lock file another process may hold.**

A clean `git status` after waiting can mean the other session already swept your earlier files into its own commit. That is fine. Check with `git log --oneline -3 -- <path>` before concluding your work is unsaved.

**Re-run the quick check right before staging in Step 7.** The gap between writing and committing is long enough for another session to start.

## Step 6: Apply what was approved

Write only what was approved, all, some, or none. Never write before approval, and never treat silence as approval.

**Back up first.** Before editing, copy each file you are about to change into `.backups/YYYY-MM-DD-<short-name>/` at the workspace root, where `<short-name>` is a few words describing the session. This template's `.gitignore` already ignores `.backups/`, so backups never reach a remote.

**Edit in place, with an exact-match check.** Change only the anchored text. Use an edit method that confirms the old text was found exactly once before replacing it. Do not retype a whole file from what a tool showed you, because tool output can be cut short and the rest of the file is lost.

**Confirm it landed.** Re-read the changed part of each file. Check that the new text is there, and that any numbered list you added to is still numbered correctly. Then tell the user what was written and where.

**Before a move or rename,** search the workspace for references to the old path and update them in the same pass. This is rule 13 in `00_Reference/File Creation Rules.md`.

**Dates come from the user's own time zone.** Many AI tools run on a server whose clock is set to UTC, which can put you on the wrong day. When a date goes into an entry, a backup folder name, or a commit message, take it from the user's time zone, for example `TZ=<your time zone> date +%Y-%m-%d`. If you do not know their time zone, ask once, and propose saving it to MEMORY.md.

## Step 7: Sync, if there is somewhere to sync to

The local save in Step 6 is the audit's real job. Syncing is an optional extra. Only attempt it if the workspace is already a git repository with a remote configured, set up via `00_Resources/GitHub Sync Guide.md`. If it is not, say plainly that the audit is done and local files are saved, and stop. The absence of GitHub sync is not a problem to apologize for or work around.

When there is a remote, this step runs last, so the session's findings ship in the same commit as the work that produced them. It runs on a clean session too.

### Where to run git

Run git in an environment that can both see the workspace files and reach the network. Some AI tools give you more than one shell. One might see your files but have no network, and another might have network but not see your files. Pick the one that has both. Usually that is a shell on your computer, where your GitHub sign-in is already saved.

If no available environment has both, do not skip the sync silently. Say so, name every uncommitted file (from `git status --porcelain`), and give the user the commands below to run themselves.

**In travel mode** the workspace is a temporary clone inside the session's own environment. Run git there, in that clone. See `00_Skills/Custom/travel-mode/SKILL.md`.

### Check the remote first

Read the setup from git rather than assuming it:

```bash
cd "<workspace root>"
git remote get-url origin
git branch --show-current
```

If there is no remote, say so and stop. Never create one.

If the remote points at the CoworkOS template repository the files were originally copied from, do not push. Say so plainly and offer to remove that remote. That repository belongs to the template's author, and pushing to it would send your life into someone else's repository.

### The sequence

Fetch before anything else, and read what comes back:

```bash
git fetch origin
git status -sb
```

If the first line says `behind` or `diverged`, the remote has commits this session never saw, usually from a travel session or another device. **Stop before committing and say so.** Then:

1. Close any editor that keeps files open in memory, such as a note-taking app. If it is open during a pull, it can overwrite what was pulled with its own stale copy.
2. Run `git pull --rebase origin main` (use your branch name if it is not `main`).
3. Read what came down, then continue.

Once the fetch is clean:

```bash
git status --porcelain
```

If that prints nothing, report "Workspace already in sync" and stop. Otherwise, re-run the quick check from Step 5, then:

```bash
git add -A
git commit -m "<message>"
git push origin main
git status -sb
```

The last command is the verification. It must show `## main...origin/main` with no `ahead` or `behind` count. A command that exits without an error is not proof the push landed. Read the output.

### Commit message format

```
Session YYYY-MM-DD: <three to six word theme>

- <what changed, one line per meaningful group>
- <audit findings written, if any>
```

The theme says what the session was actually about. Take the date from the user's time zone (Step 6).

A good message:

```
Session 2026-03-14: Budget categories and rent update

- Finances: new grocery and transport categories
- MEMORY.md: rent change and savings target decision
```

A bad message: `Update files`. It tells a future reader nothing.

### Scope is the whole workspace, deliberately

`git add -A` stages every uncommitted change, not only what Step 6 wrote. That is on purpose. Anything left behind by an earlier session, or edited by hand outside the AI tool, goes up in the same push. The audit becomes the one sync point for the entire workspace, so nobody needs a habit of committing each document.

That same sweep is why Step 5 exists. The behavior that picks up a stray file will also pick up another session's half-written one.

### What to report

Keep it to a few lines:

- The commit subject line.
- The files changed, grouped by top-level folder, with a count for each. Do not list forty filenames.
- Confirmation that local and remote match, from `git status -sb`.

### If the identity guard blocks the commit

This template ships a pre-commit hook at `.githooks/pre-commit` that blocks commits adding things shaped like ID numbers, account numbers, or access tokens. If it blocks a commit:

- Stop. Show the user the masked finding the guard printed, and wait.
- The fix is to remove the identifier from the file. If the file itself is an identity or financial document, move it out of the workspace and reference it by path from where it actually lives.
- Use `git commit --no-verify` only when the user has explicitly confirmed the finding is a false positive. Never decide that alone.

To scan the whole workspace on demand, which reports but never blocks:

```bash
python3 .githooks/pre-commit --full
```

### When something goes wrong

| Situation | What to do |
| :--- | :--- |
| Another session is mid-write (lock file, recent commit, merge or rebase, or a different branch) | Hold and re-check per Step 5. If still busy after six checks, stop and report. Never delete a lock another process may hold |
| The opening fetch shows `behind` or `diverged` | Stop before committing. Close any editor that caches open files, run `git pull --rebase`, then continue |
| Push rejected because the remote moved | Run `git pull --rebase`, read what came down, push again. Never force-push |
| The rebase hits a conflict | Stop. Report the conflicting files and wait for a decision |
| No remote configured | Say so and stop. Never create one |
| The remote is the CoworkOS template repository | Do not push. Say so and offer to remove that remote |
| A file is over 100 MB | Report it, since GitHub will reject the push. Do not set up large-file storage without asking |
| The identity guard blocks the commit | Stop, show the masked finding, and wait. Never bypass it unasked |
| No environment can both see the files and reach the network | Say so, name every uncommitted file, and give the commands |

## Safety rules

These apply to Steps 5 through 7 and override any instinct to tidy up.

- **Never write or commit while another session holds the workspace.** Hold and re-check per Step 5.
- **Never run a command that discards uncommitted work.** That includes `git push --force`, `git reset --hard`, `git clean -fd` and `git checkout -- .`. The files on disk are the primary copy. Git is the backup.
- **Never change repository visibility or add collaborators.** The repository is private because the workspace holds personal material.
- **Never switch branches to get a commit onto the main branch.** A branch you did not check out may belong to another session.
- **Never resolve a conflict by guessing which side is right.** Report the files and wait.
- **Never bypass the identity guard** without an explicit, confirmed false positive.
- **Never treat silence as approval.** No answer means nothing gets written.
- **Never treat a successful exit code as proof of sync.** Verify with `git status -sb` and read the output.

## What this deliberately does not do

It does not reorganize files, does not run a general cleanup pass, and does not track progress against a plan. Scope creep is exactly how a two-question checklist turns into a chore nobody wants to run at the end of a long session. If the workspace needs restructuring, treat that as its own, separate task.
