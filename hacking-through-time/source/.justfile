# base name of the main binaries
BIN_NAME := "hacking-through-time"
# output path
OUTFILE := "out" / BIN_NAME


default: build install info

# build the binary
build:
	# encode flag into Rust source code
	python encode_flag.py $(<flag.txt) src/constants.rs

	# compile the binaries
	cargo build --release
	cargo build --release --target=aarch64-unknown-linux-gnu

	install -DTpm755 ./target/release/{{BIN_NAME}} {{OUTFILE}}
	install -DTpm755 ./target/aarch64-unknown-linux-gnu/release/{{BIN_NAME}} {{OUTFILE}}-arm64

# "install" the binaries to static/
install:
	install -Dpm755 -t ../static {{OUTFILE}} {{OUTFILE}}-arm64

# remove build files
clean:
	-rm -r ./target
	-rm -r ./out

# display info about the built binary
@info:
	echo
	ls -l --color {{OUTFILE}}
	file -b {{OUTFILE}}
	ldd {{OUTFILE}}
	-checksec --file={{OUTFILE}}
