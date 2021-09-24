# 20190802117

plainText = input("Enter the message: ")
plainText = plainText.replace(" ", "")
plainText = plainText.lower()
print(plainText)
abc = "abcdefghijklmnopqrstuvwxyz"
key = [4, 3, 1, 2, 5, 6, 7]
matrix = []
encrypted_txt = ""
last_seen = 0
for row in range(len(key)):
    # if last_seen < len(plainText):
    string = plainText[row: : len(key)]

    if len(string) < len(plainText) % len(key): 
        string += abc[0 - (len(key) - row)]
    matrix.append(string)

print(matrix)

for index in key:
    encrypted_txt += matrix[index - 1]

print(encrypted_txt)




