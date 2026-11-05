# Mobile Capture Guide

*Read when the user wants to jot things down from their phone, or asks how to reach their second brain away from the computer.*

A second brain only works if a thought can get into it in a few seconds, wherever you are. Most good ideas, tasks and reminders turn up away from the computer. This guide sets up a way to send them in from a phone, so they are waiting in your inbox the next time you sit down.

There are three ways to do it. Pick the first one that fits; you can add another later.

| Path | Best for | Needs |
| :--- | :--- | :--- |
| 1. Synced folder | Most people, and iPhone users especially | Your workspace kept in a cloud-synced folder |
| 2. Email to yourself | Any phone, no setup on the phone | An email connector in your AI tool |
| 3. GitHub sync and travel mode | Doing real work from the phone, not only capturing | A private GitHub repository and an AI tool that can use it |

Whichever path you use, phone captures land in your inbox and wait there. The weekly review files each one into the right place, or turns it into a task, or drops it.

---

## Path 1: Synced folder

Keep your workspace inside a folder your phone can also see, such as iCloud Drive or another cloud storage folder that syncs to your computer. Your AI tool keeps working from the same folder on your computer, as before.

Your phone writes to one file only: `98_Temp/Phone Inbox.md`. The AI never edits that file except during the weekly review, when it moves each line to its home and empties the file. Keeping the phone and the AI on separate files means they never write to the same file at the same moment.

Each capture is one line in this form, which the dashboard and the daily brief read:

```
- [YYYY-MM-DD] the thought
```

If the date is missing, the line still counts; it just shows without one.

### On an iPhone: a one-tap shortcut

The Shortcuts app that comes with the iPhone can add a line to a file in iCloud Drive. Set it up once, then capture from your home screen, or by asking Siri using the shortcut's name.

1. Make sure your workspace is in its own folder at the top level of iCloud Drive, such as `iCloud Drive/My Second Brain`. Shortcuts is most reliable with a folder you created at the top level.
2. Open Shortcuts and create a new shortcut. Name it something you would say, such as "Capture".
3. Add the action **Ask for Input**, type Text, with the prompt "What's on your mind?"
4. Add **Format Date**, set to Current Date, with a custom format of `yyyy-MM-dd`.
5. Add **Text**, and build the line: a hyphen and a space, then `[`, the Formatted Date, `]`, a space, then Provided Input.
6. Add **Append to Text File**. Choose iCloud Drive, set the file path to `/My Second Brain/98_Temp/Phone Inbox.md` (using your own folder name), and turn on making a new line.
7. Run it once and check the line appears in the file on your computer. iCloud can take a little while to sync, so give it a minute before deciding it failed.
8. Add the shortcut to your home screen.

If the shortcut cannot write to your folder, the cause is usually the folder's location. Move the workspace to a folder at the top level of iCloud Drive and update the path, or ask your AI tool to help you check it.

### On any phone: a notes or text app

Any app on your phone that can open and edit a plain text file in your cloud folder works. Open `98_Temp/Phone Inbox.md`, add a line at the bottom in the form above, and save. Some apps can also add a home-screen shortcut straight to one file, which makes this nearly as fast as the iPhone shortcut.

---

## Path 2: Email to yourself

Send yourself an email whose subject starts with `Inbox:`, such as "Inbox: book the dentist". The rest of the subject, and the first line of the body if there is one, is the capture.

This needs an email connector in your AI tool (see 00_Resources/Connectors Guide.md). The weekly review searches for these emails, adds each one to `98_Temp/Inbox.md` as a dated line, and records how far it has imported, so nothing is added twice. It only reads your mailbox and never moves, labels or deletes the emails, so tidy them in your email app whenever you like.

To turn it on, tell your AI tool: "Set up email capture." It records a line in the Scheduled Tasks section of root MEMORY.md, "Email capture, root, read at weekly review, imported up to [date]", which is how later sessions know to look.

---

## Path 3: GitHub sync and travel mode

If you already sync your workspace to a private GitHub repository, the travel-mode skill lets an AI tool on your phone work from that copy and push the changes back. That covers far more than capture, but it needs a GitHub token and an AI tool that can use it. See 00_Resources/GitHub Sync Guide.md and 00_Skills/Custom/travel-mode/SKILL.md.

---

## When captures do not show up

- **The line is in the file on the phone but not on the computer.** Sync has not caught up yet. Open the cloud folder on the computer, or wait a few minutes.
- **The dashboard does not count a capture.** Check the line starts with a hyphen and a space. The date in square brackets is optional.
- **Two copies of the file appear, one marked as conflicted.** The phone and the computer both changed it while offline. Ask your AI tool to merge the two into `Phone Inbox.md` and delete the extra copy.
- **Email captures never arrive.** Check the email connector is still signed in, and that the subject starts with exactly `Inbox:`.
