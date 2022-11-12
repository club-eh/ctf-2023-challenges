#!/bin/sh

set -eu

# prepend colon to port number
export PORT=":${PORT}"
# generate a random secret
export SECRET="$(head -c32 /dev/urandom | base64 -w0)"

# execute the server
exec ./main
