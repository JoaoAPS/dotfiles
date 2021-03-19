# -- Prompt --:
# %F{n} aciona a cor n (segundo definido na configuração do termite)
# %f reseta cor
# %n = user name
# %M = host
# %~ = path

PROMPT="%F{4}%n %F{3}%3~ %F{8}> %f"
RPROMPT='%{$fg_bold[green]%}$(git_prompt_info)%{$reset_color%}% '

ZSH_THEME_GIT_PROMPT_PREFIX="%F{15}<%F{2}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%f"
ZSH_THEME_GIT_PROMPT_DIRTY="%F{11} ✗%F{15}>%f"
ZSH_THEME_GIT_PROMPT_CLEAN="%F{15}>"
