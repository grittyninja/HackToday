#!/bin/bash
if [ -z "$1" ];then
  echo "need chall name as argument"; echo "$0 (chall name) (team numbers)"; exit
fi
if [ -z "$2" ];then
  echo "need team numbers as argument"; echo "$0 (chall name) (team numbers)"; exit
fi
team_num=$2
binary=$1
cport_prefix="3"
sport_prefix="2"
chall_num="02"
docker_log="docker_$binary.log"
docker_csv="docker_$binary.csv"
username_list="username.list"
token_list="token.list"
usernames=( $( cat ./$username_list ) )
tokens=( $( cat ./$token_list ) )
echo -n "" > $docker_log
echo -n "" > $docker_csv
for team in $(seq -f "%02g" 1 $team_num); do
  tag_name="$binary"__"$team"
  cport="$cport_prefix""$team""$chall_num"
  sport="$sport_prefix""$team""$chall_num"
  flag_name="flag_$(tr -cd '[:alnum:]' < /dev/urandom | fold -w30 | head -n1 | md5sum | awk '{ print $1 }')"
  flag="HackToday{$(tr -cd '[:alnum:]' < /dev/urandom | fold -w30 | head -n1 | sha256sum | awk '{ print $1 }')}"
  username="${usernames[$((${team##+(0)}-1))]}"
  password=`echo -n "${tokens[$((${team##+(0)}-1))]}$flag" | md5sum | awk '{print $1}'`
  echo "Team: $team" >> $docker_log
  echo "Username: $username" >> $docker_log
  echo "Password: $password" >> $docker_log
  echo "Flag filename: $flag_name" >> $docker_log
  echo "Flag: $flag" >> $docker_log
  echo "CPort: $cport" >> $docker_log
  echo "SPort: $sport" >> $docker_log
  echo "$flag,$(expr $team + 0),$(expr $chall_num + 0)" >> $docker_csv
  docker build --build-arg "password=$password" --build-arg="binary=$binary" --build-arg "username=$username" --build-arg "flag=$flag" --build-arg "flag_name=$flag_name" -t $tag_name .
  docker run -p "$cport:5000" -p "$sport:22" -itd $tag_name 
done
