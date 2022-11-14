#!/usr/bin/env python3

from PIL import Image


def decode(img: Image.Image) -> bytes:
	buf = bytearray()
	for pixel in img.getdata():
		buf.append(pixel[0] | pixel[1] | pixel[2])
	return bytes(buf)


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("filepath", help="Path to the image containing encoded data.")
	args = parser.parse_args()


	with Image.open(args.filepath) as img:
		flag = decode(img)

	print(f"Recovered flag: {flag!r}")
