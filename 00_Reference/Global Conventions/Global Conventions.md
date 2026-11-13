# Global Conventions

*One rulebook per connected tool, connector or plugin. Read the rulebook for a tool before using that tool, as the Rulebooks table in root CLAUDE.md says.*

A connector only gives your AI tool access. A rulebook says how you want that access used: defaults, limits, and the mistakes to avoid. Keeping each tool's rules in its own file means a session loads only the rulebook the task needs, and root CLAUDE.md stays short.

## Rulebooks

The list below starts with one example. Replace it with your own as you connect tools.

- `Calendar.md`: an example rulebook for a calendar connector. Edit it to match how you work, or delete it if you do not use a calendar connector.

## How to add a rulebook

1. When you connect a new tool, connector or plugin, create `00_Reference/Global Conventions/<Tool name>.md`. Use a stable name with no date, as the File Creation Rules say for files in `00_Reference/`. Start the file with an H1 title that matches the file name.
2. Ask the user how they want the tool used. Draft the first rules from how they already use it, and ask about anything missing. Write a rule only when the user has said it or confirmed it.
3. Add a row to the Rulebooks table in root CLAUDE.md saying when to read it. Changing root CLAUDE.md follows the Change Log rule in `00_Reference/CLAUDE.md Change Log.md`.
4. Add the file to the list above.
5. When a correction or a new preference about that tool comes up in a session, add it to its rulebook, not to root CLAUDE.md.
