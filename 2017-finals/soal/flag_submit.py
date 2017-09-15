#!/usr/bin/env python
from pwn import *
import sys

a = remote("192.168.8.236",1337)
username = "admin"
password = "polisi"
a.recvuntil(": ")
a.sendline(username)
a.recvuntil(": ")
a.sendline(password)
if(len(sys.argv)>1):
	file = open(sys.argv[1], "r")
	fileread = file.read()
	hasil =fileread.split("\n")
	for i in hasil:
		flag = (i.split(","))[:1][0]
		team = (i.split(","))[1:][0]
		problem_num = (i.split(","))[-1][0]
		print a.recvuntil(">>> ")
		a.sendline("/add flags")
		print a.recvuntil(": "),flag
		a.sendline(flag)
		print a.recvuntil(": "),team
		a.sendline(team)
		print a.recvuntil(": "),problem_num
		a.sendline(problem_num)
	print "DONE !!!"
else:
	print "NEED DIRECTORY ARGUMENT\n\nex:./flag_submit.py docker_math.csv\n\n"