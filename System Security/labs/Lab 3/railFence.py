plainText = input("Enter the message: ")
rows = int(input("Enter the number of rows: "))
plainText = plainText.replace(" ", "")
plainText = plainText.lower()
print("Plaintext without spaces: ", plainText)
# we are discovered run at once
# 2n - 2 - first row

def encryption(plainText, rows):
    cipherText = ""
    for row in range(rows):
        index = 0
        # the first row
        if row == 0:
            while index < len(plainText):
                cipherText += plainText[index]
                index += 2 * rows - 2
        elif row == rows - 1: # the last row
            index = row
            while index < len(plainText):
                cipherText += plainText[index]
                index += 2 * rows - 2
        else:  # intermediate rows
            left_offset = row
            right_offset = 2 * rows - 2 - row
            while left_offset < len(plainText):
                cipherText += plainText[left_offset]
                if right_offset < len(plainText):
                    cipherText += plainText[right_offset]
                left_offset += 2 * rows - 2
                right_offset += 2 * rows - 2
    return cipherText

def decrytion(encrypted):
    global rows
    plainText = "." * len(encrypted)

    cycle = 2 * rows - 2
    units = len(encrypted) // cycle
    
    rail_lengths = [0] * rows
    rail_lengths[0] = units  # estimating the characters in the first row

    # estimating the characters in the intermediate rows
    for i in range(1, rows - 1):
        rail_lengths[i] = 2 * units
    
    rail_lengths[rows - 1] = units  # estimating the characters in the last row

    for i in range(len(encrypted) % cycle):
        if i < rows:
            rail_lengths[i] += 1
        else:
            rail_lengths[cycle - i] += 1


    # decryption for the first rail
    index = 0
    rail_offset = 0
    for char in encrypted[:rail_lengths[0]]:
        plainText = plainText[:index] + char + plainText[index + 1:]
        index += cycle

    # decryption for the intermediate rails
    rail_offset += rail_lengths[0]
    for row in range(1, rows - 1):
        left_index = row
        right_index = cycle - row
        left_char = True
        for char in encrypted[rail_offset: rail_offset + rail_lengths[row]]:
            if left_char:
                plainText = plainText[:left_index] + char + plainText[left_index + 1:]
                left_index += cycle
                left_char = False
            else:
                plainText = plainText[:right_index] + char + plainText[right_index + 1:]
                right_index += cycle
                left_char = True
        rail_offset += rail_lengths[row]
    # decryptions for the last rail
    index = rows - 1

    for char in encrypted[rail_offset: ]:
        plainText = plainText[:index] + char + plainText[index + 1:]
        index += cycle
    return plainText

encrypted = encryption(plainText, rows)
print("encrypted message: ", encrypted)
print("Decrypted message: ", decrytion(encrypted))


