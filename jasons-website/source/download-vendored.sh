#!/bin/sh

# script to download 3rd-party web assets

set -eu

if [[ -n "${1:-}" ]]; then
    mkdir -p "$1"
    cd "$1"
fi


JQUERY_VER=3.6.1
BOOTSTRAP_VER=5.2.2


dl() {
    wget "$1" -O "$2"
}

dl "https://code.jquery.com/jquery-${JQUERY_VER}.min.js" 'jquery.min.js'
dl "https://cdn.jsdelivr.net/npm/bootstrap@${BOOTSTRAP_VER}/dist/css/bootstrap.min.css" 'bootstrap.min.css'