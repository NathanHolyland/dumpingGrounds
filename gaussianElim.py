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

    return row_1 - scale_factor*row_2#

def eliminate(matrix, inverse, size, r, c, exclusions):
    # if value was sourced from subtraction look elsewhere
    # if subtraction will result in elimination of diagonal look elsewhere
    print(f"exlcuded operations: {exclusions}")
    if [r,c] in exclusions or matrix[r][r] == (matrix[c][r])*(matrix[r][c]/matrix[c][c]):
        resolved = False
        for i in range(size):
            # if the matrix contains nothing skip
            # if the new row is the same as the current row skip
            # if the new row is one of the identities skip
            # if the identity on the current row will get eliminated by the operation skip
            if matrix[i][c] == 0 or i==r or i==c:
                continue
            if matrix[r][r] == matrix[c][i]*(matrix[r][c]/matrix[i][c]):
                continue
            resolved =  True
            print(f"R{r} - {matrix[r][c]}/{matrix[i][c]} * R{i} > R{r}")
            inverse[r] = rowSub(inverse, r, i, (matrix[r][c]/matrix[i][c]))
            matrix[r] = rowSub(matrix, r, i, (matrix[r][c]/matrix[i][c]))
            print(matrix)
        if resolved:
            return
            
        # find a row to add to the identity on current row (which wont increase [r][c] by the same ratio)
        for i in range(size):
            # if position contains nothing or is current position skip
            if matrix[i][r] == 0 or i==r:
                continue
            # if the ratio will increase by the same factor with the row operation skip
            if matrix[i][c]/matrix[r][c] == matrix[i][r]/matrix[r][r]:
                continue

            print(f"R{r} - R{i} > R{r}")
            inverse[r] = rowSub(inverse, r, i)
            matrix[r] = rowSub(matrix, r, i)
            print(matrix)
        # repeat elimination step
        eliminate(matrix, inverse, size, r, c, exclusions)
        return

    print(f"R{r} - {matrix[r][c]}/{matrix[c][c]} * R{c} > R{r}")
    inverse[r] = rowSub(inverse, r, c, (matrix[r][c]/matrix[c][c]))
    matrix[r] = rowSub(matrix, r, c, (matrix[r][c]/matrix[c][c]))
    print(matrix)
    

def gaussian(M):
    matrix = M.copy()
    size = checkSquare(matrix)
    inverse = np.identity(size)
    if not size:
        print("matrix is not square")
        return None
    if np.linalg.det(M) == 0:
        print("matrix is not invertible")
        return None

    # handle zeros in diag
    exclusions = []
    for i in range(size):
        if matrix[i][i] == 0:
            for j in range(size):
                if matrix[j][i] == 0 or i==j:
                    continue
                print(f"R{i} - 1/{matrix[j][i]} * R{j} > R{i}")
                inverse[i] = rowSub(inverse, i, j, -1/matrix[j][i])
                matrix[i] = rowSub(matrix, i, j, -1/matrix[j][i])
                print(matrix)
                exclusions.append([i,j])
                break

    # bottom side elimination
    for c in range(size):
        for r in range(size):
            if r <= c:
                continue
            eliminate(matrix, inverse, size, r, c, exclusions)
    
    # top side elimination
    for c in range(size):
        for r in range(size):
            if r >= c:
                continue
            eliminate(matrix, inverse, size, r, c, exclusions)
    
    for i in range(size):
        print(f"R{i}/{matrix[i][i]} > R{i}")
        inverse[i] = inverse[i] / matrix[i][i]
        matrix[i] = matrix[i] / matrix[i][i]
    
    print(f"final:\n{matrix}")
    
    return inverse

def testCase():
    M = np.array([
        [-1, 1, -1, 1, -1, 1],
        [0, 0, 0, 0, 0, 1],
        [32, 16, 8, 4, 2, 1],
        [1024, 256, 64, 16, 4, 1],
        [7776, 1296, 216, 36, 6, 1],
        [16807, 2401, 343, 49, 7, 1]
    ],float)
    print(gaussian(M))

testCase()