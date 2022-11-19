# container image used for compiling the binary
TOOLCHAIN_IMAGE := "docker.io/library/rust:1.65"
# name of the main binary
BIN_NAME := "hacking-through-time"
# output path
OUTFILE := "out" / BIN_NAME


default: build install info

# build the binary
build:
	# encode flag into Rust source code
	python encode_flag.py $(<flag.txt) src/constants.rs

	# compile the binary
	podman run -it --rm -w /build -v ./:/build/ {{TOOLCHAIN_IMAGE}} \
		cargo build --release

	install -DTpm755 ./target/release/{{BIN_NAME}} {{OUTFILE}}

# "install" the binary to static/
install:
	install -Dpm755 -t ../static {{OUTFILE}}

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
