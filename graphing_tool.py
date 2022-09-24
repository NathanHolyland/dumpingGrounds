import matplotlib.pyplot as plt
import numpy as np
from gaussianElim import *

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
    x_min = np.Infinity
    x_max = -np.Infinity
    for i in range(noPoints):
        print(f"point {i}:")
        newPoint_x = float(input("enter X: "))
        newPoint_y = float(input("enter Y: "))
        if newPoint_x < x_min:
            x_min = newPoint_x
        elif newPoint_x > x_max:
            x_max = newPoint_x
        print()
        points.append(np.array([newPoint_x, newPoint_y]))
    return points, x_min, x_max

def PolyCoefficients(x, coeffs):
    y = 0
    for i in range(len(coeffs)):
        y += coeffs[len(coeffs)-(i+1)]*x**i
    return y

points, x_min, x_max = userInput()
print(f"points: {points}")
print(f"min {x_min}, max {x_max}")
matrix, results = generatePolynomialMatrix(len(points)-1, points)
print(matrix)
inverse = gaussian(matrix)
print(f"{inverse} * {results}")
params = np.matmul(inverse, results)
print(f"calculated parameters:\n{params}")

x = np.linspace(x_min,x_max,10000)

# plot the function
plt.plot(x, PolyCoefficients(x, params))
plt.show()

