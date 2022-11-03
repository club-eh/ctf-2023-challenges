#!/bin/bash

set -eu

OUTDIR="../../out"


GCCFLAGS=(
	-Wall
	-std=gnu11
	-march=x86-64-v2
	# optimizations
	-O2
	-flto
	-fno-plt  # used by Rust, so might as well match
	# linking
	-I"$OUTDIR"  # for libverify.h
	-Wl,--gc-sections  # prune unused static library code
	-Wl,-O,--as-needed,-z,now  # optimizations-ish
)

# security (disabled to avoid distracting players)
#GCCFLAGS+=(
#	-fstack-clash-protection
#	-fstack-protector-strong  # stack canaries
#	-D_FORTIFY_SOURCE=2  # buffer overflow detection
#	-fcf-protection=full  # code flow protection
#)


gcc "${GCCFLAGS[@]}" main.c "$OUTDIR"/libverify.a -o "$OUTDIR"/flag_verifier
