#!/bin/bash

# Copied from https://github.com/k-vernooy/dotfiles - All thanks go to him!

function get_music() {
    IFS=$'\n'
    for i in $(ls ~/Music | grep -v 'Podcasts\|Other\|thumbnails'); do
        name="${i%.*}"
        # name="t"
        echo -en "${i}\0icon\x1f${HOME}/Music/thumbnails/${name}.png\n"
    done
}

if [ -z "$@" ]; then
    echo -en "Shuffle\0icon\x1fmedia-playlist-shuffle\n"
    get_music
else
    if [ "$1" = "Shuffle" ]; then
        $HOME/.config/rofi/scripts/mpv-controller.sh start shuffle &
    else
        $HOME/.config/rofi/scripts/mpv-controller.sh start "${HOME}/Music/$1" &
    fi
fi
