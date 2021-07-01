#!/bin/sh

outfile="my-current-settings.ini"
[ $# -gt 0 ] && outfile=$1

dconf dump / > $outfile
