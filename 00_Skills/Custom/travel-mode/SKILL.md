---
name: travel-mode
description: >
  Work on this workspace from its GitHub copy when your primary computer is
  unreachable, then push everything back so a later session on that computer
  can pull it down. Use this skill when you say "travel mode," "start a
  travel session," "my computer is closed," "work from GitHub," "I'm
  travelling," or "work without my computer." Requires the workspace to
  already be a git repository with a remote, set up via the GitHub Sync
  Guide, and a GitHub token with write access to that repository.
---

# Travel Mode

Work the workspace out of its GitHub copy instead of the computer it normally lives on. Everything about how files are created, named, routed and written stays exactly the same, because every rule that governs those things is inside the repository. The only thing that changes is where the files sit and how they get back.

This skill assumes you have already followed `00_Resources/GitHub Sync Guide.md` and have a private GitHub repository this workspace pushes to.

## Check whether this skill is needed at all

If your AI tool can reach your primary computer directly in this session, say so and stop:

> Your computer is reachable, so travel mode is not needed. Working against the local workspace directly is faster and skips the token step.

Travel mode is for when that connection is genuinely down. Using it while your computer is connected creates a second copy of the workspace and invites exactly the divergence the whole design is built to avoid.

## The one thing that is different, and it matters

On your computer, files live on disk and survive whatever happens to a session. In travel mode they live in a temporary environment that can be destroyed when the session ends, sometimes without warning.

**So every turn ends with everything pushed out.** Not every meaningful piece of work, not only at close-out: every turn. There is no reliable signal that a travel session has ended. You may lose signal, close the app, or simply stop responding without saying anything, and a rule that only fires "at close-out" is worthless in exactly the case it exists for. Treat every turn as if it might be the last one.

**"Saved" is not the same as "pushed."** Step 3 below decides which is actually true for a given session. Do not tell yourself, or anyone relying on this, that everything is safe until that probe has passed.

## Step 1: Get a token

Most temporary or sandboxed environments have network access but no saved credential, since the usual one lives on your own computer.

If you need to create one, these are reasonable settings for a fine-grained GitHub personal access token:

| Setting | Value |
| :--- | :--- |
| Type | Fine-grained, not classic |
| Repository access | Only the one repository this workspace syncs to |
| Permission | Contents: Read and write |
| Expiration | A fixed period, with a reminder to rotate it before it expires |

Say this once, plainly, and do not repeat it every session:

> This token will sit in this conversation's history. Scoped to one repository, that is a small blast radius, but rotate it if this conversation is ever shared or exported.

**Never write the token into a file.** Not into a note, not into a scratch file, not anywhere inside the clone. It belongs only in the remote URL, which lives in `.git/config` and is not tracked. The identity guard (Step 4) blocks GitHub token patterns at commit time as a backstop; do not rely on the backstop as the primary protection.

## Step 2: Clone, markdown only

```bash
cd <a scratch directory in this environment>
git clone --depth 1 --filter=blob:none --sparse --quiet \
  https://x-access-token:<TOKEN>@github.com/<your-username>/<your-repo-name>.git workspace
cd workspace
git sparse-checkout set --no-cone '*.md' '/.githooks/pre-commit'
```

A sparse, shallow clone of just the markdown files and the hook script is almost always faster than cloning everything, especially if your workspace has grown to include PDFs, images, or other large binary files that are not useful outside your normal working environment anyway.

**`/.githooks/pre-commit` needs to stay in the pattern deliberately.** It is a shell script, not markdown, so `'*.md'` alone excludes it and the file never reaches disk. Step 4 then fails on a file that is not there.

Two things worth knowing about how sparse checkouts behave:

- Files that are not checked out **stay in the index**, so a commit never deletes them.
- `--filter=blob:none` **without** `--sparse` is usually slower, not faster, because checkout then refetches every blob one at a time.

**Never print the remote URL.** `git remote -v` echoes the token. If the URL is needed for a check, use `git remote get-url origin | sed 's#//.*@#//***@#'`.

## Step 3: Probe the write path before doing any work

**A successful clone proves nothing about pushing.** Some environments allow reads but restrict writes for policy reasons unrelated to your token's own permissions. Find out now, in a few seconds, rather than after the work is written.

```bash
git commit --allow-empty -m "Travel probe"
git push origin main && git reset --hard HEAD~1
```

Read the output, not just the exit code.

**If the push succeeds**, the reset removes the probe commit and travel mode runs exactly as written below. Tell the person you are working with, once:

> Everything is pushed as we go, so you can stop whenever you need to without losing anything.

**If the push is refused**, treat this as a signal to stop pushing, not something to retry with a different token or work around through a platform's REST API instead of git. Go to Degraded mode below and say so before starting work.

## Degraded mode: when the push path is closed

The work still has to leave the temporary environment. Only the transport changes.

Tell the person you are working with, before writing anything:

> Push is blocked on this session, so nothing will reach GitHub. Everything I produce comes to you as a file you need to save, and it lands in the workspace by hand once you are back at your computer.

Then, for every deliverable, in this order:

1. **Send it as a downloadable file**, every time it is finished or meaningfully revised. This is the primary path in degraded mode, not a courtesy copy.
2. **Name the destination path explicitly**, so placing it by hand later is mechanical: the full path it would have taken inside the workspace.

Still commit locally as Step 6 describes, even though the commits will not survive the session ending. It keeps the working tree honest and makes the file list at close-out accurate.

**Do not deliver the same document twice**, once as-is and once revised, without saying which one supersedes the other.

## Step 4: Activate the identity guard

The clone carries the hook file, since Step 2 puts it in the sparse pattern, but not the configuration that runs it:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
```

Confirm it is active before writing anything: check that `.githooks/pre-commit` exists and is executable, and read the output rather than trusting the exit code alone. Without this the guard is silently inactive, which is worse than not having it at all, because the protection is assumed rather than present.

This matters more here than it looks. The guard is a local git hook, so anything that commits through a platform's web API instead of through git bypasses it entirely. Going through git is what keeps it running.

## Step 5: Load context exactly as usual

```bash
cat CLAUDE.md
cat MEMORY.md
```

From here nothing is special. The Routing Protocol, Routing Map, File Creation Rules, Governance Rules, the Memory System, and voice-principles are all markdown, so they are all in the sparse checkout. Read the workstation's own `CLAUDE.md` and `MEMORY.md` for whatever you are working on, state which files were loaded, and proceed under the normal rules.

A clone made seconds ago is current by definition, so any "check for a newer version before starting" rule elsewhere in this workspace does not apply here.

## Step 6: Work, and get it out as you go

Files are created in the clone at the same paths they would take on your computer. Same naming, same routing, same frontmatter, same everything.

**A new `.md` file at any depth is covered by the sparse pattern and commits normally.** A non-markdown file is not, and `git add` will refuse it with an error naming the sparse-checkout definition. That refusal is loud rather than silent, so it will not pass unnoticed. If a non-markdown file is genuinely needed, widen the pattern for that one path rather than reaching for a broader override:

```bash
git sparse-checkout set --no-cone '*.md' '/.githooks/pre-commit' '/path/to/thing.png'
```

After each meaningful unit of work:

```bash
git add -A
git commit -m "Travel YYYY-MM-DD: <three to six word theme>"
git push origin main
git status -sb
```

The `Travel` prefix on the commit subject is the marker that separates these from ordinary sessions, which makes the return pull easy to read. Verify with `git status -sb` and read the output rather than trusting the exit code.

**In degraded mode, drop the `git push` line** and deliver by the Degraded mode transports instead. Everything else in this step is unchanged.

## Step 7: Close out

Run the session-audit skill as normal; it applies unchanged here.

Then tell the person what waits for them, in one of two shapes depending on Step 3.

**Pushed session:**

> Pushed N commits to GitHub. When you are back at your computer, pull before you open your usual editor or app for this workspace: `git pull --rebase origin main`.

If you browse this workspace with a tool that keeps its own in-memory cache of files, such as Obsidian, close that tool first, then pull, then reopen it. Otherwise it can overwrite what you just pulled with whatever it still has in memory. This warning is not a formality; it is one of the more common ways travel-mode work gets silently overwritten.

**Degraded session:**

> Nothing reached GitHub, so there is nothing to pull. N files came to you in this conversation. Here is where each one goes:

Then list every file with its full workstation-relative destination path. **Never give the pushed-session close-out on a degraded session.** Telling someone to pull when the remote never moved sends them looking for work that is not there.

### Nothing survives as chat-only content

The temporary environment dies with the session, and the conversation itself cannot write to your computer later. So anything that exists only as text in the conversation is lost the moment the session ends.

Reasoning, drafts, decisions and findings produced in conversation get written to their proper paths under the normal rules and get out of the temporary environment in the same turn that produced them. Anything deliberately not kept gets named as dropped, so nothing is silently assumed saved.

## What does not work in travel mode

Say so plainly rather than attempting a workaround:

| Not available | Why |
| :--- | :--- |
| Views, backlinks, or app-specific features of whatever tool you normally browse this workspace with | That tool runs on your computer. The files are plain markdown here |
| Large binary files not in the sparse checkout | Not cloned, to keep the clone fast. Widen the pattern only if one is genuinely needed |
| Anything you deliberately keep outside this repository | If part of your setup is intentionally excluded from git, it stays unavailable here, which is the point |
| Scheduled or recurring tasks tied to your computer | They only fire while that computer and its usual app are running |
| A platform's REST API as a substitute for `git push` | Bypasses the identity guard entirely, since that guard is a local git hook. Push through git, not around it |
| `git push`, on some sessions | Some sandboxed environments restrict outbound writes for policy reasons independent of your token. Step 3 detects this. Reads are usually unaffected, so a clean clone is not evidence that push will also work |
| Writing to your computer directly from this session | No live connection exists unless your specific tool provides one, and that is a separate feature from travel mode itself |

## Safety Rules

- **Never print the token or the remote URL.** Mask it in any output.
- **Never write the token into a file**, including a scratch file inside the clone.
- **Never use `git commit --no-verify`** to get past the identity guard. Stop and report instead.
- **Never force push.** A rejected push means the remote moved; pull with `--rebase` and read what came down.
- **Never resolve a conflict by picking a side automatically.** Report the files and wait for a decision.
- **Never leave work uncommitted at the end of a turn.** The environment is temporary.
- **Never end a turn with work living only in the conversation.** Write it to its proper path and get it out of the environment in that same turn, or say plainly that it was dropped.
- **Never retry a policy-refused push more than once or twice.** It is usually a deliberate restriction, not a transient fault, and will refuse identically every time.
