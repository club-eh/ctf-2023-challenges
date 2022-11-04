#!/bin/bash

set -e
cd "$(dirname "$(realpath "$0")")"


FLAG="$(<flag.txt)"


mkdir -p out/


# encode flag into constants
echo "  => Encoding flag into libverify constants..."
(
	python encode_flag.py "$FLAG" ./src/libverify/src/constants.rs | bat -pl rust
)

echo "  => Building libverify..."
(
	cd src/libverify/
	./build.sh
)

echo "  => Building flag_verifier..."
(
	cd src/flag_verifier/
	./build.sh
)

echo "  => Stripping flag_verifier..."
(
	cd out/
	# remove debug info (but leave symbols)
	strip --strip-debug flag_verifier
	# remove Rust stdlib symbols
	#readelf -sW flag_verifier | grep -E '_ZN3std\w+' -o | xargs -i strip flag_verifier -N {}
)

echo "  => Installing flag_verifier..."
(
	install -pm755 -t ../static ./out/flag_verifier
)

echo "  => Done"
(
	ls -l --color ./out/flag_verifier
)
