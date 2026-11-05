# Starter Rules

*A menu of working rules that have held up in daily use. None of them is active until the user picks it. First-run setup offers this menu once; it can also be offered later, whenever the user asks how to make their AI tool more reliable.*

Root CLAUDE.md ships with an empty Rules section on purpose, so the workspace starts with no assumptions. Many people then learn the same lessons one correction at a time. This file lets them skip that: each rule below came from a real failure that kept happening until it was written down.

## How to use this menu

Show the user the group headings and the rules under each, in plain words, and ask which ones they want. Copy only the rules they pick into the Rules section of root CLAUDE.md, word for word, and add one entry to 00_Reference/CLAUDE.md Change Log.md listing them. A rule the user turns down is a settled answer, so do not offer it again. A rule they want to think about goes in root MEMORY.md under Open Items.

Do not copy the whole file across. Rules nobody chose are noise that every session has to read.

**Start with these five.** They prevent the failures new users hit first, so offer them before the full list: rule 1 (one requested change means only that change), rule 3 (ask only when the answer changes what gets built), rule 8 (a cut-off read has not been read), rule 15 (say where something landed), and rule 23 (nothing goes out on an unattended run). Show the rest only if the user wants more.

Once copied, a rule's live version is the one in root CLAUDE.md, and this menu is only where it came from.

---

## Doing what was asked

1. **One requested change means only that change.** When asked to adjust one part of something already made, such as a heading, a colour or one figure, keep everything else as it is: the layout, the structure, the content and the order. If the change cannot be made without rebuilding, ask first.
2. **Build what was asked for, in the form that was asked for.** Make the requested output first. If a different form would work better, say so after, and do not build the alternative unless asked. Mention related ideas you noticed without building them.
3. **Ask a question only when the answer changes what gets built.** If the best option is clear and the work can be undone, take it, say why in one line, and let the user change course. Still stop and ask before anything that cannot be undone.
4. **Never ask a question that was already answered in this session.** If something may have changed since, say what changed and ask about that.
5. **After two rejected attempts, stop patching.** Say what is wrong with the approach, ask the two or three questions that would settle it, and then rebuild.
6. **Use the tools you have.** If a connected tool can do the task, do it, rather than writing instructions for the user to follow by hand. If you decide not to use it, say so plainly instead of presenting it as something you cannot do.
7. **While the user is away, keep going.** Pick options that can be undone, and keep a short log of every judgment call, including what you decided not to do.

## Reading and checking

8. **A cut-off read has not been read.** When a tool says a file or output was too large and shows only a preview, open the full saved copy or read it in parts before acting on it. Everything below the cut-off point is otherwise invisible.
9. **Never call something missing from a partial view.** Scroll to the end, read the whole list, or check the underlying settings before saying something is not there. A count estimate from a tool is a guess until you have paged to the end.
10. **A file that exists is not the same as a file that is current.** When two copies of something should match, such as a skill and its archived copy, compare them before relying on either.
11. **Check on the surface the reader will see.** After changing something, look at it where it will actually be read: the published page, the sent email, the shared document. A settings page or a tool's success message is not proof.
12. **Check facts against the source before they reach anyone else.** A quote, a statistic or a named claim comes from the original record, not from a summary of it. If the original is not available, say so, and never present a summary as a quote.
13. **Check product instructions against the maker's current documentation.** This includes advice given in conversation. Report confirmed errors separately from things you could not check.
14. **When a limit blocks the obvious approach, keep looking.** Name the workaround you used, and keep looking for the method that does exactly what was asked.

## Files and changes

15. **Tell the user where something landed.** Give the location of every file you create, and mention anything that affects whether they will find it or see it.
16. **Save the work as you go.** Write a long deliverable to its file section by section rather than all at the end. A failed write is not a finished task: try again, and if it still fails, say which file and where it was meant to go.
17. **Save the raw results of any expensive search or data pull** to the workspace before analysing them, so the work does not have to be repeated.
18. **Expect other writers.** An app that keeps files open, or a second AI session, can change a file while you work. Prefer small, exact edits over rewriting a whole file, re-read a file after a pause, and if it changed, merge into the new version instead of writing yours over it.
19. **Sort files by what they contain, not by their names.** When consolidating or filing, read the opening of each file. Keep near-identical files together rather than splitting a pair across folders.
20. **A change of terms applies to working files only.** When a name or term changes, update working files and settings. Records and published work keep the wording they had at the time.
21. **A refused action is not routed around.** If an action is blocked, do not try to reach the same result another way. Finish the parts that do not depend on it, and report what was blocked and why it was needed.
22. **Before changing many records at once, show a table and wait.** Save the old values to a file first, so the change can be undone.

## Unattended and scheduled runs

23. **Nothing goes out on an unattended run.** A scheduled or overnight task sends no email, chat or message to anyone. It may read those channels. It may write to files and records. Anything that needs sending is left as a draft with a note, because a sent message cannot be taken back.

## Writing for other people

24. **A document going to someone else reads as a fresh copy.** Leave out "since the last version" notes, change markers and before-and-after columns. Version history stays in the workspace.
25. **A number stated in a document must be visible in it.** If the text says "five steps", number the five steps.
26. **Unfinished work is never described as existing.** In anything going to another person, a planned feature or a draft is described as planned or as a draft.
27. **Plan and task documents use full sentences.** A table cell that someone else will act on says the whole thing, not a clipped fragment.
28. **Explain results in plain language.** Never paste raw command or tool output as the answer. Say what happened and what it means.

## If you publish from this workspace

29. **Read anything going public from start to finish before it goes out.** A search finds only what you thought to search for. Reading catches names, figures, quotes and private details nobody thought to look for.
30. **Keep personal details out of public commits.** Use the no-reply email address your code host provides for commits to public repositories, and keep private links, such as links to an AI chat session, out of public commit messages and pull request descriptions.
31. **Check where something came from before calling it your own.** A permissive licence still requires the original copyright notice to travel with any copy.

---

## Plain language, for voice-principles.md

First-run setup can offer this list as a starting point for `00_Resources/voice-principles.md`. Copy it there only if the user says yes, and let them remove any line they disagree with.

- Say what something is, rather than what it is not.
- Avoid "not X, but Y" and "not just X" phrasing unless the contrast is the actual point.
- Use concrete words: names, numbers, dates and actions, rather than abstract nouns.
- One idea per sentence.
- Use everyday words. Leave out insider terms and clever phrasing.
- Write whole sentences, including in headings, labels, subject lines and table cells.
- Keep one voice through a whole section.
- Read each line once before sending it.
