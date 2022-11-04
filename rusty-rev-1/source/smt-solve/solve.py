#!/usr/bin/env python3

import re

import attrs
import claripy


# known flag prefix
FLAG_PREFIX = b"clubeh{"


@attrs.define
class BinaryConstants:
	FLAG_LEN: int
	FLAG_STRIPE_XOR: list[int]
	FLAG_BLOCK_XOR: list[int]

	@classmethod
	def _from_constants_rs(cls, filepath: str) -> "BinaryConstants":
		"""Parses the `constants.rs` file from the libverify source code."""

		RE_ARRAY = re.compile(r"const (?P<name>\w+): \[u\d+; \d+\] = \[(?P<values>[\d, ]+)\];$", re.MULTILINE)
		RE_UINT = re.compile(r"const (?P<name>\w+): u(?:\d+|size) = (?P<value>\d+);$", re.MULTILINE)

		with open(filepath) as fp:
			raw = fp.read()

		parsed: dict[str, int | list[int]] = dict()
		for match in RE_UINT.finditer(raw):
			parsed[match.group('name')] = int(match.group('value'))
		for match in RE_ARRAY.finditer(raw):
			parsed[match.group('name')] = [int(strval) for strval in match.group('values').split(',')]

		return cls(
			FLAG_LEN = parsed["FLAG_LEN"],
			FLAG_STRIPE_XOR = parsed["FLAG_STRIPE_XOR"],
			FLAG_BLOCK_XOR = parsed["FLAG_BLOCK_XOR"],
		)


def solve():
	# get constants
	constants = BinaryConstants._from_constants_rs("../libverify/src/constants.rs")
	# shorter alias
	FLAG_LEN = constants.FLAG_LEN


	# create solver
	solver = claripy.Solver()

	# create symbolic variables
	flag_chars = [claripy.BVS(f"char_{i}", 8) for i in range(FLAG_LEN)]
	flag_str = claripy.Concat(*flag_chars)


	# constrain to ASCII
	for char in flag_chars:
		solver.add(char >= 0x20)
		solver.add(char < 0x7f)

	# constrain prefix
	for known_char, char in zip(FLAG_PREFIX, flag_chars):
		solver.add(char == known_char)

	# simplify
	solver.simplify()


	# constrain stripe XORs
	for i in range(0, FLAG_LEN // 2):
		solver.add(flag_chars[i*2] ^ flag_chars[i*2+1] == constants.FLAG_STRIPE_XOR[i])

	# constrain block XORs
	for i in range(0, FLAG_LEN // 2):
		solver.add(flag_chars[i] ^ flag_chars[i+(FLAG_LEN//2)] == constants.FLAG_BLOCK_XOR[i])

	# simplify
	solver.simplify()


	for solution in solver.eval(flag_str, 3):
		print(f"Found solution: {solution.to_bytes(FLAG_LEN, 'big')}")


	from IPython import embed; embed()


if __name__ == "__main__":
	solve()
