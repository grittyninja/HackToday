#!/usr/bin/python

import circle
import sys

for j in range(1, 100):
        cipher = 'Hy80o81d9}95{8047Ta887k43c2a'
        print j
        for i in range(100):
                cipher = circle.encrypt(cipher, j)
                if 'HackToday' in cipher:
                        print i, cipher
                        sys.exit(0)
