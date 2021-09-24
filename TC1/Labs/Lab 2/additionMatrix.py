# addition of two matrices

import pprint
pp = pprint.PrettyPrinter(indent=4)

def createMatrix():
    matrix = []
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    
    if rows != columns:
        print("In order to add matrices, their dimensions must be same")
        createMatrix()
    
    for row in range(rows):
        temp = []
        for column in range(columns):
            element = float(input("Enter the element: "))
            temp.append(element)
        matrix.append(temp)

    return matrix



def add(matrixA, matrixB):
    resultant = []
    for row in range(len(matrixA)):
        temp = []
        for i in range(len(matrixA[row])):
            temp.append(matrixA[row][i] + matrixB[row][i])
        resultant.append(temp)

    return resultant

matrixA = createMatrix()
matrixB = createMatrix()
pp.pprint(matrixA)
pp.pprint(matrixB)

pp.pprint(add(matrixA, matrixB))




