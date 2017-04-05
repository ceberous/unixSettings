import subprocess , sys

if len(sys.argv) < 4:
	print( "usage args = hash-function , path-of-file-to-check , correct-answer" )
	sys.exit()

wSUB = subprocess.Popen( [ sys.argv[1] , sys.argv[2] ] , stdout=subprocess.PIPE )
for line in iter( wSUB.stdout.readline , '' ):
	a1 = line.rstrip().split(" ")
	if a1[0] == sys.argv[3]:
		print "Identical " + sys.argv[1] + " Hash Sums"
		print a1[0] 
		print "\t\t="
		print sys.argv[3]
	else:
		print "Hash Check Failed"
