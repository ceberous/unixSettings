#!/usr/bin/python
import subprocess , sys , os 
wPath = None
wSize = None

def run_command( wCommandArray ):
    wP = subprocess.Popen( wCommandArray , stdout=subprocess.PIPE , stderr=subprocess.PIPE )
    stdout, stderr = wP.communicate()
    wError = [ s.strip() for s in stderr.splitlines() ]
    if ( len( wError ) == 0 ):
        wResult = [ s.strip() for s in stdout.splitlines() ]
        return wResult
    else:
        print "error running command"
        print wError
        return wError

def get_size():
    global wSize
    wCA = [ "ffprobe" , "-v" , "error" , "-show_entries" , "stream=width,height" , "-of" , "default=noprint_wrappers=1" , sys.argv[1]  ]        
    wResults = run_command( wCA )
    wResults[0] = wResults[0].split("width=")[1]
    wResults[1] = wResults[1].split("height=")[1]
    wSize = wResults

def create_tmp_frame_dir():
    global wPath
    run_command( [ "mkdir" , wPath ] )

def remove_tmp_frame_dir():
    global wPath
    wPath = wPath + "/"
    run_command( [ "rm" , "-rf" , wPath ] )

def make_frames():
    print "\nGenerating Frames"
    global wPath , wSize
    wSmallest = wSize[0] if wSize[0] > wSize[1] else wSize[1]
    wScale = "scale=" + wSmallest + ":-1:flags=lanczos,fps=" + sys.argv[2]
    tmpPA = wPath + "/ffout%03d.png"
    wCA = [ "ffmpeg" , "-i" , sys.argv[1] , "-vf" , wScale , tmpPA ]
    run_command( wCA )

def convert_frames():
    print "\nConverting Frames to GIF"
    global wPath
    tmpPA = wPath + "/ffout*.png"
    wCA = [ "convert" , "-loop" , "0" , tmpPA , "output.gif" ]
    run_command( wCA )

def wMain():

    global wPath
    wEnd = sys.argv[1].rfind("/")
    wPath = sys.argv[1][0:wEnd+1] + "wFramesTMP"
    print wPath

    create_tmp_frame_dir()
    get_size()
    make_frames()
    convert_frames()
    remove_tmp_frame_dir()

wMain()