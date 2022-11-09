#!/bin/bash

# automatic solve script for git-remembers-all

set -eu


solve() {
	local TARPATH="$1"

	# create temp dir for the repo
	WORKDIR="$(mktemp -d)"

	# extract bare repo to temp dir (ignoring the futuristic timestamps)
	echo "extracting repo"
	tar -xf "$TARPATH" -C "$WORKDIR" --warning=no-timestamp

	# find the unreachable blob
	echo "looking for unreachable objects"
	HIDDEN_BLOB="$(git -C "$WORKDIR" fsck --unreachable | grep -oE 'blob \w+')"
	echo "found hidden object: $HIDDEN_BLOB"

	# get the contents of the unreachable blob (.env)
	DOTENV_CONTENTS="$(git -C "$WORKDIR" cat-file $HIDDEN_BLOB)"
	echo "contents: $DOTENV_CONTENTS"

	# decode and print the flag
	echo -n "flag: "
	echo "$DOTENV_CONTENTS" | cut -f2 -d= | base64 -d

	# cleanup temp dir
	rm -rf "$WORKDIR"
}


if (($#!=1)); then
	echo "usage: $0 <path to git-repo.tar>"
	exit 1
fi

if [[ ! -f "$1" ]]; then
	echo "error: '$1' does not exist!"
	exit 1
fi

solve "$1"
