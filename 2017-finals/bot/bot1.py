#!/usr/bin/python
# {1:[1,1,1,1,1]}

from pwn import *
import requests
import time

real = time.time()
b = time.time()

def submit(q):
	print "[+] Submit query"
	a = remote('192.168.8.236', 1337)
	a.recvuntil('Username:')
	a.sendline('bot')
	a.recvuntil('Token:')
	a.sendline('awkarin')
	a.sendline(q)
	a.recvuntil('Done')
	a.close()
	print "[+] Done"

def cek():
	print "[+] Checking up service ....."
	q = '{1:['
	for i in range(1, 11):
		port = '3' + str(i).zfill(2) + '01'
		ip = 'http://192.168.8.236'
		url = ip + ':' + port
		print url
		try:
			a = requests.get(url, timeout = 2) # treshold 2 detik waktu tunggu
			hasil = a.text
			if 'Celebrate It' not in hasil:
				raise e
			q += str(1)
		except:
			q += str(0)

		if i < 10:
				q += ','
	q += ']}'
	print "[+] Query : ", q
	return q

if __name__ == '__main__':
	while 1:
		submit(cek())

		total = time.time() - b
		time.sleep(30-total)

		print time.time() - real