#!/usr/bin/env python3

from datetime import timedelta


def analyze_sleeps(data: str):
	# calculate total nanoseconds
	total_ns = sum(int(value) for value in data.split())

	# convert to Python timedelta
	td = timedelta(microseconds = total_ns // 1000)

	print(f"Sleep total: {td}")


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("sleeplog", help="Path to file containing list of sleep intervals.")
	args = parser.parse_args()

	with open(args.sleeplog) as fp:
		analyze_sleeps(fp.read())
