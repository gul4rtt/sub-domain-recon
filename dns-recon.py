#!/usr/bin/env python

import socket 
import sys

print("dominio/alvo: ", sys.argv[1])
print("wordlist: ", sys.argv[2])

file = open(sys.argv[2], 'r')
count = 0

while True:
    count +=1
    line = file.readline()

    if not line:
        break
    line = line.strip('\n')
    DNS = line + "." + sys.argv[1]
    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass
file.close()

