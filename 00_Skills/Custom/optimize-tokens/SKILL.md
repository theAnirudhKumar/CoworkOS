---
name: optimize-tokens
description: >
  Use when the user says "optimize tokens," "reduce tokens," "token efficient," or "how do I prompt this better," or asks how to get the same result with less back-and-forth. Also use proactively, at most once per task, when a request is clearly heavy and a leaner version would save a lot: many files read when a few would do, a whole document pasted when one section would do, a vague ask that will cause rounds of clarification, a full rewrite when targeted edits would do, or context repeated that was already given. Shows a leaner version of the request and its quality impact, then asks before proceeding. Quality comes first: published or external output is never cut.
---

# Optimize Tokens

Everything the AI reads and writes is measured in tokens, and more tokens means a slower, costlier response that sits closer to the limit of what the AI can hold at once.

This skill helps the user get the same result with less waste. The aim is fewer wasted round trips, less repeated context, and tighter requests. The output itself stays as good as it needs to be. A cheaper answer that is wrong costs more than an expensive one that is right, so quality always comes first.

---

## When this skill runs

### Explicit request

The user asks to optimize tokens, reduce tokens, be token efficient, or prompt something better. Look at their current or next request and show a leaner version that reaches the same outcome, using the suggestion block below.

### Proactive flag

Flag a request on your own only when it is clearly heavy and the saving would be large. Do this at most once per task, before starting the work. These are the signals worth flagging:

- Reading many files when a few would answer the question.
- A whole document pasted when only one section matters.
- A vague ask that will lead to several rounds of clarification.
- A full rewrite requested when a few targeted edits would do.
- Context repeated that was already given earlier in the session.
- Several separate asks that could be batched into one message.

If a request is only slightly heavy, do the work and say nothing. A small saving is not worth interrupting the user.

---

## Two gates before suggesting anything

### Gate 1: Quality

Decide what quality the output needs, from context or by asking. Published or external output, such as anything another person will read, is never cut, so proceed in full. Internal drafts and exploratory work welcome optimization. Quick personal use, such as a note for the user alone, can be optimized aggressively. If the purpose is unclear, ask: "This looks like [type of output]. Should I keep it lean, or does it need full quality?"

### Gate 2: Complexity

Some tasks are heavy by nature, because they need full context, many files, or long output to be done well. If the task cannot be made lighter without losing something that matters, say so in one line and proceed without optimizing. For example: "This needs the full set of files to be done well, so I'll go ahead as asked."

---

## The suggestion block

Show every suggestion in this format, and keep it tight.

**What was asked:**
> [the original request, or a short paraphrase of it]

**Why it is heavy:**
One or two sentences on what drives the token cost.

**Leaner version:**
> [the rewritten request, concrete and scoped]

**What changes:**
What gets cut, and why that does not hurt the result.

**Quality impact:** None, Minimal or Moderate, with a short note.

Then ask whether to go ahead with the leaner version or the original.

---

## Six patterns that save tokens

### 1. Scope the input

Send the part that matters instead of the whole thing. "Here is my full report draft, give me feedback" becomes "Here is the summary section of my report draft. What is unclear or missing?"

### 2. Specify the output format

Say the shape of the answer up front, so it arrives right the first time. "Can you help me with this trip?" becomes "Give me a three-day plan for the trip as a table, one row per day, with a morning, afternoon and evening column."

### 3. Refer back instead of re-pasting

If something was already shared in this session, point to it by name. "Use the budget table from earlier" costs far less than pasting the table again.

### 4. Batch the asks

Combine related requests into one message. "Review the budget categories, flag anything over last month, then suggest two cuts" is cheaper than three separate messages.

### 5. Constrain open-ended questions

Give a broad question a frame. "What should I do about my monthly spending?" becomes "Give me three options to cut monthly spending by about ten percent, as a short list with the trade-off for each."

### 6. Point to a workspace file

If a person, project or preference is already written down, point to it instead of explaining it again. "The goals are in this workstation's MEMORY.md" replaces a paragraph of background. The workspace exists so that context does not have to be repeated in every chat.

---

## What never to optimize

Some things protect quality, so leave them alone. Context that is genuinely new and has not been given before stays in. Creative or strategic work keeps its room, because there the exploration is the point. Output that is published, external or high-stakes stays at full quality. A task the user has already confirmed needs full treatment is done in full, without a second suggestion.

---

## Tone

Be direct and brief. Give one flag, one rewrite and one confirmation, then move on with whichever version the user picks. Skip any lecture about token use; the user needs a better request and a green light, nothing more.
