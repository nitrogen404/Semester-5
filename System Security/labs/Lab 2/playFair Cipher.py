# code by Chandan Dhamande aka Nitrogen
# nitrogen404.github.io/nitrochan
# provisional code for Playfair cipher. Still needs some improvements. @10/9/21
# fixed the bugs @11/9/21

import pprint

alpha = "abcdefghiklmnopqrstuvwxyz"
message = str(input("Enter the message: "))
key = str(input("Enter the key: "))

message = message.replace(" ", "")
message = message.lower()
key = key.replace(" ", "")
key = key.lower()


# if len(key) % 2 != 0:
#     key += 'z'
# if len(key) % 2 != 0:
#     key += 'z'


keySet = ""  # removing duplicates from the key
repeating = [] 
for char in key:
    if char not in repeating:
        keySet += char
        repeating.append(char)


def matrixGeneration(text, key): # step 1: matrix generation
    global alpha
    matrix = []
    lastIndex = 0
    lastalphaIndex = 0
    
    alphaminuskey = []  # contains alphabets that arent common in keySet and alpha
    for char in alpha:
        if char not in keySet:
            alphaminuskey += [char]

    for i in range(5):
        row = ""
        while len(row) < 5 and lastIndex < len(key):
            row += key[lastIndex]
            lastIndex += 1
        matrix.append(row)


    for row in matrix:
        if len(row) < 5:
            tempRow = row[:len(row) + 1]
            while len(tempRow) < 5 and lastalphaIndex < len(alphaminuskey):
                tempRow += alphaminuskey[lastalphaIndex]
                lastalphaIndex += 1
            matrix[matrix.index(row)] = tempRow

    return matrix

# thisismessage
def generateDiagraph(text):  # Step: generating diagraphs from the message
    diagraph = []
    for i in range(0, len(text) + 1, 2):
        if i < len(text) - 1:
            if text[i] == text[i + 1]:
                text = text[:i + 1] + 'x' + text[i + 1:]
    if len(text) % 2 != 0:
        text = text[:] + 'x'

    for i in range(0, len(text) - 1, 2):
        diastr = ""
        # row = []
        # row += [text[i], text[i + 1]]
        # diagraph.append(row)
        diastr += str(text[i])
        diastr += str(text[i + 1])
        diagraph.append(diastr)
    
    return diagraph
    

def encryption(matrix, diagraph):
    cipherText = ""
    # if letters in same row
    for pair in diagraph:
        flag = False
        for row in matrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])
                cipherText += row[(j0 + 1) % 5] + row[(j1 + 1) % 5]
                flag = True
        if flag:
            continue

        # if letters in same column
        for j in range(5):
            col = "".join([matrix[i][j] for i in range(5)])
            if pair[0] in col and pair[1] in col:
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])
                cipherText += col[(i0 + 1) % 5] + col[(i1 + 1) % 5]
                flag = True
        
        if flag:
            continue

        i0 = 0
        i1 = 0
        j0 = 0
        j1 = 0

        for i in range(5):
            row = matrix[i]
            if pair[0] in row:
                i0 = i # row
                j0 = row.find(pair[0]) # fetch the index

            if pair[1] in row:
                i1 = i  # index of row
                j1 = row.find(pair[1])  # fetch the index of column number
        cipherText += matrix[i0][j1] + matrix[i1][j0]


    return cipherText

# pprint.pprint(generateDiagraph(message))
diagraph = generateDiagraph(message)
# pprint.pprint(diagraph)
# print("\n")
# pprint.pprint(matrixGeneration(message, keySet)) 
matrix = matrixGeneration(message, keySet)
# pprint.pprint(matrix)
print("Cipher Text: ", encryption(matrix, diagraph))









