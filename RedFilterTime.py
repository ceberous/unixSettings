#!/usr/bin/python

import sys , os , time , subprocess

#https://github.com/shawnrice/alfred.flux

wTimeZones = [ 'America/Los_Angeles' , 'America/Denver' , 'America/Detroit' , 'Europe/London' ]
wBrazil = [ "-5.8" , "-35.2"  ]
wAustralia = [ "-33.8" , "151.2" ]
wSKorea = [ "37.5" , "127.0" ]
XFLUX_CMD_BASE = "xflux -k 2000"
XFLUX_CMD_NORMAL = XFLUX_CMD_BASE + " -z 98555"
XFLUX_CMD_FINAL = XFLUX_CMD_BASE

os.environ['TZ'] = wTimeZones[0]
time.tzset()
print time.strftime('%X %x %Z')

wExtra = ""
if ( len( sys.argv ) > 1 ): wExtra = sys.argv[1]

cHour = int( time.strftime( '%H' ) )
if ( wExtra  == "revert" ):
	XFLUX_CMD_FINAL = XFLUX_CMD_FINAL
elif ( cHour <= 18  ):
	if (cHour  >= 4 ):
		XFLUX_CMD_FINAL = XFLUX_CMD_FINAL + " -l " + wBrazil[0] + " -g " + wBrazil[1]
	else:
		XFLUX_CMD_FINAL = XFLUX_CMD_FINAL + " -l " + wSKorea[0] + " -g " + wSKorea[1]

print XFLUX_CMD_FINAL
subprocess.call( "sudo pkill xflux" , shell=True )
subprocess.call( XFLUX_CMD_FINAL , shell=True )
