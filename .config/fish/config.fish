# FISH shell startup commands

# Set up path
set tmp (du "$HOME/.local/bin/" | cut -f2 | paste -sd ':'); set PATH "$PATH:$tmp"

# Default programs
export EDITOR="subl3"
export TERMINAL="st"
export BROWSER="firefox"
export READER="zathura"


# Aliases and abbriviations
if test -e ~/.config/fish/fish_aliases
    . ~/.config/fish/fish_aliases
end

#Greeting Message
set fish_greeting "   Welcome to my fish-powered suckless terminal! No mouses allowed "

#Enables special keys
tput smkx

#Binds special keys
bind \e\[P 		delete-char			#Delete
bind \e\[3\;5~ 	kill-word 			#Ctrl-Del
bind \e\[M 		kill-word 			#Ctrl-Del
bind \b 		backward-kill-word	#Ctrl-Backspace
#Dica: execute no terminal fish_key_reader para encontrar o símbolo de cada key.


#Moves dot files to .config
set XDG_CONFIG_HOME "$HOME"/.config

set ZDOTDIR "$HOME/.config/zsh"
set GNUPGHOME "$XDG_DATA_HOME"/gnupg
set GTK2_RC_FILES "$XDG_CONFIG_HOME"/gtk-2.0/gtkrc
set KDEHOME "$XDG_CONFIG_HOME"/kde
set IPYTHONDIR "$XDG_CONFIG_HOME"/jupyter
set JUPYTER_CONFIG_DIR "$XDG_CONFIG_HOME"/jupyter
set LESSHISTFILE -
set NPM_CONFIG_USERCONFIG $XDG_CONFIG_HOME/npm/npmrc
set XINITRC "$XDG_CONFIG_HOME"/X11/xinitrc


# Start graphical environment in tty1
if pacman -Qs libxft-bgra >/dev/null 2>&1
	test (tty) = "/dev/tty1" && ! pidof Xorg >/dev/null 2>&1 && exec startx
end