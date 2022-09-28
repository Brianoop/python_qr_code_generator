# Importing library
import qrcode
 
# Data to be encoded
strings = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eigth", "nineth", "tenth"]
 
 
 
for x in strings:
	# Encoding data using make() function
	#img = qrcode.make(x)
	# Saving as an image file
	#img.save('images/'+ x + '_QRCode' + '.png') 

	# create an instance from qrcode
	qr = qrcode.QRCode(version = 1,
                   box_size = 20,
                   border = 5)

	qr.add_data(x)
	qr.make(fit = True)
	img = qr.make_image(fill_color = "blue", back_color = "white")
	img.save('images/'+ x + '_qr_code' + '.png')