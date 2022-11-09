#!/bin/bash

# constructs and archives the git repo

set -e

FLAG="$(rg -o --replace '$1' '^flag ?= ?"([\w{}]+)"' ../challenge.toml)"  # get flag from challenge.toml
AUTHOR_NAME="webdev2103"
AUTHOR_EMAIL="${AUTHOR_NAME}@megacorp.internal"
GIT_BRANCH_NAME="main"

SCRIPT_DIR="$(dirname "$(realpath "$0")")"
SRCDIR="$SCRIPT_DIR"/assets
OUTFILE="$SCRIPT_DIR"/../static/git-repo.tar
WORKDIR="$SCRIPT_DIR"/build


# disable loading git config
export GIT_CONFIG_GLOBAL=/dev/null
export GIT_CONFIG_SYSTEM=/dev/null
# configure author/committer details
export GIT_AUTHOR_NAME="$AUTHOR_NAME"
export GIT_COMMITTER_NAME="$AUTHOR_NAME"
export GIT_AUTHOR_EMAIL="$AUTHOR_EMAIL"
export GIT_COMMITTER_EMAIL="$AUTHOR_EMAIL"


if [[ -e "$WORKDIR" ]]; then
	rm -rf "$WORKDIR"
fi
mkdir -p "$WORKDIR"/repo-{local,remote}


cd "$WORKDIR"/repo-local

## initialize local repository
git init -b $GIT_BRANCH_NAME

## create initial commit with readme
cp "$SRCDIR"/README.md ./

git add README.md
GIT_AUTHOR_DATE="2023-03-14 01:29:22" GIT_COMMITTER_DATE="$GIT_AUTHOR_DATE" \
	git commit README.md -m "Initial commit"

## actually add some project files
poetry init --no-interaction \
	--author="$AUTHOR_NAME <${AUTHOR_EMAIL}>" \
	--description="Lorem Ipsum web app" \
	--dependency=starlette \
	--dependency=uvicorn

echo "poetry.lock" > .gitignore
echo ".venv" >> .gitignore

cp "$SRCDIR"/app-v1.py ./app.py

git add app.py pyproject.toml .gitignore
GIT_AUTHOR_DATE="2023-03-14 01:35:17" GIT_COMMITTER_DATE="$GIT_AUTHOR_DATE" \
	git commit app.py pyproject.toml .gitignore -m "Add initial project files"

## add session middleware with leaked secret
poetry add --lock itsdangerous

cp "$SRCDIR"/app-v2.py ./app.py

# write b64-encoded secret to .env
echo -n "SECRET_KEY=" > .env
echo "$FLAG" | base64 >> .env

git add .env
GIT_AUTHOR_DATE="2023-03-14 01:47:50" GIT_COMMITTER_DATE="$GIT_AUTHOR_DATE" \
	git commit app.py pyproject.toml .env -m "Add session middleware for security"


## initialize remote repository
git -C "$WORKDIR"/repo-remote init -b main --bare


## push local changes to remote repo
git remote add github ../repo-remote
git push --set-upstream github $GIT_BRANCH_NAME

## the "oh shit", "fix up before anyone notices" moments
echo ".env" >> .gitignore

git add .gitignore
git rm .env
GIT_COMMITTER_DATE="2023-03-14 01:55:51" git commit --amend -C HEAD
git push --force


## archive the resulting remote repo
cd "$WORKDIR"/repo-remote
tar cf "$OUTFILE" * --mtime="2023-03-14 04:31:23" --owner=0 --group=0
