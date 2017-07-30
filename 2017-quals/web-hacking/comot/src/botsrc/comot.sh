#!/bin/bash

while true; do
	URL=$(curl -s [DOMAIN]:[PORT]/report/rotate.php)
	if [ -n "$URL" ]; then 
		echo "browse /notes/$URL"; 
		python comot.py $URL;
	fi
	sleep 5
done
