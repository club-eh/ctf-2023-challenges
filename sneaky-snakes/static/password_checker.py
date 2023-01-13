#!/usr/bin/env python3

import string

ALPHABET = string.ascii_lowercase + string.digits

def rot18(data: str) -> str:
	s = ''
	for n in data:
		try:
			s += ALPHABET[(ALPHABET.index(n) + 18) % len(ALPHABET)]
		except ValueError:
			s += n
	return s

def check_password(flag: str) -> bool:
	w = ['aluc9l', '7mnnei9vn', 'njwmqwiw']

	for l in flag:
		if l not in ALPHABET + '{_}':
			return False

	if not flag.startswith("clubeh"):
		return False

	if flag.count("{") != 1:
		return False
	elif flag.count("}") != 1:
		return False

	p = flag[7:-1].split(chr(95))

	if len(p) != 7:
		return False

	if not (p[0].endswith("0s") and p[0].startswith("t3l") and len(p[0]) == 5):
		return False
	if not (p[1].endswith("k35") and p[1].startswith("m4") and len(p[1]) == 5):
		return False
	if p[3] != "m05t":
		return False
	if p[2] != "th3":
		return False
	for i in range(4, 7):
		if rot18(p[i]) != w[i-4]:
			return False

	return True

if __name__ == "__main__":
	while True:
		if check_password(input("Flag: ")):
			print("Yup, that's the flag!")
			break
		else:
			print("Sorry, that's not the flag!")
