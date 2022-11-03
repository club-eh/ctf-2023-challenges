#!/usr/bin/env python3

"""Encodes the given flag into the source code of `libverify`."""

from io import StringIO
import argparse


XOR_KEY = 0b01011001


def encode(flag: bytes) -> str:
	sio = StringIO()

	# flag length
	sio.write(f"pub(crate) const FLAG_LEN: usize = {len(flag)};\n")

	# xor key
	sio.write(f"pub(crate) const XOR_KEY: u8 = {XOR_KEY};\n")

	# xor encoded flag
	encoded_flag = bytes(c ^ XOR_KEY for c in flag)
	sio.write("pub(crate) const ENCODED_FLAG: [u8; FLAG_LEN] = {!r};\n".format(list(encoded_flag)))

	return sio.getvalue()


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("flag", action="store")
	parser.add_argument("output_file", action="store")
	args = parser.parse_args()

	text = encode(str(args.flag).encode())

	print(text, end='')

	with open(args.output_file, mode="r") as fp:
		prev_text = fp.read()

	if text != prev_text:
		with open(args.output_file, mode="w") as fp:
			fp.write(text)
