#!/bin/bash

set -e

cd "$(dirname "$(realpath "$0")")"


OUTDIR="../out"


RUSTFLAGS="-C target-cpu=x86-64-v2" cargo build --release
cargo build --release --target=aarch64-unknown-linux-gnu

install -pm 644 ./target/release/libverify.a "${OUTDIR}/libverify.a"
install -pm 644 ./target/aarch64-unknown-linux-gnu/release/libverify.a "${OUTDIR}/libverify-arm64.a"

cbindgen --quiet --lang C -o "$OUTDIR"/libverify.h
