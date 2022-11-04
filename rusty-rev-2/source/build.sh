#!/bin/bash

set -e
cd "$(dirname "$(realpath "$0")")"


FLAG="$(<flag.txt)"


# validate flag length (required for the XORs to constrain the solution space properly)
if ((${#FLAG} % 4 == 0)); then
	echo "  => Flag length is valid"
else
	echo "  => Flag length is invalid!"
	exit 1
fi


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
	# remove Rust stdlib symbols
	#readelf -sW flag-checker | grep -E '_ZN3std\w+' -o | xargs -i strip flag-checker -N {}
)

echo "  => Installing flag-checker..."
(
	install -pm755 -t ../static ./out/flag-checker
)

echo "  => Done"
(
	ls -l --color ./out/flag-checker
)
