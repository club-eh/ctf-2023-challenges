#!/bin/bash

set -e

cd "$(dirname "$(realpath "$0")")"


OUTDIR="../out"


RUSTFLAGS="-C target-cpu=x86-64-v2" cargo build --release

install -pm 644 -t "$OUTDIR" ./target/release/libverify.a

cbindgen --quiet --lang C -o "$OUTDIR"/libverify.h
