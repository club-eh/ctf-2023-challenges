#!/bin/bash

# Solve using a custom library + LD_PRELOAD to replace the bcmp function.

set -e

EXE="../out/flag-checker"


# build the library
gcc -Wall -fPIC -shared -o libreplace.so libreplace.c

# run the binary with the hooked function
LD_PRELOAD=./libreplace.so "$EXE" 0123456789012345678901234567890123456789
