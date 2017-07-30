import os , time , subprocess

wTimeZones = [ 'America/Los_Angeles' , 'America/Denver' , 'America/Detroit' , 'Europe/London' ]
wAustralia = [ "-33.8" , "151.2" ]
wSKorea = [ "37.5" , "127.0" ]
XFLUX_CMD_BASE = "xflux -k 2000"
XFLUX_CMD_NORMAL = XFLUX_CMD_BASE + " -z 98555"
XFLUX_CMD_FINAL = XFLUX_CMD_BASE

os.environ['TZ'] = wTimeZones[0]
time.tzset()
print time.strftime('%X %x %Z')

cHour = int( time.strftime( '%H' ) )
if ( cHour <= 18  ):
	if ( cHour >= 4 ):
		XFLUX_CMD_FINAL = XFLUX_CMD_FINAL + " -l " + wSKorea[0] + " -g " + wSKorea[1]

print XFLUX_CMD_FINAL
subprocess.call( "pkill -9 xflux" , shell=True )
subprocess.call( XFLUX_CMD_FINAL , shell=True )
