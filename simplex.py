from tkinter import E
import numpy as np

table = np.array([
    [1,-2,-3,-1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 2, 4, 0, 0, 1, 0],
    [0, 0, 7, 5, 0, 0, 1]
])

values = [0, 15, 13, 20]

def findPivot(matrix, results):
    pivot = [None, None]
    # find column (first non negative)
    for column in range(len(matrix[0])):
        if matrix[0][column] < 0:
            pivot[1] = column
            break
    # if column wasn't found return
    if pivot[1] == None:
        return pivot

    # look for lowest ratio between the elements in the pivot row and the corresponding results
    lowest_ratio = np.Infinity
    for row in range(len(matrix)):
        # if division by 0 skip
        if matrix[row][pivot[1]] == 0:
            continue
        # divide result by the corresponding pivot element
        ratio = results[row]/matrix[row][pivot[1]]
        # if ratio is the lowest so far, and non zero the pivot element is the current one
        if 0 < ratio < lowest_ratio:
            lowest_ratio = ratio
            pivot[0] = row
    return pivot

def rowSub(row1, row2, n):
    return row1-n*row2            

# assuming top row to be row of interest
def simplex(matrix, results):
    solution = matrix.copy()
    while True:
        print(f"current matrix:\n{solution}\nresult:\n{results}")
        pivot = findPivot(solution, results)
        if pivot[0] == None or pivot[1] == None:
            return solution, results
        print(f"pivot : {pivot}")

        # divide the pivot row to make the pivot element 1
        print(f"r{pivot[0]}/{solution[pivot[0]][pivot[1]]}")

        print(f"result r{pivot[0]} changed: {results[pivot[0]]} -> ", end="")
        results[pivot[0]] = results[pivot[0]]/solution[pivot[0]][pivot[1]]
        print(f"{results[pivot[0]]}")

        print(f"{solution[pivot[0]]} / {solution[pivot[0]][pivot[1]]} = ", end="")
        solution[pivot[0]] = solution[pivot[0]]/solution[pivot[0]][pivot[1]]
        print(solution[pivot[0]])
        
        # subtract the pivot row from each row to reduce the pivot column to 0
        for row in range(len(solution)):
            if (solution[row] == solution[pivot[0]]).all(): #skip the pivot for this step
                continue
            print(f"r{row} - r{pivot[0]}*({solution[row][pivot[1]]}/{solution[pivot[0]][pivot[1]]})")

            print(f"result r{row} changed: {results[row]} -> ", end="")
            results[row] = results[row]-results[pivot[0]]*(solution[row][pivot[1]]/solution[pivot[0]][pivot[1]])
            print(f"{results[row]}")

            
            solution[row] = rowSub(solution[row], solution[pivot[0]], solution[row][pivot[1]] / solution[pivot[0]][pivot[1]])
        

print(f"\nsolution:\n\n{simplex(table, values)}")




    