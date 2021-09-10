# generating a python map
alphabets = "abcdefghijklmnopqrstuvwxyz"
encryption = "DKVQFIBJWPESCXHTMYAUOLRGZN"
map = {}
for i in alphabets:
    map.update({i: ''})

for i in range(len(encryption)):
    map.update({alphabets[i]: encryption[i]})

map.update({' ': ' '})
print(map)
print("\n")
message = str(input("Enter the message: "))
encrypt_text = ""
for char in message:

    encrypt_text += map.get(char.lower())

print("Encrypted text: ", encrypt_text)
