#!/usr/bin/env python3
"""Packs the game files into index.data for the web build.

    python3 pack_game_files.py <game folder> [index.js] [index.data]

<game folder> is a Windows or Linux folder of the port with the original game's
files in it (ROADRASH.EXE, AUDIO, DATA, IMAGES, TEXT, port/assets). index.js
(default: beside this script) lists every file with its place in index.data;
the files are written in that order and their sizes must match the list.
Names are found whatever their upper or lower case."""
import os
import re
import sys


def find(root, path):
    here = root
    for part in path.strip('/').split('/'):
        try:
            names = os.listdir(here)
        except OSError:
            return None
        match = part if part in names else next((n for n in names if n.lower() == part.lower()), None)
        if match is None:
            return None
        here = os.path.join(here, match)
    return here


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    beside = os.path.dirname(os.path.abspath(__file__))
    root = sys.argv[1]
    script = sys.argv[2] if len(sys.argv) > 2 else os.path.join(beside, 'index.js')
    out = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(os.path.abspath(script)), 'index.data')
    text = open(script, encoding='utf-8', errors='replace').read()
    listed = re.search(r'loadPackage\(\{files:\[(.*?)\],remote_package_size:(\d+)\}\)', text, re.S)
    if not listed:
        sys.exit('no file list in ' + script)
    files = [(n, int(a), int(b)) for n, a, b in re.findall(r'\{filename:"([^"]+)",start:(\d+),end:(\d+)\}', listed.group(1))]
    total = int(listed.group(2))
    problems = []
    for name, start, end in files:
        path = find(root, name)
        if path is None:
            problems.append('missing: ' + name.lstrip('/'))
        elif os.path.getsize(path) != end - start:
            problems.append('%s is %d bytes, the program expects %d' % (name.lstrip('/'), os.path.getsize(path), end - start))
    if problems:
        sys.exit('\n'.join(problems[:20]) + ('\n(%d problems)' % len(problems)) + '\nindex.data was not written')
    at = 0
    with open(out + '.part', 'wb') as packed:
        for name, start, end in files:
            if start != at:
                sys.exit('the file list in %s has a gap at %s' % (script, name))
            packed.write(open(find(root, name), 'rb').read())
            at = end
    if at != total:
        sys.exit('the file list ends at %d, the program expects %d bytes' % (at, total))
    os.replace(out + '.part', out)
    print('%s: %d files, %d bytes' % (out, len(files), total))


if __name__ == '__main__':
    main()
