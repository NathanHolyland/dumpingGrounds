from random import gauss
import numpy as np

def checkSquare(matrix):
    if np.size(matrix, 0) != np.size(matrix, 1):
        return None
    return np.size(matrix, 0)

def rowSub(matrix, n1, n2, scale_factor=1):
    dimension = [np.size(matrix, 0), np.size(matrix, 1)]
    if n1 > np.size(matrix, 0):
        print(f"called row {n1} out of {dimension[0]}")
        return
    if n2 > np.size(matrix, 0):
        print(f"called row {n2} out of {dimension[0]}")
        return
    row_1 = matrix[n1]
    row_2 = matrix[n2]

    matrix[n1] = row_1 - scale_factor*row_2

def gaussian(M):
    matrix = M.copy()
    size = checkSquare(matrix)
    inverse = np.identity(size)
    if not size:
        print("matrix is not square")
        return
    if np.linalg.det(M) == 0:
        print("matrix is not invertible")
        return

    for c in range(size):
        for r in range(size):
            if r == c:
                continue
            print()
            print(matrix)
            print(inverse)
            rowSub(inverse, r, c, (matrix[r][c]/matrix[c][c]))
            rowSub(matrix, r, c, (matrix[r][c]/matrix[c][c]))
    
    for i in range(size):
        inverse[i] = inverse[i] / matrix[i][i]
        matrix[i] = matrix[i] / matrix[i][i]
        print()
        print(matrix)
        print(inverse)

    return inverse