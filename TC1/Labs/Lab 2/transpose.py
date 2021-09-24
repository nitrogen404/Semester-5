
def createMatrix():
    matrix = []
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    
    for row in range(rows):
        temp = []
        for column in range(columns):
            element = float(input("Enter the element: "))
            temp.append(element)
        matrix.append(temp)

    return matrix

def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        temp = [0] * len(matrix)
        result.append(temp)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]

    return result


matrix = createMatrix()
print(matrix)
transpose = transpose(matrix)
print(transpose)