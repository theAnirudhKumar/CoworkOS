# Visual Standards

*Read before producing or reviewing anything with visual structure: step-by-step instructions, tables, diagrams, screenshots, or a generated document such as a PDF, a Word file or a slide deck.*

---

## General Principles

- **Clarity first.** Every table, diagram or layout should make the content easier to understand. Structure that only looks organised is noise.
- **Consistency across outputs.** When producing several items of the same kind in one session, such as three diagrams or two walkthroughs, give them the same format.
- **Label everything.** Tables have headers. Diagrams have titles. Steps have numbers. Screenshots have captions when the context is not obvious.
- **Show it rather than describe it.** In a guide or reference document, give the reader something to look at: an example table, a sample layout, a rendered option. A written description of a layout is a placeholder until the real thing is there.

---

## Step-by-Step Instructions

1. Number every step with `1.`, `2.`, `3.`, never bullets or letters.
2. Give each step exactly one action. If a step needs two actions, split it into two steps.
3. Start each step with a verb: "Click Settings," "Open the file," "Paste the value."
4. Put a clarification for a step as an indented bullet under it, rather than a nested numbered list.
5. State the expected result when it is not obvious: "Click Save. The page reloads and shows a confirmation."

---

## Tables

- Every table has a header row with short, clear column labels in title case. Cell text uses sentence case.
- Left-align text columns (`:---` in markdown). Centre only short values such as numbers, ratings or one-word statuses. A centred column of sentences is hard to read.
- Keep each cell to one or two sentences. Put longer detail in a section and point to it.
- Use a table for comparisons, mappings and reference data. Content that reads as an argument or a story works better as prose.
- Keep tables to about five columns. Six or more will not fit a portrait page, so split the table or give it a landscape page.

### Tables in generated documents

Markdown alignment rarely survives conversion into a Word file, a PDF or slides. When a table is going into a generated file:

- **Set column widths on purpose, in proportion to the content.** Converters tend to make every column the same width, so a one-word label gets as much room as a paragraph.
- **Set alignment for each column on purpose.** Converters often centre every cell.
- Make the header row bold and shaded, and repeat it on each page.
- Keep rows from splitting across a page break, and keep a short table on one page.
- **Render the output and look at it before delivering.** Convert to PDF, look at the pages as images, and check them. A file that opens without an error can still look wrong, and looking at the pages is the only check that reliably catches it.

---

## Screenshots

- Give every screenshot a caption that says what it shows and why it matters.
- When a screenshot is annotated, also describe the annotation in words, so the point survives without the highlight.
- Use the exact label shown on screen when naming a button or menu item. Do not paraphrase it.

---

## Diagrams and Flowcharts

- Give every diagram a title.
- Keep one flow direction per diagram: top to bottom, or left to right.
- Use the same shape for the same kind of thing: diamonds for decisions, rectangles for actions, rounded rectangles for start and end.
- Label an arrow whenever its direction alone does not explain the relationship.
- Keep one level of nesting. A sub-process complex enough to need its own detail gets its own diagram.

---

## Headings and Emphasis

- One H1 per file, for its title. H2 for major sections, H3 for subsections. Never skip a level.
- Use **bold** for a term being defined, a key idea or a critical instruction, and sparingly.
- Use `code formatting` for file paths, file names, commands and any text that should be typed or copied exactly.
- Use a bold lead sentence or a quote block for a warning or an exception that would cause a mistake if missed.
