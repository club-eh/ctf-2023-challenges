#!/bin/bash

set -eu

OUTDIR="../out"


CCFLAGS=(
	-Wall
	-std=c11

	# optimizations
	-O2
	-flto
	-fno-plt  # used by Rust, so might as well match

	# linking
	-I"$OUTDIR"  # for libverify.h
	-L"$OUTDIR"  # for libverify.a
	-Wl,--gc-sections  # prune unused static library code
	-Wl,-O,--as-needed,-z,now  # optimizations-ish

	# security
	#-fcf-protection=full  # code flow protection - doesn't work on ARM64
	# following options are disabled to avoid distracting players
	#-fstack-clash-protection
	#-fstack-protector-strong  # stack canaries
	#-D_FORTIFY_SOURCE=2  # buffer overflow detection
)


x86_64-pc-linux-gnu-gcc -march=x86-64-v2 "${CCFLAGS[@]}" main.c -lverify -o "$OUTDIR"/flag-checker
aarch64-linux-gnu-gcc "${CCFLAGS[@]}" main.c -lverify-arm64 -o "$OUTDIR"/flag-checker-arm64
