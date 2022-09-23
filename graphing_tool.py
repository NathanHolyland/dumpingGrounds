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

points, x_min, x_max = userInput()
x = np.linspace(-x_min,x_max,1000)
print(x)

y = np.zeros(np.shape(x), float)
for order in range(1, len(points)):
    matrix, results = generatePolynomialMatrix(order, points)
    print(results)
    if np.linalg.det(matrix) == 0:
        continue
    inverse = gaussian(matrix)
    params = results * inverse
    print(params)
    for i in range(len(params)):
        print(params[i])
        if i == len(params)-1:
            y+=params[i]
            break
        y += params[i]*(x**(order-i))
    break

print(y)

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')
plt.show()

