#!/usr/bin/python
import sys , os , random, string

wSAL = len(sys.argv)

w_length = 25
w_extra =  '!@#$%^*()'
if ( wSAL > 1 ):
        w_length = int(sys.argv[1])
if ( wSAL > 2 ):
        if ( sys.argv[2] == "url" ):
                w_extra = "$-_.+!*'(),"

w_byte_seed = random.randrange( 1024 ,  2048 , 8 )
print w_byte_seed

chars = string.ascii_letters + string.digits + w_extra
random.seed = (os.urandom( w_byte_seed  ))
