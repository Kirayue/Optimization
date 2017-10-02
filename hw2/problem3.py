import sys
from pprint import pprint
from random import uniform
import math
import numpy as np
import matplotlib.pyplot as plt

def equation(p):
    x1 = p[0]
    x2 = p[1]
    #return x1  -  x2
    return (4 - 2.1 * (x1 ** 2) + (x1 ** 4) / 3) * (x1 ** 2) + x1 * x2 + (4 * (x2 ** 2) - 4) * (x2 ** 2)

def distance(xa, xb):
    return math.sqrt((xa[0] - xb[0]) ** 2 + (xa[1] - xb[1]) ** 2) 

def center(p1, p2, p3):
    return [(p1[0] + p2[0] + p3[0]) / 3, (p1[1] + p2[1] + p3[1]) / 3]

def middle(p1, p2):
    return np.array([(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2])

def minimum(p1, p2):
    return np.array(p1) if equation(p1) > equation(p2) else np.array(p2)

def DownHill(xlower, xupper, ylower, yupper, epsilon):
    alpha = 1
    gamma = 2
    beta = 0.5
    init_p1 = np.array([uniform(xlower, xupper), uniform(ylower, yupper)])
    init_p2 = np.array([uniform(xlower, xupper), uniform(ylower, yupper)])
    init_p3 = np.array([uniform(xlower, xupper), uniform(ylower, yupper)])
    p = [center(init_p1, init_p2, init_p3)]
    candi = np.array(sorted([init_p1, init_p2, init_p3], key = lambda p : equation(p)))
    while distance(candi[0], candi[2]) > epsilon:
        xa = middle(candi[0], candi[1])   
        xr = xa + alpha * (xa - candi[2])
        if equation(candi[0]) > equation(xr):
            xe = xa + gamma * (xr - xa)
            if equation(xr) > equation(xe):
                candi[2] = xe
            else:
                candi[2] = xr
            candi = sorted(candi, key = lambda p : equation(p))
        else:
            if equation(candi[1]) >= equation(xr):
                candi[2] = xr
                candi = sorted(candi, key = lambda p : equation(p))
            else:
                xp = minimum(xr, candi[2])
                xc = xa + beta * (xp - xa)
                if equation(xc) > equation(xp):
                    xtemp = candi[0]
                    for index, point in enumerate(candi):
                        candi[index] = point + (xtemp - point) / 2
                else:
                    candi[2] = xc
                candi = sorted(candi, key = lambda p : equation(p))
        p.append(center(candi[0], candi[1], candi[2]))
    return p

if __name__ == "__main__":
    x1_upper = 2
    x1_lower = -2
    x2_upper = 2
    x2_lower = -2
    epsilon = 0.00001
    p = DownHill(x1_lower, x1_upper, x2_lower, x2_upper, epsilon)
    y = []
    for point in p:
        y.append(equation(point))
    v = list(range(len(y)))
    print("x1 = {}, x2 = {}, f(x1, x2) = {}".format(p[-1][0], p[-1][1], equation(p[-1])) )
    plt.scatter(v, y)
    plt.ylabel('function value')
    plt.xlabel('iteration')
    plt.show()
