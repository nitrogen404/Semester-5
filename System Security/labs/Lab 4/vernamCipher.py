message = input("Enter the message: ")
message = message.replace(" ", "")
key = input("Enter the key: (Please note the letter casing) ")

def vernamEncrypt(message, key):
	if len(key) < len(message):
		for i in range(len(message) - len(key)):
			key += key[i]
	
	encryptedTxt = ""
	for i in range(len(message)):
		encryptedTxt += chr(ord(message[i]) ^ ord(key[i]))

	return encryptedTxt

print(vernamEncrypt(message, key))