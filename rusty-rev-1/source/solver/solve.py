#!/usr/bin/env python3

"""Solve script that doubles as a binary verifier (to ensure there is only one valid input, the original flag)."""

import angr
import claripy


FLAG_TEXT = open("../flag.txt", mode="rb").readline()[:-1]
FLAG_LEN = len(FLAG_TEXT)  # can be determined via static analysis

STDOUT_FIND = b"Flag is correct"
STDOUT_AVOID = b"Flag is incorrect"


def check_found(state: angr.SimState) -> bool:
	return STDOUT_FIND in b''.join(state.posix.stdout.concretize())

def check_avoid(state: angr.SimState) -> bool:
	return STDOUT_AVOID in b''.join(state.posix.stdout.concretize())


def solve(exe: str):
	proj = angr.Project(exe, auto_load_libs=False)

	flag_chars = [claripy.BVS(f"char_{idx}", 8) for idx in range(FLAG_LEN)]
	flag_str = claripy.Concat(*flag_chars)

	state = proj.factory.entry_state(
		args = [exe, flag_str],
		add_options = {
			#angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS,
			#angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY,
			#*angr.options.unicorn,
		},
	)


	simmgr = proj.factory.simulation_manager(state)


	#simmgr.explore(find=check_found, avoid=check_avoid)
	simmgr.explore(find=check_found)

	print(simmgr)


	if len(simmgr.found) == 0:
		print("ERROR: couldn't find any matching states!")
	else:
		# concretize up to 3 valid solutions
		results = simmgr.found[0].solver.eval_upto(flag_str, cast_to=bytes, n=3)

		print(f"Results: {results}")

		if len(results) != 1:
			print("ERROR: multiple results found!")
		elif results[0] != FLAG_TEXT:
			print("ERROR: incorrect flag found!")
		else:
			print("Success!")

		if len(simmgr.found) > 1:
			print("WARNING: found multiple matching states!")


	print()
	from IPython import embed; embed()


if __name__ == "__main__":
	from pathlib import Path

	exe = Path(__file__).parent / "../out/flag-checker"

	solve(str(exe))
