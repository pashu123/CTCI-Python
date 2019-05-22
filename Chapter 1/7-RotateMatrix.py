### CTCI solution ####
### Author : Prashant Kumar ####

## Inplace matrix substitution with while relying on small 
## maths


def rotate_matrix(matrix:list)->list:
    '''Gives the 90 degree rotated matrix i.e list of list'''
    # when is is not the square matrix
    if len(matrix) == 0 or len(matrix[0]) != len(matrix):
        return False
    
    n = len(matrix)
    for layer in range(0,n//2):
        # layer wise length set
        first = layer
        last = n-1-layer

        for i in range(first,last):
            # Set offset while moving in the same row
            offset = i - first

            # save the top variable
            top = matrix[first][i]

            # left to top
            matrix[first][i] = matrix[last- offset][first]

            # bottom to left
            matrix[last-offset][first] = matrix[last][last - offset]

            # right to bottom
            matrix[last][last - offset] = matrix[i][last]

            # top to right
            matrix[i][last] = top

    return matrix




matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

x = rotate_matrix(matrix)

print(x)

