#!/bin/sh
clear
afplay br.mp3 > /dev/null 2>&1 &
play br.mp3 > /dev/null 2>&1 &

chmod +x raptor

echo "Installing Raptor...

"

insd=$(pwd)

echo $PATH | grep -q $insd
result=$?

echo "8888888b.                 888                   
888   Y88b                888                   
888    888                888                   
888   d88P 8888b. 88888b. 888888 .d88b. 888d888 
8888888P\"     \"88b888 \"88b888   d88\"\"88b888P\"   
888 T88b  .d888888888  888888   888  888888     
888  T88b 888  888888 d88PY88b. Y88..88P888     
888   T88b\"Y88888888888P\"  \"Y888 \"Y88P\" 888     
                  888                           
                  888                           
                  888                           
                          - a tool from 3ch0 8ase"

if [ "$result" -ne 0 ]; then
	export PATH="`pwd`:$PATH"
	echo $PATH
fi
echo "...done!"
echo -en "Press q to exit: "
read -r -s -n1 input
if [[ $input = "q" ]] || [[ $input = "Q" ]]; then
	killall afplay > /dev/null 2>&1 &
	killall play > /dev/null 2>&1 &
fi
