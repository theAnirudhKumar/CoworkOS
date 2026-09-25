# Troubleshooting

Problems people actually hit setting this up, in the order they tend to show up.

## My AI tool didn't ask me any setup questions, it just created folders

This usually means the install prompt from the README got skipped or paraphrased. The prompt matters more than it looks: it tells your AI tool to read `CLAUDE.md`, which sends it to `SETUP.md`, the first-run setup, which is what makes it *ask* what areas of life or work you want tracked instead of guessing. If it already created workstations you did not ask for, tell it to delete them and re-read `SETUP.md` before doing anything else. If you typed your own install instructions instead of using the install prompt from the CoworkOS template's README, paste that version instead, it is the one that has actually been tested.

## Nothing happens when I say "run session-audit" (or any skill name)

Having the file in `00_Skills/Custom/session-audit/SKILL.md` does not make it a runnable skill, that folder is a register and a recovery copy, not where skills execute from. Turning a file into something you can actually invoke is a separate step, and how you do it depends on your AI tool. Ask your tool directly: "read 00_Skills/Custom/session-audit/SKILL.md and set this up as a skill I can invoke going forward" works on any tool that supports the concept at all. If your tool doesn't support installable skills (see `00_Resources/Using CoworkOS with Other AI Tools.md`), ask it to just follow the steps in that file directly when you ask for a session audit, instead of expecting it to register as a reusable skill.

## I don't use git and the setup instructions lost me at the git commands

You don't need to type any git command yourself. For getting the files in the first place, use the **Download ZIP** option on the template's GitHub page instead of `git clone`. For the optional GitHub sync in `00_Resources/GitHub Sync Guide.md`, once you've created the account and the empty repository, hand your AI tool the whole guide and ask it to run the steps for you, that's the tested path. If you do want to type the commands yourself, both guides now say exactly where to open a terminal (Applications > Utilities > Terminal on a Mac, Command Prompt or PowerShell on Windows).

## I turned on the GitHub sync but the identity guard doesn't seem to do anything

The `.gitignore` and `.githooks/pre-commit` files ship inert, they need one activation step to turn on:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
```

Run that once from inside the workspace folder (your AI tool can run it for you). Until you do, the pre-commit hook that checks for ID numbers and account numbers in what you're about to commit simply isn't wired in, git ignores hooks it hasn't been pointed at.

## `git push` failed with something about the remote having work I don't have

This happens if the repository you created on GitHub already has a commit in it, most commonly because you ticked "Add a README" while creating it. Delete that repository and recreate it empty (no README, no `.gitignore`, no license, CoworkOS brings its own), or, if you'd rather keep it, pull first with `git pull origin main --allow-unrelated-histories` before pushing. Either way, this is exactly the kind of step worth handing to your AI tool rather than working through by hand.

## Setup is finished but the workspace still has the template author's files or name in it

First-run setup ends by handing the workspace over: it deletes the template's own README, CHANGELOG, CONTRIBUTING, `validate.py` and `.github/` folder, clears the placeholder example entries, removes any git remote pointing back at the template repository, and finally deletes `SETUP.md` itself. If a workspace was set up before that step existed, or the step got skipped, ask your AI tool to do it now: "delete README.md, CHANGELOG.md, CONTRIBUTING.md, validate.py, and the .github folder; remove the example entries from MEMORY.md and ARCHIVE.md; and if this folder is a git repository, remove any remote that points at the CoworkOS template and ask me whether to delete the template's git history." Keep `LICENSE`, the template's license requires its copyright notice to stay with the copy. The remote matters most: until it is gone, a session-audit sync could try to push your workspace to the template's repository.

## I renamed or deleted Example Workstation and now routing seems broken

Two things need to happen together, and it's easy to do the first without the second. Deleting the folder is only half the change, the Routing Map table near the bottom of root `CLAUDE.md` still has a row pointing at it. Remove that row (or update it to point at whatever replaced it) in the same pass. If your AI tool did the rename or delete for you, ask it to update the Routing Map too, that's the actual cause when routing seems to misfire right after cleaning up the example.

## My AI tool keeps re-asking questions I already answered, or forgets a correction I made

Check whether the fact actually made it into `MEMORY.md` or the relevant workstation's `MEMORY.md`, memory writes in this system require your approval, so a correction you made mid-conversation only sticks if you (or a session-audit pass) confirmed it should be written. If it's genuinely missing, that's what the session-audit skill above is for, run it before ending a session instead of relying on everything getting caught in the moment.

## Everything above and I'm still stuck

Open an issue on the CoworkOS template repository you downloaded this from (its CONTRIBUTING file describes how contributions work) describing what you asked for, what happened, and what your AI tool is. If it's specific to running this on a tool other than Claude Cowork, check `00_Resources/Using CoworkOS with Other AI Tools.md` first, several tool-specific quirks are already documented there.
