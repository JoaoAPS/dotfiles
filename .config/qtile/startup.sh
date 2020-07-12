#!/bin/sh

exec picom &
exec redshift -l -25.5:-50 -t 5500:3000 &
exec numlockx off &
exec dunst &
exec unclutter -idle 5 &

#Desabilita screensaver
exec xset s off&
exec xset s noblank&
exec xset -dpms&
