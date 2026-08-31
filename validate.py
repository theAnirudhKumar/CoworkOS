#!/usr/bin/env python3
"""
Structural checks for this repository.

Run it before opening a pull request:

    python3 validate.py

It exits non-zero and prints one line per problem. Continuous integration
runs the same script on every pull request, so anything it catches here is
anything that would fail there.

This checks structure, not judgement. It cannot tell you whether a change
keeps the template generic enough for a stranger to adapt. See
CONTRIBUTING.md for the part that needs a person.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

PUNCT = {
    '—': 'em dash',
    '–': 'en dash',
    '‘': 'curly quote',
    '’': 'curly apostrophe',
    '“': 'curly quote',
    '”': 'curly quote',
}
# No "Open"+"AI" collision check here, unlike some sibling repos: this
# template's own compatibility doc has to name real third-party AI companies
# (OpenAI included) to be useful, so that pattern would flag correct content
# rather than a mistake.


def rel(path):
    return os.path.relpath(path, ROOT)


def all_markdown_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if os.sep + '.git' in dirpath:
            continue
        for name in filenames:
            if name.endswith('.md'):
                yield os.path.join(dirpath, name)


def check_punctuation(path, text, bad):
    for ch, name in PUNCT.items():
        n = text.count(ch)
        if n:
            bad.append(f'{rel(path)}: {n} {name}{"s" if n > 1 else ""}')


def check_skill(path, text, bad):
    folder = os.path.basename(os.path.dirname(path))

    m = re.search(r'^name:[ \t]*(.+?)[ \t]*$', text, re.M)
    if not m:
        bad.append(f'{rel(path)}: no name in frontmatter')
    elif m.group(1) != folder:
        bad.append(f'{rel(path)}: frontmatter name "{m.group(1)}" but folder "{folder}"')

    d = re.search(r'^description:[ \t]*>[ \t]*\n(.*?)\n---', text, re.S | re.M)
    if not d:
        bad.append(f'{rel(path)}: no block description in frontmatter')

    h1 = re.search(r'^# (.+)$', text, re.M)
    if h1:
        expected = folder.replace('-', ' ')
        if h1.group(1).strip().lower() != expected.lower():
            bad.append(f'{rel(path)}: H1 "{h1.group(1).strip()}" does not match folder "{folder}"')


def check_root_files(bad):
    required = ['CLAUDE.md', 'MEMORY.md', 'ARCHIVE.md', 'README.md',
                'CONTRIBUTING.md', 'CHANGELOG.md', 'LICENSE']
    for name in required:
        if not os.path.exists(os.path.join(ROOT, name)):
            bad.append(f'missing required root file: {name}')


def check_cross_references(bad):
    """Every 00_Reference and 00_Resources file should be listed in both
    README.md's Structure table and CLAUDE.md's Memory & Governance table,
    so a new reference file does not silently go undiscovered. This is the
    exact drift that happened once: a resource file existed but nothing in
    either root file pointed to it."""
    readme = os.path.join(ROOT, 'README.md')
    claude = os.path.join(ROOT, 'CLAUDE.md')
    if not (os.path.exists(readme) and os.path.exists(claude)):
        return
    readme_text = open(readme, encoding='utf-8').read()
    claude_text = open(claude, encoding='utf-8').read()

    for sub in ('00_Reference', '00_Resources'):
        base = os.path.join(ROOT, sub)
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            if not name.endswith('.md'):
                continue
            marker = f'{sub}/{name}'
            if marker not in readme_text:
                bad.append(f'README.md: Structure table missing {marker}')
            if sub == '00_Reference' and marker not in claude_text:
                bad.append(f'CLAUDE.md: Memory & Governance table missing {marker}')


def main():
    bad = []

    check_root_files(bad)
    check_cross_references(bad)

    for path in all_markdown_files():
        text = open(path, encoding='utf-8').read()
        check_punctuation(path, text, bad)
        if os.path.basename(path) == 'SKILL.md':
            check_skill(path, text, bad)

    if bad:
        print(f'{len(bad)} problem{"s" if len(bad) > 1 else ""}:\n')
        for line in sorted(bad):
            print('  ' + line)
        print('\nRules are in CONTRIBUTING.md.')
        return 1

    print('all checks passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
