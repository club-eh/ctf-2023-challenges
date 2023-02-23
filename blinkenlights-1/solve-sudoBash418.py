#!/usr/bin/env python3

from typing import Iterator

from enum import Enum
from pathlib import Path
from io import StringIO

from PIL.Image import Image
import av


# global settings (configurable via CLI)
DEBUG = False
BATCH_DECODE = False


# LED pixel coordinates
RLED_COORDS = (207, 550)
GLED_COORDS = (224, 550)

# LED color thresholds (works for both RGB and grayscale videos)
RLED_THRESHOLD_HI = 225
RLED_THRESHOLD_LO = 210
GLED_THRESHOLD_HI = 205
GLED_THRESHOLD_LO = 190

# LED channels
RLED_CHANNEL = 1  # use green channel because red is very high even when LED is off
GLED_CHANNEL = 1

# Minimum # of frames between LED symbols to mark the beginning of a new character
FRAMEDIV_CHARACTER = 12


class LEDSymbol(Enum):
	RLED_HI = 0
	RLED_LO = 1
	GLED_HI = 2
	GLED_LO = 3

class MorseSymbol(Enum):
	DOT = 0
	DASH = 1


def extract_symbols(fp: Path) -> Iterator[tuple[LEDSymbol, int]]:
	"""Extracts the raw LED transition symbols from a video, with frame times."""

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
				yield LEDSymbol.RLED_LO, frame.index
		else:
			# check for transition
			if rval > RLED_THRESHOLD_HI:
				rled_on = True
				# emit signal
				if DEBUG:
					print(f"RLED HI signal at frame {frame.index}")
				yield LEDSymbol.RLED_HI, frame.index

		# handle GLED
		if gled_on:
			# check for transition
			if gval < GLED_THRESHOLD_LO:
				gled_on = False
				# emit signal
				if DEBUG:
					print(f"GLED LO signal at frame {frame.index}")
				yield LEDSymbol.GLED_LO, frame.index
		else:
			# check for transition
			if gval > GLED_THRESHOLD_HI:
				gled_on = True
				# emit signal
				if DEBUG:
					print(f"GLED HI signal at frame {frame.index}")
				yield LEDSymbol.GLED_HI, frame.index

def decode_led_symbols(symbols: Iterator[tuple[LEDSymbol, int]]) -> list[list[MorseSymbol]]:
	"""Decodes the LED transition symbols into Morse code symbols.

	Returns a list representing a single Morse "word".

	Each item is a list of characters, and each character is a list of Morse symbols.
	"""

	# initialize output buffer
	buf: list[list[MorseSymbol]] = list()

	# record timestamp of last HI-to-LO transition (initialized with placeholder guaranteed to trigger a new character)
	last_ts: int = 0 - FRAMEDIV_CHARACTER - 1
	# record whether each LED went high since the last RLED LO
	r_went_hi = g_went_hi = False

	# iterate over LED symbols
	for sym, ts in symbols:
		match sym:
			case LEDSymbol.RLED_HI:
				assert not r_went_hi
				r_went_hi = True

				if ts - last_ts >= FRAMEDIV_CHARACTER:
					# start new character
					buf.append([])

			case LEDSymbol.RLED_LO:
				if not r_went_hi:
					print(f"ERROR: RLED LO before RLED HI!")

				morse_sym = MorseSymbol.DASH if g_went_hi else MorseSymbol.DOT

				# append symbol to character
				buf[-1].append(morse_sym)

				# reset LED memory
				r_went_hi = g_went_hi = False

				# update last_ts
				last_ts = ts

			case LEDSymbol.GLED_HI:
				assert not g_went_hi
				g_went_hi = True

			case LEDSymbol.GLED_LO:
				# update last_ts
				last_ts = ts

	return buf

def morse_word_to_ascii(word: list[list[MorseSymbol]]) -> str:
	sio = StringIO()

	for char in word:
		for sym in char:
			match sym:
				case MorseSymbol.DASH:
					sio.write("-")
				case MorseSymbol.DOT:
					sio.write(".")
		sio.write(" ")

	return sio.getvalue()[:-1]

def decode_morse_code(word: list[list[MorseSymbol]]) -> str:
	"""Decodes a list of Morse characters into a string."""

	def _decode_char(char: str) -> str:
		return {
			'.-':		'a',
			'-...':		'b',
			'-.-.':		'c',
			'-..':		'd',
			'.': 		'e',
			'..-.':		'f',
			'--.':		'g',
			'....':		'h',
			'..':		'i',
			'.---':		'j',
			'-.-':		'k',
			'.-..':		'l',
			'--':		'm',
			'-.':		'n',
			'---':		'o',
			'.--.':		'p',
			'--.-':		'q',
			'.-.':		'r',
			'...':		's',
			'-':		't',
			'..-':		'u',
			'...-':		'v',
			'.--':		'w',
			'-..-':		'x',
			'-.--':		'y',
			'--..':		'z',
			'-----':	'0',
			'.----':	'1',
			'..---':	'2',
			'...--':	'3',
			'....-':	'4',
			'.....':	'5',
			'-....':	'6',
			'--...':	'7',
			'---..':	'8',
			'----.':	'9',
		}[char]

	sio = StringIO()

	for char in word:
		dec_char = _decode_char(''.join('-' if s == MorseSymbol.DASH else '.' for s in char))
		sio.write(dec_char)

	return sio.getvalue()


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

	print("Extracting Morse code symbols from video...")
	morse_symbols = decode_led_symbols(extract_symbols(args.filepath))

	print(f"Extracted Morse code: {morse_word_to_ascii(morse_symbols)}")

	print("Decoding Morse code...")
	decoded_text = decode_morse_code(morse_symbols)
	print(f"Decoded text: {decoded_text}")
