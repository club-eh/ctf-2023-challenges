#!/bin/sh

set -eu

# set listening port
export PORT=":1337"
# generate a random secret
export SECRET="$(head -c32 /dev/urandom | base64 -w0)"

# execute the server
exec ./main
