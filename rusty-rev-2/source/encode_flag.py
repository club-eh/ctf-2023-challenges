#!/usr/bin/env python3

"""Encodes the given flag into the source code of `libverify`."""

from typing import Literal
import io


# FNV-1a 64-bit constants
FNV_1A_BASIS = 0xcbf29ce484222325
FNV_1A_PRIME = 0x00000100000001b3


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


def fnv_1a_64bit_padded(data: bytes) -> int:
	"""Calculates the FNV-1a 64-bit hash of a bytestream."""

	buf = bytearray(data)
	buf.extend([0 for _ in range(8)])

	val = FNV_1A_BASIS

	for idx in range(0, len(data)+1, 8):
		elem = int.from_bytes(buf[idx:idx+8], 'big')

		val ^= elem
		val = (val * FNV_1A_PRIME) % (2 ** 64)  # wrap to 64-bit int

	return val


def encode(flag: bytes) -> str:
	if len(flag) % 2 == 1:
		raise Exception("Flag length must be divisible by 2!")

	FLAG_HALFLEN = len(flag) // 2

	rc = RustConstants()

	rc.write_int("FLAG_LEN", "usize", len(flag))

	rc.write_int("FLAG_FNV", "u64", fnv_1a_64bit_padded(flag))

	rc.write_u8_array("FLAG_BLOCK_XOR", bytes(flag[i] ^ flag[i + FLAG_HALFLEN] for i in range(FLAG_HALFLEN)))

	rc.write_u8_array("FLAG_STRIPE_XOR", bytes(flag[i*2] ^ flag[i*2+1] for i in range(FLAG_HALFLEN)))

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
