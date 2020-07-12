function fish_prompt
	#Se há um virtual environment ativo, imprime ele
	if set -q VIRTUAL_ENV
    	echo -n -s (set_color yellow) "(" (basename "$VIRTUAL_ENV") ")" (set_color normal) " "
	end
	
    test $SSH_TTY
    and printf (set_color red)$USER(set_color brwhite)'@'(set_color yellow)(prompt_hostname)' '
    test "$USER" = 'root'
    and echo (set_color red)"#"

    # Main
    echo -n (set_color blue)'nanni' (set_color green)(prompt_pwd) (set_color white)'>'(set_color white)' '
end
