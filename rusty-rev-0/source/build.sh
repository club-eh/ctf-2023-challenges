#!/bin/bash

set -e
cd "$(dirname "$(realpath "$0")")"


FLAG="$(<flag.txt)"


mkdir -p out/


# encode flag into constants
echo "  => Encoding flag into libverify constants..."
(
	python encode_flag.py "$FLAG" ./libverify/src/constants.rs | bat -pl rust
)

echo "  => Building libverify..."
(
	cd libverify/
	./build.sh
)

echo "  => Building flag-checker..."
(
	cd flag-checker/
	./build.sh
)

echo "  => Stripping flag-checker..."
(
	cd out/
	# remove debug info (but leave symbols)
	strip --strip-debug flag-checker
	aarch64-linux-gnu-strip --strip-debug flag-checker-arm64
	# remove Rust stdlib symbols
	#readelf -sW flag-checker | grep -E '_ZN3std\w+' -o | xargs -i strip flag-checker -N {}
)

echo "  => Installing flag-checker..."
(
	install -pm755 -t ../static ./out/flag-checker{,-arm64}
)

echo "  => Done"
(
	ls -l --color ./out/flag-checker{,-arm64}
)
