import base64

s = b"Hello, World"

ec = base64.b64encode(s)
print ("Encoded value = " + str(ec))

dc = base64.b64decode(ec)
print ("Decoded value = " + str(dc))

if (s == dc):
	print("Encoding and decoding successful!")
