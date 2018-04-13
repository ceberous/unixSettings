import os , sys
from imgurpython import ImgurClient

if len( sys.argv ) < 2:
	UploadFolderBasePath = "/home/morpheous/Pictures/1/"
else:
	UploadFolderBasePath = sys.argv[1]

def get_ordered_image_paths( wBaseDir ):
	os.chdir( wBaseDir )
	return sorted( filter( os.path.isfile, os.listdir( "." ) ) , key=os.path.getmtime )


def imgur_authenticate_pin():
	
	# https://api.imgur.com/oauth2/addclient
	client_id = ""
	client_secret = ""

	client = ImgurClient( client_id , client_secret )

	authorization_url = client.get_auth_url( "pin" )

	print( "Go to the following URL: {0}".format( authorization_url ) )
	try:
		pin = raw_input( "Enter Pin\n" )
	except:
		pin = input( "Enter Pin\n" )

	credentials = client.authorize( pin , "pin" )
	client.set_user_auth( credentials[ "access_token" ] , credentials[ "refresh_token" ] )
	print "\n\n"

	return client


# 1.) Get Ordered Path List
OrderedImagePaths =  get_ordered_image_paths( UploadFolderBasePath )

# 2.) Log-In
client = imgur_authenticate_pin()

# 3.) Upload
MD_Formated_UploadedPaths = []
totalS = str( len( OrderedImagePaths ) )
for index , image_path in enumerate( OrderedImagePaths ):
	wRealPath = os.path.join( UploadFolderBasePath , image_path )
	uploaded_img = client.upload_from_path( image_path , config=None , anon=False )
	print "Uploaded --> " + wRealPath + " --> [ " + str( ( index + 1 ) ) + " ] of " + totalS
	MD_Formated_UploadedPaths.append( "![](" + uploaded_img[ "link" ] + ")" )

# 4.) Print 
print "\n\n"
for x in MD_Formated_UploadedPaths:
	print x
