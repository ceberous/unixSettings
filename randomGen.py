#!/usr/bin/python
import sys , os , random, string

try:
	w_length = int(sys.argv[1])
except:
	w_length = 25

chars = string.ascii_letters + string.digits + '!@#$%^*()'
random.seed = (os.urandom(1024))

print ''.join(random.choice(chars) for i in range(w_length))
