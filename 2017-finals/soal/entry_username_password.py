#!/usr/bin/python

from pwn import *

a = remote('192.168.8.236', 1337)
print a.recvuntil('Username:')
a.sendline('admin')
print a.recvuntil('Token')
a.sendline('polisi')

usernames = open('username.list').read().split('\n')
names = open('name.list').read().split('\n')
tokens = open('token.list').read().split('\n')

for i in range(1, 11):
	print a.recvuntil('>>>')
	a.sendline('/add teams')
	print a.recvuntil('Username:')
	a.sendline(usernames[i-1])
	print a.recvuntil('Team number:')
	a.sendline(str(i))
	print a.recvuntil('Token:')
	a.sendline(tokens[i-1])
	print a.recvuntil('Team name:')
	a.sendline(names[i-1])