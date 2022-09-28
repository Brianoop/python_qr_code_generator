# Importing library
import qrcode
 
# Data to be encoded
strings = ["first", "second", "third", "fourth", "fifth"]
 

for x in strings:
	# Encoding data using make() function
	img = qrcode.make(x)
	# Saving as an image file
	img.save('images/'+ x + '_QRCode' + '.png') 

