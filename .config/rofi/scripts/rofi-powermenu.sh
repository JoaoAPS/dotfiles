#!/bin/bash

# Copied from https://github.com/k-vernooy/dotfiles - All thanks go to him!

if [ -z "$@" ]; then
    echo -en "Shutdown\0icon\x1fsystem-shutdown\n"
    echo -en "Logout\0icon\x1fsystem-log-out\n"
    echo -en "Suspend\0icon\x1fsystem-suspend\n"
    echo -en "Reboot\0icon\x1fsystem-restart\n"
    echo -en "Cancel\0icon\x1fcancel\n"
else
    if [ "$1" = "Shutdown" ]; then
        sudo shutdown -h now
    elif [ "$1" = "Logout" ]; then
        i3-msg exit || gnome-session-quit --logout --no-prompt
    elif [ "$1" = "Reboot" ]; then
        # sudo reboot
        sudo shutdown -r now
    elif [ "$1" = "Suspend" ]; then
        system-ctl suspend
    fi
fi
