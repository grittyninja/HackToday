#!/bin/bash
if [ -z "$1" ];then
  echo "need team numbers as argument"; exit
fi
team=$1
echo -n "" > username.list
echo -n "" > password.list
echo -n "" > token.list
for i in `seq 1 $team`; do
  username="$(tr -cd '[:lower:]' < /dev/urandom | fold -w10 | head -n1 |  awk '{ print $1 }')"
  echo $username >> username.list
  password="$(tr -cd '[:lower:]' < /dev/urandom | fold -w15 | head -n1 |  awk '{ print $1 }')"
  echo $password >> password.list
  token="$(tr -cd '[:lower:]' < /dev/urandom | fold -w5 | head -n1 |  awk '{ print $1 }')"
  echo $token >> token.list
done