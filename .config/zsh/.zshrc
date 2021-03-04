# Enable colors and change prompt:
autoload -U colors && colors	# Load colors
setopt autocd		# Automatically cd into typed directory.
stty stop undef		# Disable ctrl-s to freeze terminal.
# PS1="%F{4}%n %F{2}%~ %f> " # Prompt, now is set by oh-my-zsh

# History in cache directory:
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.config/zsh/history

# Load oh-my-zsh configs
[ -f "${ZDOTDIR:-${XDG_CONFIG_HOME:-$HOME/.config}/zsh}/oh-my-zsh-rc" ] && source "${ZDOTDIR:-${XDG_CONFIG_HOME:-$HOME/.config}/zsh}/oh-my-zsh-rc"

# Load aliases and shortcuts if existent.
[ -f "${ZDOTDIR:-${XDG_CONFIG_HOME:-$HOME/.config}/zsh}/alias" ] && source "${ZDOTDIR:-${XDG_CONFIG_HOME:-$HOME/.config}/zsh}/alias"
[ -f "${ZDOTDIR:-${XDG_CONFIG_HOME:-$HOME/.config}/zsh}/shortcutrc" ] && source "${ZDOTDIR:-${XDG_CONFIG_HOME:-$HOME/.config}/zsh}/shortcutrc"

# Set Ctrl+Backspace
bindkey '^H' backward-kill-word


# Syntax highlighting dos comandos
# Para as opções disponiver ver https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/docs/highlighters/main.md
# Para definir a cor, escreva `fg=n` onde n é o número da cor segundo definido na configuração do termite
: ${ZSH_HIGHLIGHT_STYLES[unknown-token]:=fg=red}  # Comando que não existe
: ${ZSH_HIGHLIGHT_STYLES[reserved-word]:=fg=yellow,bold}  # for, if, etc
: ${ZSH_HIGHLIGHT_STYLES[precommand]:=fg=green,underline}
: ${ZSH_HIGHLIGHT_STYLES[commandseparator]:=fg=6}  # &&, ||, etc.
: ${ZSH_HIGHLIGHT_STYLES[path]:=fg=16,underline}  # Path alvo do comando quando existe
: ${ZSH_HIGHLIGHT_STYLES[command-substitution]:=fg=10}
: ${ZSH_HIGHLIGHT_STYLES[single-hyphen-option]:=fg=6}  # Command Arguments
: ${ZSH_HIGHLIGHT_STYLES[double-hyphen-option]:=fg=6}  # Command Arguments
: ${ZSH_HIGHLIGHT_STYLES[redirection]:=fg=1}  # >, >>, etc
: ${ZSH_HIGHLIGHT_STYLES[arg0]:=fg=10}    # Comando
: ${ZSH_HIGHLIGHT_STYLES[alias]:=fg=10,underline}  # Alias