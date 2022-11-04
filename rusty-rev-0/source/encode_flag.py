#!/usr/bin/env python3

"""Encodes the given flag into the source code of `libverify`."""

from typing import Literal
import io


class RustConstants:
	"""Utility class for easily writing Rust constants."""

	# Rust integer types
	TYPES_UINT = Literal["u8", "u16", "u32", "u64", "usize"]
	TYPES_SINT = Literal["i8", "i16", "i32", "i64", "isize"]
	TYPES_INT = Literal[TYPES_UINT, TYPES_SINT]

	def __init__(self, prefix: str = "pub(crate) ") -> None:
		self.prefix = prefix
		self.sio = io.StringIO()

	def get_value(self) -> str:
		return self.sio.getvalue()

	def write(self, data: str):
		"""Write an arbitrary string."""
		self.sio.write(data)

	def write_int(self, name: str, type: TYPES_INT, value: int):
		"""Write the given integer with the given type."""
		self.sio.write(self.prefix)
		self.sio.write(f"const {name}: {type} = {value};\n")

	def write_u8_array(self, name: str, data: bytes):
		"""Write the given byte array as an array of u8 integers."""
		self.sio.write(self.prefix)
		self.sio.write(f"const {name}: [u8; {len(data)}] = {list(data)!r};\n")


XOR_KEY = 0b01011001


def encode(flag: bytes) -> str:
	rc = RustConstants()

	rc.write_int("FLAG_LEN", "usize", len(flag))

	rc.write_int("XOR_KEY", "u8", XOR_KEY)

	rc.write_u8_array("ENCODED_FLAG", bytes(c ^ XOR_KEY for c in flag))

	return rc.get_value()


if __name__ == "__main__":
	import argparse

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
