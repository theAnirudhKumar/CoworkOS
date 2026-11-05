---
name: travel-mode
description: >
  Use this skill when you say "travel mode," "start a travel session," "my
  computer is closed," "work from GitHub," "I'm travelling," or "work
  without my computer." It works on this workspace from its GitHub copy
  when your primary computer is unreachable, then pushes everything back so
  a later session on that computer can pull it down. A GitHub token may be
  included in the same message as the trigger. Requires the workspace to
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

**So every turn ends with everything out of that environment.** Every turn, not only after big pieces of work and not only at close-out. There is no reliable signal that a travel session has ended. You may lose signal, close the app, or simply stop responding without saying anything. A rule that only fires "at close-out" is worthless in exactly the case it exists for. Treat every turn as if it might be the last one.

**"Out of the environment" is not always "pushed."** Step 3 decides which is true for a given session. Do not tell anyone everything is pushed until that probe has passed.

## Step 1: Get a token

Most temporary or sandboxed environments have network access but no saved credential, since the usual one lives on your own computer.

**The token may arrive in the trigger message**, for example `travel mode <token>`. That saves a round trip. If the trigger arrives without one, ask for it once.

If you need to create one, these are reasonable settings for a fine-grained GitHub personal access token:

| Setting | Value |
| :--- | :--- |
| Type | Fine-grained, not classic |
| Repository access | Only the one repository this workspace syncs to |
| Permission | Contents: Read and write |
| Expiration | A fixed period, with a reminder to rotate it before it expires |

Say this once, plainly, and do not repeat it every session:

> This token will sit in this conversation's history. Scoped to one repository, that is a small blast radius, but rotate it if this conversation is ever shared or exported.

**Never write the token into a file.** Not into a note, not into a scratch file, not anywhere inside the clone. It belongs only in the remote URL, which lives in `.git/config` and is not tracked. The identity guard (Step 4) blocks GitHub token patterns at commit time as a backstop. Do not rely on the backstop as the main protection.

**A valid token is not enough on its own.** See Step 3.

## Step 2: Clone, markdown only

```bash
cd <a scratch directory in this environment>
git clone --depth 1 --filter=blob:none --sparse --quiet \
  https://x-access-token:<TOKEN>@github.com/<your-username>/<your-repo-name>.git workspace
cd workspace
git sparse-checkout set --no-cone '*.md' '/.githooks/pre-commit'
```

A sparse, shallow clone of just the markdown files and the hook script is almost always faster than cloning everything. That matters most once your workspace includes PDFs, images, or other large files that are not useful outside your normal working environment anyway.

**If the clone fails with a 404 or a permission error, regenerate the token** scoped to the right repository, rather than debugging further. A token that has expired, was scoped to the wrong repository, or was created before the repository was renamed produces exactly these errors, and a fresh token is the fastest fix.

**`/.githooks/pre-commit` needs to stay in the pattern deliberately.** It is a shell script, not markdown, so `'*.md'` alone leaves it out and the file never reaches disk. Step 4 then fails on a file that is not there.

Two things worth knowing about how sparse checkouts behave:

- Files that are not checked out **stay in the index**, so a commit never deletes them.
- `--filter=blob:none` **without** `--sparse` is usually slower, because checkout then fetches every file one at a time.

**Never print the remote URL.** `git remote -v` shows the token. If the URL is needed for a check, use `git remote get-url origin | sed 's#//.*@#//***@#'`.

## Step 3: Probe the write path before doing any work

**A successful clone proves nothing about pushing.** Some environments allow reads but restrict writes for policy reasons that have nothing to do with your token's permissions. Find out now, in a few seconds, rather than after the work is written.

```bash
git commit --allow-empty -m "Travel probe"
git push origin main && git reset --hard HEAD~1
```

Read the output, not just the exit code. The `reset --hard` here only removes the empty probe commit, right after cloning, before any work exists.

**If the push succeeds**, the reset removes the probe commit and travel mode runs exactly as written below. Tell the person you are working with, once:

> Everything is pushed as we go, so you can stop whenever you need to without losing anything.

**If the push is refused**, check whether your AI tool offers a documented way to authorize this repository for the session, such as adding it to the session's connected repositories. If one exists, use it, then run the probe again. If none exists, go to Degraded mode below and say so before starting work. Do not try a different token, and do not work around git through a platform's web API.

An error message may name a fix, such as a setting to change. Check that the fix actually exists in your tool before acting on it or passing it on. Repeating an error message's advice is not the same as checking it.

## Degraded mode: when the push path is closed

The work still has to leave the temporary environment. Only the transport changes.

Tell the person you are working with, before writing anything:

> Push is blocked on this session, so nothing will reach GitHub. Everything I produce comes to you as a file you need to save, and it lands in the workspace by hand once you are back at your computer. Nothing is pushed, so there is nothing to pull.

Then, for every deliverable, in this order:

1. **Send it as a downloadable file**, every time it is finished or meaningfully revised. This is the main path in degraded mode, not a courtesy copy.
2. **Optionally, email it to yourself.** If a mail connector is available, it can send the file to your own address. Mail connectors sign in separately from git, so this route usually still works when push is blocked, and the file lands somewhere you already read. Ask for the address. Never guess one.
3. **Name the destination path explicitly**, so placing it by hand later is mechanical: the full path it would have taken inside the workspace.

A file-storage connector that can only create new files, not update existing ones, is a poor extra route. Every revision lands as a new file, so iterating leaves a trail of duplicates. Use one only if asked.

Still commit locally as Step 6 describes, even though the commits will not survive the session ending. It keeps the working tree honest and makes the file list at close-out accurate.

**Do not write two near-identical copies of the same document.** Delivering one file twice is fine. Writing a second, slightly different file because the first was forgotten is what this rule prevents. If a revision replaces an earlier delivery, say which one is current.

## Step 4: Activate the identity guard

The clone carries the hook file, since Step 2 puts it in the sparse pattern, but not the setting that runs it:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
```

Confirm it is active before writing anything. Check that `.githooks/pre-commit` exists and is executable, and read the output rather than trusting the exit code. Without this the guard is silently inactive. That is worse than not having it at all, because everyone assumes the protection is there.

This matters more here than it looks. The guard is a local git hook. Anything that commits through a platform's web API instead of through git skips it entirely. Going through git is what keeps it running.

## Step 5: Load context exactly as usual

```bash
cat CLAUDE.md
cat MEMORY.md
```

From here nothing is special. The Routing Protocol, Routing Map, File Creation Rules, Governance Rules, the Memory System, and voice-principles are all markdown, so they are all in the sparse checkout. Read the workstation's own `CLAUDE.md` and `MEMORY.md` for whatever you are working on, state which files were loaded, and proceed under the normal rules.

A clone made seconds ago is current by definition. Any "check for a newer version before starting" rule elsewhere in this workspace does not apply here.

## Step 6: Work, and get it out as you go

Files are created in the clone at the same paths they would take on your computer. Same naming, same routing, same frontmatter, same everything.

**A new `.md` file at any depth is covered by the sparse pattern and commits normally.** A non-markdown file is not, and `git add` refuses it with an error naming the sparse-checkout definition. That refusal is loud, so it will not pass unnoticed. If a non-markdown file is genuinely needed, widen the pattern for that one path:

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

The `Travel` prefix on the commit subject separates these from ordinary sessions, which makes the return pull easy to read. Take the date from your own time zone, not the environment's clock, which is often set to UTC. Verify with `git status -sb` and read the output rather than trusting the exit code.

**In degraded mode, drop the `git push` line** and deliver by the Degraded mode routes instead. Everything else in this step is unchanged.

### Nothing survives as chat-only content

The temporary environment dies with the session, and the conversation itself cannot write to your computer later. Anything that exists only as text in the conversation is lost the moment the session ends.

**Check this at the end of every turn.** Reasoning, drafts, decisions and findings produced in conversation get written to their proper paths under the normal rules. They get out of the temporary environment in the same turn that produced them. Anything deliberately not kept gets named as dropped, so nothing is silently assumed saved.

Close-out in Step 7 is only the final sweep over this. If that sweep finds something stranded, the per-turn check was missed.

## Step 7: Close out

**When the session carried substantial thinking, run the chat-context skill in handoff mode first** (`00_Skills/Custom/chat-context/SKILL.md`). It writes a structured context file for the next session. On a pushed session that file travels back with everything else. On a degraded session it is delivered as a file like any other. It matters more there, because the conversation is exactly what does not survive.

Then run the session-audit skill as normal. It applies unchanged, with one point to note: its git step runs inside this temporary clone, since that is where the files are.

Then tell the person what waits for them, in one of two shapes depending on Step 3.

**Pushed session:**

> Pushed N commits to GitHub. When you are back at your computer, pull before you open your usual editor or app for this workspace: `git pull --rebase origin main`.

If you browse this workspace with an editor that keeps files open in memory, such as a note-taking app, close it first, then pull, then reopen it. Otherwise it can overwrite what you just pulled with whatever it still has in memory. This warning is not a formality. It is one of the most common ways travel-mode work gets silently overwritten.

**Degraded session:**

> Nothing reached GitHub, so there is nothing to pull. N files came to you in this conversation. Here is where each one goes:

Then list every file with its full destination path inside the workspace. **Never give the pushed-session close-out on a degraded session.** Telling someone to pull when the remote never moved sends them looking for work that is not there.

## What does not work in travel mode

Say so plainly rather than attempting a workaround:

| Not available | Why |
| :--- | :--- |
| Views, backlinks, or app-specific features of whatever tool you normally browse this workspace with | That tool runs on your computer. The files are plain markdown here |
| Large binary files not in the sparse checkout | Not cloned, to keep the clone fast. Widen the pattern only if one is genuinely needed |
| Anything you deliberately keep outside this repository | If part of your setup is intentionally left out of git, it stays unavailable here, which is the point |
| Scheduled or recurring tasks tied to your computer | They only run while that computer and its usual app are running |
| A platform's web API as a substitute for `git push` | It skips the identity guard entirely, since that guard is a local git hook. Push through git |
| `git push`, on some sessions | Some sandboxed environments restrict writes for policy reasons, whatever your token allows. Step 3 detects this. Reads are usually unaffected, so a clean clone is not evidence that push will work |
| Writing to your computer directly from this session | No live connection exists unless your specific tool provides one, and that is a separate feature from travel mode |

## Safety Rules

- **Never print the token or the remote URL.** Mask it in any output.
- **Never write the token into a file**, including a scratch file inside the clone.
- **Never use `git commit --no-verify`** to get past the identity guard. Stop and report instead.
- **Never force push.** A rejected push because the remote moved means pull with `--rebase` and read what came down.
- **Never resolve a conflict by picking a side automatically.** Report the files and wait for a decision.
- **Never leave work uncommitted at the end of a turn.** The environment is temporary.
- **Never end a turn with work living only in the conversation.** Write it to its proper path and get it out of the environment in that same turn, or say plainly that it was dropped.
- **Never retry a policy-refused push more than once.** It is a deliberate restriction, not a passing fault, and it will refuse the same way every time. One confirming retry is reasonable. More is wasted turns.
- **Never tell the user to change a setting you have not verified exists.** An error message can name a fix that is not in the product. Repeating its advice is not checking it.
