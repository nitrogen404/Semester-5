message = 'HHWKSWXSLGNTCG'
key = 'PASCAL'

def generateKey(oriKey, message):
  croppedKey = ""
  if len(message) == len(oriKey):
    return oriKey
  else:
    croppedKey = oriKey

  for i in range(len(message) - len(oriKey)):
    croppedKey += oriKey[i % len(oriKey)]
  return croppedKey  


def decryption(message, key):
  orignalMsg = []
  for i in range(len(message)):
    x = (ord(message[i]) - ord(key[i]) + 26) % 26
    x += ord('A')
    orignalMsg.append(chr(x))
  return "".join(orignalMsg)

croppedKey = generateKey(key, message)
print(decryption(message, croppedKey))

