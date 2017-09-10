#!/usr/bin/env python
import sys,re

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

def XxxXxxx_xXxxxxx(s):
  return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
             lambda mo: mo.group(0)[0].upper() +
                        mo.group(0)[1:].lower(),
             s)

print """Sanca 2.0  
Type Anything You Want
                           ____
  ________________________/ O  \___/
 <_/_\_/_\_/_\_/_\_/_\_/_______/   \

"""
while 1:
  try:
    print eval(XxxXxxx_xXxxxxx(raw_input(">>> ")))
  except KeyboardInterrupt:
    print " CTRL+Z to Exit"
  except Exception as e: 
    print(e)
