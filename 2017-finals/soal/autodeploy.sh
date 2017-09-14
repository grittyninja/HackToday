#!/bin/bash
if [ -z "$1" ];then
  echo "need team numbers as argument"; echo "$0 (team numbers)"; exit
fi


team_num=$1

echo "Birthday Card"
sleep 2
(cd ./birthday_card && ./docker_build.sh birthday $team_num)

echo "Buaya LSI"
sleep 2
(cd ./buaya_lsi && ./docker_build.sh buaya $team_num)

echo "Cacah Jiwa"
sleep 2
#(cd ./cacah_jiwa && ./docker_build.sh cacah_jiwa $team_num)

echo "How to Blog"
sleep 2
(cd ./howto_blog && ./docker_build.sh howto_blog $team_num)

echo "Kudanil LSI"
sleep 2
#(cd ./kudanil_lsi && ./docker_build.sh kudanil_lsi $team_num)

echo "Math Service"
sleep 2
(cd ./math_service && ./docker_build.sh math $team_num)

echo "Musicality Icon"
sleep 2
(cd ./musicality_icon && ./docker_build.sh musicality_icon $team_num)

echo "Sanca"
sleep 2
(cd ./sanca && ./docker_build.sh sanca $team_num)
