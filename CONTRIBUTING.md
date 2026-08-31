# Contributing

This repository is a template, so the bar for a change is different from a normal project: the question is not just "does this work," but "does this stay generic enough for a stranger to adapt to their own life." A pull request that quietly assumes one country, one AI tool, or one kind of workstation is a regression even if the markdown renders fine.

## Before you write anything

Open an issue first, describing what you want to change and why: use the "Something is wrong" template if a documented step failed, or "Propose a change" for a gap or an addition. Nothing gets edited here without one. This gives a place to agree on scope before any time goes into a draft, and it is the same discipline this repository was built under.

## Workflow

1. Open an issue.
2. Branch off `main`, named `<issue-number>-short-description`.
3. Make the change on that branch.
4. Open a pull request with `Closes #<issue-number>` in the body.
5. A maintainer reads the full diff, not just a summary of it, before merging.
6. Squash or merge (either is fine); delete the branch afterward.

Nothing merges to `main` by a direct push, including from a maintainer. Every change goes through a pull request, so there is always a diff to review before it lands.

## What belongs here, and what does not

This repository is the skeleton, not anyone's real workspace. A pull request should never include:

- A real name, employer, customer name, email address, or file path from someone's actual workspace.
- Content specific to one person's situation dressed up as a general rule. If a rule only makes sense for a narrow case, say so explicitly rather than presenting it as universal.
- An identity guard pattern, filename pattern, or example tuned to one country's document formats without saying which country it covers. `.githooks/pre-commit` and `.gitignore` are explicit about this already; keep new patterns the same way.

## Style, since it is enforced

Run `python3 validate.py` before opening a pull request; continuous integration runs the same script. It checks:

- No em dashes or en dashes. Use a comma, a period, or a parenthetical instead.
- Straight quotes and apostrophes, not curly ones.
- Two-sentence cap on any entry written to `MEMORY.md` or `ARCHIVE.md`: one sentence for the fact, an optional second sentence for why it matters.
- Every markdown file opens with an H1 title matching its filename.
- Prose over bullet lists where either would work. Reach for a list only when the content is genuinely enumerable, not as a default format.

These are the same rules the template teaches an installer to follow inside their own workspace (see `00_Reference/File Creation Rules.md` and `00_Reference/Governance Rules.md`), applied here to the repository itself.

## Adding support for another AI tool

If you want to document how CoworkOS works with a tool not already covered in `00_Resources/Using CoworkOS with Other AI Tools.md`, verify the behavior you are describing rather than assuming it matches another tool's pattern. Link to the tool's own documentation for anything specific to how it reads files or handles memory, and say plainly where you were not able to verify a detail.

## If your AI tool fixes something in a shipped file for you

Sometimes the fastest path through confusing wording in this template is your own AI tool patching its local copy of a file to make sense of it, and that is a completely reasonable thing for it to do in the moment. But a fix that only exists on your machine is a fix nobody else benefits from, and the next person hits the exact same confusion. If this happens to you, open an issue describing what was confusing and what your AI tool changed to work around it, using the "Something is wrong" template. That local patch is often most of a real fix already; someone still has to bring it back here.

## Questions

Open an issue. That is also where a change starts, so there is nowhere else this needs to go.
