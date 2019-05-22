### CTCI solution ####
### Author : Prashant Kumar ####

## Zero matrix in place

def setrow(matrix,i):
    for j in range(len(matrix[0])):
        matrix[i][j] = 0
    return matrix

def setcolumn(matrix,i):
    for j in range(len(matrix)):
        matrix[j][i] = 0
    return matrix


def zeromatrix(matrix):
    row = len(matrix)
    column = len(matrix[0])

    rowlist = [False] * row
    columnlist = [False] * column

    for i in range(row):
        for j in range(column):
            if matrix[i][j] == 0:
                rowlist[i] = True
                columnlist[j] = True
    
    for i in range(len(rowlist)):
        if rowlist[i] == True:
            matrix = setrow(matrix,i)
    
    for i in range(len(columnlist)):
        if columnlist[i] == True:
            matrix = setcolumn(matrix,i)

    return matrix


matrix = [[1,2,1,4],[5,6,7,8],[9,0,11,12],[13,14,15,16]]

x = zeromatrix(matrix)

print(x)