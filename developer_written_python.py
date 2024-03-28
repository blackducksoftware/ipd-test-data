#!/usr/bin/env python
"""
Usage: dos_line_endings

Takes stdin, changes all line endings from \r or \n to \r\n, strips UTF-8
byte-order mark (if any), writes to stdout.
"""

import sys
import re

PY3K = sys.version_info >= (3, 0)

if PY3K:
    stdin = sys.stdin.buffer
    stdout = sys.stdout.buffer
else:
    stdin = sys.stdin
    stdout = sys.stdout
    # Python 2 on Windows opens sys.stdin in text mode, and
    # binary data that read from it becomes corrupted on \r\n
    if sys.platform == 'win32':
        # set sys.stdin to binary mode
        import os, msvcrt # NOQA
        msvcrt.setmode(stdin.fileno(), os.O_BINARY)
        msvcrt.setmode(stdout.fileno(), os.O_BINARY)

utf8_bom = b'\xEF\xBB\xBF'
line_ending_re = re.compile(b'\r\n|\r|\n')

input_data = stdin.read()
no_bom = input_data
if input_data.startswith(utf8_bom):
    no_bom = input_data.replace(utf8_bom, b'', 1)

stdout.write(line_ending_re.sub(b'\r\n', no_bom))
if not no_bom.endswith(b'\r\n'):
    stdout.write(b'\r\n')
