#!/bin/bash

# A solve using GDB for dynamic analysis.
# The binary decodes the flag and then compares it to the input - meaning we can read the plaintext flag directly out of memory.

set -e

EXE="../out/flag-checker"


gdb --batch --command get-flag.gdbscript --args "$EXE" 0123456789012345678901234567890123456789
