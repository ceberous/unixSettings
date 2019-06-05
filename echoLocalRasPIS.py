#!/usr/bin/python
import os
import socket
import fcntl
import struct
from subprocess import Popen, PIPE

wIP = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(socket.connect(('8.8.8.8')))]] )])
x1 = wIP.rfind( "." )
wNet_Mask = wIP[ 0 : x1  ] + ".0/24"
print wNet_Mask

wArgs = "sudo nmap -sP " + wNet_Mask + " | awk '/^Nmap/{ip=$NF}/B8:27:EB/{print ip}'"
print wArgs
p = Popen( wArgs , shell=True , stdout=PIPE , bufsize=1 )
with p.stdout:
    for line in iter( p.stdout.readline , b'' ):
        print line,
p.wait()
