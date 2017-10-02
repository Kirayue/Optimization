import sys
from random import uniform
import math
import matplotlib.pyplot as plt

def equation(x1, x2):
    #return x1 ** 2 + 2 * x2 - 7
    return (4 - 2.1 * (x1 ** 2) + (x1 ** 4) / 3) * (x1 ** 2) + x1 * x2 + (4 * (x2 ** 2) - 4) * (x2 ** 2)

def distance(xa, xb):
    result = math.sqrt((xa[0] - xb[0]) ** 2 + (xa[1] - xb[1]) ** 2) 
    return result
def golden(upper, lower, model, l, d, anotherX):
    alpha = 0.618
    listOfx1 = []
    listOfx2 = []
    listOfupper = [upper]
    listOflower = [lower]
    while upper - lower > l:
        x1 = alpha * lower + (1 - alpha) * upper
        x2 = alpha * upper + (1 - alpha) * lower
        listOfx1.append(x1)
        listOfx2.append(x2)
        if model == 'min':
            if d == 0:
                if equation(x1, anotherX) <= equation(x2, anotherX):
                    upper = x2
                else:
                    lower = x1
            elif d == 1:
                if equation(anotherX, x1) <= equation(anotherX, x2):
                    upper = x2
                else:
                    lower = x1
        else:
            if d == 0:
                if equation(x1, anotherX) <= equation(x2, anotherX):
                    upper = x2
                else:
                    lower = x1
            elif d == 1:
                if equation(anotherX, x1) <= equation(anotherX, x2):
                    lower = x1
                else:
                    upper = x2
        listOfupper.append(upper)
        listOflower.append(lower)
    return listOfupper, listOflower
if __name__ == "__main__":
    x1_upper = 2
    x1_lower = -2
    x2_upper = 2
    x2_lower = -2
    l = 0.00001
    epsilon = 0.000001
    init_x1 = uniform(x1_lower, x1_upper)
    init_x2 = uniform(x2_lower, x2_upper)
    x = [[init_x1, init_x2]]
    # first time 
    listOfupperX1, listOflowerX1 = golden(x1_upper, x1_lower, 'min', l, 0, init_x2)
    x1 = listOflowerX1[-1]
    listOfupperX2, listOflowerX2 = golden(x2_upper, x2_lower, 'min', l, 1, x1)
    x2 = listOflowerX2[-1]
    x.append([x1, x2])
    while distance(x[-2], x[-1]) > epsilon:
        listOfupperX1, listOflowerX1 = golden(x1_upper, x1_lower, 'min', l, 0, x2)
        x1 = listOflowerX1[-1]
        listOfupperX2, listOflowerX2 = golden(x2_upper, x2_lower, 'min', l, 1, x1)
        x2 = listOflowerX2[-1]
        x.append([x1, x2])
    y = []
    for point in x:
        y.append(equation(point[0], point[1]))
    v = list(range(len(y)))
    print("x1 = {}, x2 = {}, f(x1, x2) = {}".format(x[-1][0], x[-1][1], equation(x[-1][0], x[-1][1])) )
    plt.scatter(v, y)
    plt.ylabel('function value')
    plt.xlabel('iteration')
    plt.show()
