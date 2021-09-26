binmessage = input("Enter the message: ")
binmessage = binmessage.replace(" ", "")
binkey = input("Enter the key: ")
binkey = binkey.replace(" ", "")

def encrypt(message, key):
	if len(key) < len(message):
		for i in range(len(message) - len(key)):
			key += key[i]
	
	encryptedTxt = ""
	for binary in range(len(message)):
		encryptedTxt += str(int('{0: b}'.format(ord(message[binary]))) ^ int('{0: b}'.format(ord(key[binary]))))
	return encryptedTxt


print(encrypt(binmessage, binkey))
