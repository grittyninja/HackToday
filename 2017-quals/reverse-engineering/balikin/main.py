from Crypto.Cipher import XOR
import base64
import codecs
source = "flag"
target = "hasil"
key = "RENDANGBASOGULING"

BLOCKSIZE = 1048576

def cobacoba(data):
    hasil = ""
    kr=0
    for i in data[::-1]:
        hasil+= chr(ord(i)+ord(key[kr%len(key)]))
        
        kr+=1
    
    cipher = XOR.new(key)
    return base64.b64encode(cipher.encrypt(hasil))
        

with codecs.open(source, "r", "utf-8") as sourceFile:
    with codecs.open(target, "w", "ascii") as targetFile:
        while True:
            contents = sourceFile.read(BLOCKSIZE)
            contents = cobacoba(contents)
            if not contents:
                break
            
            targetFile.write(contents)
            
            

            
            
