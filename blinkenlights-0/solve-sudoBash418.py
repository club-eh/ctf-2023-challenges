#!/usr/bin/env python3

from typing import Iterator

from enum import Enum
from functools import reduce
from pathlib import Path

from PIL.Image import Image
import av


# global settings (configurable via CLI)
DEBUG = False
BATCH_DECODE = False


# LED pixel coordinates
RLED_COORDS = (233, 550)
GLED_COORDS = (250, 550)

# LED color thresholds (works for both RGB and grayscale videos)
RLED_THRESHOLD_HI = 245
RLED_THRESHOLD_LO = 215
GLED_THRESHOLD_HI = 245
GLED_THRESHOLD_LO = 215

# LED channels
RLED_CHANNEL = 1  # use green channel because red is very high even when LED is off
GLED_CHANNEL = 1


class LEDSymbols(Enum):
	RED = 0
	GREEN = 1


def extract_symbols(fp: Path) -> Iterator[LEDSymbols]:
	"""Extracts the raw LED low-to-high transition symbols from a video."""

	# open the video
	container = av.open(fp.open("rb"))

	if BATCH_DECODE:
		# enable higher throughput frame decoding
		container.streams.video[0].thread_type = "AUTO"

	# initialize LED statuses
	rled_on = gled_on = False

	# iterate over each frame in the video
	for frame in container.decode(video=0):
		img: Image = frame.to_image()

		# get LED values
		rval = img.getpixel(RLED_COORDS)[RLED_CHANNEL]
		gval = img.getpixel(GLED_COORDS)[GLED_CHANNEL]

		# handle RLED
		if rled_on:
			# check for transition
			if rval < RLED_THRESHOLD_LO:
				rled_on = False
		else:
			# check for transition
			if rval > RLED_THRESHOLD_HI:
				rled_on = True
				# emit red signal
				yield LEDSymbols.RED
				if DEBUG:
					print(f"RLED signal at frame {frame.index}")

		# handle GLED
		if gled_on:
			# check for transition
			if gval < GLED_THRESHOLD_LO:
				gled_on = False
		else:
			# check for transition
			if gval > GLED_THRESHOLD_HI:
				gled_on = True
				# emit green signal
				yield LEDSymbols.GREEN
				if DEBUG:
					print(f"GLED signal at frame {frame.index}")

def decode_led_symbols(symbols: Iterator[LEDSymbols]) -> bytes:
	# initialize output buffer
	buf = bytearray()

	# create working bit buffer
	bitbuf: list[bool] = []

	# iterate over LED symbols
	for sym in symbols:
		match sym:
			case LEDSymbols.GREEN:
				bitbuf.append(False)
			case LEDSymbols.RED:
				bitbuf.append(True)

		# flush bit buffer to output if it's full
		if len(bitbuf) > 7:
			buf.append(reduce(lambda x, y: (x << 1) | y, bitbuf, 0))
			bitbuf = []

	# warn if bit buffer isn't empty
	if len(bitbuf):
		print("WARNING: bit buffer has an incomplete byte remaining!")

	return bytes(buf)


if __name__ == "__main__":
	import argparse
	import sys

	parser = argparse.ArgumentParser()
	parser.add_argument("filepath", type=Path, help="Path to the video recording to analyze.")
	parser.add_argument("--debug", "-d", action="store_true", help="Enable debugging output.")
	parser.add_argument("--batch-decode", "-b", action="store_true", help="Enable a higher throughput (but higher latency) decoding method.")
	args = parser.parse_args()

	if args.debug:
		DEBUG = True

	if args.batch_decode:
		BATCH_DECODE = True

	if not args.filepath.exists():
		print(f"ERROR: file does not exist: '{args.filepath}'", file=sys.stderr)
		raise SystemExit(1)

	print(decode_led_symbols(extract_symbols(args.filepath)))
