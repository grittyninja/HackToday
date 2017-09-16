#!/usr/bin/python
# {1:[1,1,1,1,1]}

from pwn import *
import time


def submit(q):
	print "[+] Submit query"
	a = remote('192.168.8.236', 1337)
	a.recvuntil('Username:')
	a.sendline('bot')
	a.recvuntil('Password:')
	a.sendline('awkarin')
	a.sendline(q)
	a.recvuntil('Done')
	a.close()
	print "[+] Done"

def cek():
	print "[+] Checking up service ....."
	q = '{3:['
	for i in range(1, 11):
		port = '3' + str(i).zfill(2) + '03'
		ip = '192.168.8.236'
		try:
			a = remote(ip, port)
			hasil = a.recvuntil('Nama suami :', timeout = 2)
			if not hasil:
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
		real = time.time()
		b = time.time()

		submit(cek())

		total = time.time() - b
		time.sleep(30-total)

		print time.time() - real