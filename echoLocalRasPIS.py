import os
import socket

halo3PIStatus  = True if os.system("sudo ping -c 1 " + "halopi3.local") is 0 else False

print "Local IP = " + ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

print "halopi3 is Alive? = " + str(halo3PIStatus)
