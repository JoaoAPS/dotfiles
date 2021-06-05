#!/bin/sh

if [ $# -eq 0 ]; then
    echo "Uso: ./import.sh <arquivo .ini>"
    exit
fi

dconf load / < $1
