import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self, x_values, y_values):
        self.x_vals = x_values
        self.y_vals = y_values

    def show(self):
        plt.plot(self.x_vals, self.y_vals)
        plt.show()
    
    def plotPoint(self, coords):
        plt.plot(coords[0],coords[1],'go') 

#coefficients from x^o to x^0
class EqGraph(Graph):
    def __init__(self, x_min, x_max, points, coeffs):
        x_vals = np.linspace(x_min,x_max,points)
        y_vals = 0
        for i in range(len(coeffs)):
            y_vals += coeffs[len(coeffs)-(i+1)]*x_vals**i
        super().__init__(x_vals, y_vals)

