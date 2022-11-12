#!/bin/sh

# script to download 3rd-party web assets

set -eu

if [[ -n "${1:-}" ]]; then
    mkdir -p "$1"
    cd "$1"
fi


BOOTSTRAP_VER=5.2.2


dl() {
    wget "$1" -O "$2"
}

dl "https://cdn.jsdelivr.net/npm/bootstrap@${BOOTSTRAP_VER}/dist/css/bootstrap.min.css" 'bootstrap.min.css'
dl "https://cdn.jsdelivr.net/npm/bootstrap@${BOOTSTRAP_VER}/dist/js/bootstrap.min.js" 'bootstrap.min.js'
