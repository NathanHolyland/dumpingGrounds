from gaussianElim import *
from graphing_tool import EqGraph
import random

def generateRow(order, x):
    row = []
    for i in range(order, -1, -1):
        row.append(x**i)
    return row

def generatePolynomialMatrix(order, points):
    matrix_list = []
    result_vec = []
    print(order)
    for i in range(order+1):
        matrix_list.append(generateRow(order, points[i][0]))
        result_vec.append(points[i][1])
    return np.array(matrix_list, float), np.array(result_vec, float)

def userInput():
    points = []

    noPoints = int(input("no of points: "))
    rand = input("random? Y|N: ")
    x_min = np.Infinity
    x_max = -np.Infinity
    for i in range(noPoints):
        if rand == "Y":
            newPoint_x = random.randrange(-20, 20)
            newPoint_y = random.randrange(-20, 20)
        else:
            print(f"point {i}:")
            newPoint_x = float(input("enter X: "))
            newPoint_y = float(input("enter Y: "))
            print()
        if newPoint_x < x_min:
            x_min = newPoint_x
        elif newPoint_x > x_max:
            x_max = newPoint_x
        points.append(np.array([newPoint_x, newPoint_y]))
    return points, x_min, x_max

points, x_min, x_max = userInput()
print(f"min {x_min}, max {x_max}")
matrix, results = generatePolynomialMatrix(len(points)-1, points)
print(matrix)
inverse = gaussian(matrix)
print(f"{inverse} * {results}")
params = np.matmul(inverse, results)
print(f"\n\n\n\n\npoints:\n{points}")
print(f"\n\ncalculated parameters:\n{params}")

graph =  EqGraph(x_min, x_max, 10000, params)
for point in points:
    graph.plotPoint(point)
graph.show()