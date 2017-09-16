#!/bin/bash

team_num=10
sport_prefix=2
cport_prefix=3

echo "Run Birthday"
sleep 2
chall_num="01"
name="birthday"
for team in $(seq -f "%02g" 1 $team_num); do 
	tagname=$name"__"$team
	cport="$cport_prefix""$team""$chall_num"
  	sport="$sport_prefix""$team""$chall_num"
	echo $tagname
	docker run --restart always -p "$cport:5000" -p "$sport:22" -itd $tagname
done

echo "Run Buaya LSI"
sleep 2
chall_num="02"
name="buaya"
for team in $(seq -f "%02g" 1 $team_num); do 
	tagname=$name"__"$team
	cport="$cport_prefix""$team""$chall_num"
  	sport="$sport_prefix""$team""$chall_num"
	echo $tagname
	docker run --restart always -p "$cport:5000" -p "$sport:22" -itd $tagname
done

echo "Run Cacah Jiwa"
sleep 2
chall_num="03"
name="cacah"
for team in $(seq -f "%02g" 1 $team_num); do 
	tagname=$name"__"$team
	cport="$cport_prefix""$team""$chall_num"
  	sport="$sport_prefix""$team""$chall_num"
	echo $tagname
	docker run --restart always -p "$cport:5000" -p "$sport:22" -itd $tagname
done

echo "Run Blog"
sleep 2
chall_num="04"
name="blog"
for team in $(seq -f "%02g" 1 $team_num); do 
	tagname=$name"__"$team
	cport="$cport_prefix""$team""$chall_num"
  	sport="$sport_prefix""$team""$chall_num"
	echo $tagname
	docker run --restart always -p "$cport:80" -p "$sport:22" -itd $tagname
done

echo "Run Kudanil"
sleep 2
chall_num="05"
name="kudanil_lsi"
for team in $(seq -f "%02g" 1 $team_num); do 
	tagname=$name"__"$team
	cport="$cport_prefix""$team""$chall_num"
  	sport="$sport_prefix""$team""$chall_num"
	echo $tagname
	docker run --restart always -p "$cport:5000" -p "$sport:22" -itd $tagname
done

echo "Run Math Service"
sleep 2
chall_num="06"
name="math"
for team in $(seq -f "%02g" 1 $team_num); do 
	tagname=$name"__"$team
	cport="$cport_prefix""$team""$chall_num"
  	sport="$sport_prefix""$team""$chall_num"
	echo $tagname
	docker run --restart always -p "$cport:5000" -p "$sport:22" -itd $tagname
done

echo "Run Musicality Icon"
sleep 2
chall_num="07"
name="musicality_icon"
for team in $(seq -f "%02g" 1 $team_num); do 
	tagname=$name"__"$team
	cport="$cport_prefix""$team""$chall_num"
  	sport="$sport_prefix""$team""$chall_num"
	echo $tagname
	docker run --restart always -p "$cport:80" -p "$sport:22" -itd $tagname
done

echo "Run Sanca"
sleep 2
chall_num="08"
name="sanca"
for team in $(seq -f "%02g" 1 $team_num); do 
	tagname=$name"__"$team
	cport="$cport_prefix""$team""$chall_num"
  	sport="$sport_prefix""$team""$chall_num"
	echo $tagname
	docker run --restart always -p "$cport:5000" -p "$sport:22" -itd $tagname
done

