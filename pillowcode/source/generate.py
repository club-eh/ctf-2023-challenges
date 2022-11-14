#!/usr/bin/env python3

from PIL import Image


def encode(data: bytes) -> Image.Image:
	img = Image.new("RGB", (len(data), 1))
	buf = bytearray(len(data) * 3)
	for i in range(len(data)):
		buf[i*3+1] = data[i] & 0x70
		buf[i*3] = data[i] & 0x8a
		buf[i*3+2] = data[i] & 0x05
	img.frombytes(bytes(buf))
	return img


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("flag")
	parser.add_argument("filename")
	args = parser.parse_args()

	encode(args.flag.encode()).save(args.filename)
