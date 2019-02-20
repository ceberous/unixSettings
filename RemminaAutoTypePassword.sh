#!/bin/bash
remmina -c /home/morpheous/.remmina/profile.remmina
sleep .3
xdotool type "password"
sleep .3
xdotool key Return
