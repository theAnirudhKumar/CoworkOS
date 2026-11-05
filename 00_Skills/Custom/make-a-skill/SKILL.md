---
name: make-a-skill
description: >
  Use when the user says "make this a skill," "save this as a skill," "turn this into a skill," or "build a skill for." Also offer it, once and in one line, when the user asks for the same kind of work for the third time, counting this session and what workspace files and handoffs show. Turns a piece of work that went well into a reusable skill. It names the job and confirms it, gathers the steps, inputs, output shape and corrections that made the work succeed, checks for an existing skill that already covers it, drafts a SKILL.md to this template's structural rules, and waits for approval. Then it saves the archive copy to 00_Skills/Custom, adds a row to the Skills Inventory, sets the skill up live if the AI tool has a skill mechanism, and suggests a first test run. It keeps personal details in MEMORY.md or workstation files, so the skill stays reusable.
---

# Make A Skill

Some work comes back again and again: a weekly summary, a type of email, a review done the same way each time. Each time, the user explains the steps again, and makes the same corrections again. A skill writes the method down once. Later sessions follow it without the user explaining anything.

This skill owns the procedure for building a new skill. Root CLAUDE.md owns routing and memory. 00_Reference/Governance Rules.md owns the Skills Rule, which says where a skill's archive copy goes. 00_Reference/File Creation Rules.md owns naming and placement. Read those where the steps below point to them.

---

## When to offer it unprompted

Count requests for the same kind of work. Use what this session shows, plus what workspace files and chat handoffs show about earlier sessions. On the third request, offer once, in one line, for example: "This is the third time we have done this kind of review. Want me to save it as a skill?"

If the user says no, do not offer again for that kind of work. Propose a short entry in root MEMORY.md, or in the workstation's MEMORY.md, recording the decline and its date, so later sessions know not to ask. Write it only if the user approves, per the memory rules in root CLAUDE.md.

## When not to make a skill

- **A one-off task.** If the work is unlikely to come back, a skill only adds a file to maintain. Say so and do the work directly.
- **A rule, not a workflow.** If the thing prescribes behavior in every session ("always," "never," "before X do Y"), it belongs in root CLAUDE.md or a workstation CLAUDE.md. A skill is a set of steps for one kind of job, used when that job comes up. Use the two placement tests in root CLAUDE.md and propose the right file instead.
- **A fact.** A preference or a status belongs in MEMORY.md.

---

## Step 1: Name the job

Write one sentence that says what the skill does, for whom, and what it produces. For example: "Turns a pasted meeting transcript into a one-page summary with decisions and action items." Show it to the user and ask whether it is right. Do not go further until they confirm it.

## Step 2: Gather what worked

Collect the method from the conversation, or from the files that did the work if it happened in an earlier session. Look for:

- **The steps**, in the order they actually happened.
- **The inputs** the work needed: files, pasted text, a connected app, a question asked up front.
- **The output shape:** format, length, headings, where the file was saved and under what name.
- **Corrections the user made.** Each one is a rule the skill should follow from the start. A draft the user rewrote shows what they wanted.
- **What to avoid:** approaches that were tried and dropped, and why.

If an earlier session did the work, read its handoff file and the output files in full. A search inside a file is no substitute for reading it.

## Step 3: Check for an existing skill

Read 00_Skills/Skills Inventory.md. Then check the AI tool's own list of skills, if it has one. If an existing skill already covers this job, or most of it, say which one and propose improving it instead of making a second skill. Two skills for one job make the AI guess which to use.

## Step 4: Draft the SKILL.md

Follow these structural rules.

1. **Folder name** is lowercase words joined by hyphens, such as `meeting-summary`.
2. **Frontmatter** starts the file. `name:` matches the folder name exactly.
3. **`description: >`** is a block that starts with the literal trigger phrases the user would say, in quotes. Then it says what the skill does. Keep it under 1,024 characters. The AI tool often decides whether to use a skill from this text alone, so the triggers come first.
4. **H1** is the folder name in title case, with spaces in place of hyphens, such as `# Meeting Summary`.
5. **Length** stays under 500 lines. Most skills need far fewer.
6. **Steps the AI can follow without the original conversation.** Write for a reader who has never seen the chat that produced the skill. Name files by full path. Spell out each check.
7. **A line on what the skill deliberately does not do.** This keeps it from growing into a chore.
8. **The least it needs to run.** Say which inputs are required and which are optional. If a connected app helps but is not required, say what the skill does without it.

Keep personal details out of the skill. Names, addresses, account details, a client list or a house style belong in MEMORY.md or the workstation's files. The skill points to those files by path, such as "read the sign-off preference in MEMORY.md." This keeps the skill reusable, and it keeps private details in one place.

Write in plain words: short sentences, one idea each, everyday vocabulary, per the Writing Instruction Files rule in 00_Reference/Governance Rules.md. Use the existing skills in 00_Skills/Custom/ as models for format and voice.

A starting shape:

```markdown
---
name: <folder-name>
description: >
  Use when the user says "<trigger one>," "<trigger two>," or "<trigger three>." <What it does, in two or three sentences.>
---

# <Folder Name In Title Case>

<One short paragraph on what the job is and why it is a skill.>

## What it needs

<Required inputs, then optional ones.>

## Step 1: <First step>

<What to do, in plain words.>

## What this deliberately does not do

<One or two lines.>
```

## Step 5: Show the draft and wait

Show the whole draft, the folder name, and where it will be saved. Ask for approval. Do not save anything before the user says yes. If they ask for changes, make them and show the draft again.

## Step 6: Save the archive copy

Once approved:

1. Save the file to `00_Skills/Custom/<name>/SKILL.md`.
2. Add a row to the Inventory table in `00_Skills/Skills Inventory.md`, with the skill name, type Custom, the archive path, and a one-line note.
3. Add a row to the Skills table in root CLAUDE.md with the trigger phrases and the file path, so every future session can find it even where the skill is not installed.

This follows the Skills Rule in 00_Reference/Governance Rules.md. The archive copy is the recovery path if the live skill is ever lost.

If the skill is someone else's work rather than one built here, it goes in `00_Skills/Third-Party/<name>/` instead. Copy the whole source folder as it is, with its original LICENSE and README, per `00_Skills/Third-Party/README.md`. Check what the license permits before relying on it.

## Step 7: Set it up as a live skill

What this means depends on the AI tool.

- **If the tool has a skill mechanism,** attempt the setup now, rather than only describing it. The steps differ by tool and change over time, so use the tool's own current method. If you are not sure of the steps, ask the tool directly how to install a skill from a file. See 00_Resources/Using CoworkOS with Other AI Tools.md for tools with a known answer.
- **If the tool has no skill mechanism, or you are not sure,** say so plainly. Then explain how the workspace still gets the same behavior: when the user says a trigger phrase, the AI reads the SKILL.md file from 00_Skills/Custom/ and follows it. This is the same framing first-run setup uses when it offers the template's skills.

Report which of the two happened.

## Step 8: Suggest a first test run

Suggest trying the skill on a real task soon, rather than a made-up example. After the run, ask what needed correcting. Offer to fold each correction back into the skill. Any change updates both the live skill and the archive copy in the same session, and the Inventory row if its note changed.

---

## Rules

- **Approval before saving.** Nothing is written to 00_Skills/ or the Inventory until the user approves the draft.
- **One skill per job.** Improve an existing skill before making a new one.
- **No personal details inside a skill.** Point to the file that holds them.
- **Every live skill has an archive copy.** Save both in the same session.

## What this deliberately does not do

It does not review or rewrite existing skills in bulk, and it does not install skills from outside the workspace on its own. It builds one skill at a time, from work the user has already done and approved.
