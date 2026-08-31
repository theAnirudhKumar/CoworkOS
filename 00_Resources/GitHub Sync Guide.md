# GitHub Sync Guide

This is for the optional step in first-run setup: putting this workspace under version control and pushing it to a GitHub repository you own. Nothing about the template requires this. Skip this file entirely if you only ever use CoworkOS from one computer.

## Why you might want this

The main reason is reaching your workspace from somewhere other than your primary computer, most commonly a phone, while you are away from it. If your AI tool has a mobile app or a way to work from a synced copy of a workspace (Claude Cowork's travel mode is one example, documented in `00_Skills/Custom/travel-mode/SKILL.md`), that feature needs somewhere to pull from and push back to, and a GitHub repository you control is that somewhere.

A second reason, independent of mobile access, is simply having a backup and a history. A workspace that only exists on one machine's disk is one spilled coffee away from being gone; a workspace under version control survives that, and you can see what changed and when.

Neither reason requires anyone but you to have access to the repository. Keep it private unless you have a specific reason to share it.

## What this involves

You do not need to know git to follow these steps, but you should understand what you are agreeing to: your workspace's content, including whatever you end up tracking in it (notes, decisions, plans), will live in a GitHub repository under your account. Treat that the same way you would treat any other place you store personal information, private by default, and be deliberate about what you choose to track there in the first place.

### 1. Create a GitHub account, if you do not have one

Go to github.com and sign up. The free tier is enough for this; you do not need a paid plan.

### 2. Create a new repository

From your GitHub account, create a new repository. Give it a name that means something to you. Set its visibility to **Private**, not Public, since this will hold real information about your life or work.

### 3. Connect this workspace to it

From inside the folder where this workspace lives, on the computer where you first set it up:

```bash
git init
git add -A
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

If you have never used git from this computer before, it will ask you to authenticate with GitHub the first time you push. Follow whatever prompt it gives you; a browser-based sign-in is the usual path.

### 4. Turn on the identity guard

This step matters more once your workspace is going to a remote server, not just staying on your own disk. From the same folder:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
```

See `.githooks/pre-commit` itself and the "Protecting what goes in here" section of the main `README.md` for what this catches, and why the example patterns are only a starting point for wherever you live.

### 5. Connect your AI tool to the repository, if it supports it

How this works depends entirely on which tool you use and whether it has a documented way to work from a GitHub-synced copy. Check `00_Resources/Using CoworkOS with Other AI Tools.md` and that tool's own documentation. For Claude Cowork specifically, `00_Skills/Custom/travel-mode/SKILL.md` documents one way to do this.

## Keeping it in sync

Once this is connected, get in the habit of pushing after a session that changed anything (many setups, including the session-audit skill referenced elsewhere in this template, do this automatically as their last step) and pulling before starting a new one on a different device. Working from two unsynced copies at once is how you end up with conflicting versions of the same file.
