#!/usr/bin/env python3

from typing import Iterator

from enum import Enum
from pathlib import Path

from bitstring import BitArray
from PIL.Image import Image
import av


# global settings
DEBUG = False
BATCH_DECODE = False

# LED pixel coordinates
RLED_COORDS = (175, 740)
GLED_COORDS = (200, 740)

# LED color thresholds (works for both RGB and grayscale videos)
RLED_THRESHOLD_HI = 225
RLED_THRESHOLD_LO = 215
GLED_THRESHOLD_HI = 225
GLED_THRESHOLD_LO = 215

# LED channels
RLED_CHANNEL = 1  # use green channel because red is very high even when LED is off
GLED_CHANNEL = 1


class LEDSymbol(Enum):
	RLED_HI = 0
	RLED_LO = 1
	GLED_HI = 2
	GLED_LO = 3


def extract_symbols(fp: Path) -> Iterator[LEDSymbol]:
	"""Extracts the raw LED transition symbols from a video."""

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
				# emit signal
				if DEBUG:
					print(f"RLED LO signal at frame {frame.index}")
				yield LEDSymbol.RLED_LO
		else:
			# check for transition
			if rval > RLED_THRESHOLD_HI:
				rled_on = True
				# emit signal
				if DEBUG:
					print(f"RLED HI signal at frame {frame.index}")
				yield LEDSymbol.RLED_HI

		# handle GLED
		if gled_on:
			# check for transition
			if gval < GLED_THRESHOLD_LO:
				gled_on = False
				# emit signal
				if DEBUG:
					print(f"GLED LO signal at frame {frame.index}")
				yield LEDSymbol.GLED_LO
		else:
			# check for transition
			if gval > GLED_THRESHOLD_HI:
				gled_on = True
				# emit signal
				if DEBUG:
					print(f"GLED HI signal at frame {frame.index}")
				yield LEDSymbol.GLED_HI

def extract_bitstream(symbols: Iterator[LEDSymbol]):
	# initialize output buffers
	buf1 = BitArray()
	buf2 = BitArray()

	gstate = False
	rstate = False

	# iterate over LED symbols
	stream = 1
	for sym in symbols:
		match sym:
			case LEDSymbol.GLED_LO:
				# ignore if RLED is HI (thus we're on stream 2)
				if not rstate:
					# append bit
					buf1.append([False])
			case LEDSymbol.RLED_HI:
				# ignore if GLED is LO (thus we're on stream 2)
				if gstate:
					# append bit
					buf1.append([True])
				elif stream == 1:
					# handle stream transition
					stream = 2
					buf1 = buf1[:-1]  # drop last bit
					if DEBUG:
						print("stream transition 1 -> 2")
			case LEDSymbol.RLED_LO:
				# ignore if GLED is HI (thus we're on stream 1)
				if not gstate:
					# append bit
					buf2.append([False])
			case LEDSymbol.GLED_HI:
				# ignore if RLED is LO (thus we're on stream 1)
				if rstate:
					# append bit
					buf2.append([True])
				elif stream == 2:
					# handle stream transition
					stream = 1
					buf2 = buf2[:-1]  # drop last bit
					if DEBUG:
						print("stream transition 2 -> 1")

		# update stored LED state
		match sym:
			case LEDSymbol.GLED_HI:
				gstate = True
			case LEDSymbol.GLED_LO:
				gstate = False
			case LEDSymbol.RLED_HI:
				rstate = True
			case LEDSymbol.RLED_LO:
				rstate = False

	# drop last erroneous bit of stream 2
	buf2 = buf2[:-1]

	if len(buf1) != len(buf2):
		print(f"WARNING: bitstream lengths do not match! ({len(buf1)} != {len(buf2)})")

	if len(buf1) % 8 != 0:
		print("WARNING: len(buf1) is not divisible by 8!")
	if len(buf2) % 8 != 0:
		print("WARNING: len(buf2) is not divisible by 8!")

	return buf1, buf2


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

	b1, b2 = extract_bitstream(extract_symbols(args.filepath))

	print((b1 ^ b2).bytes)
