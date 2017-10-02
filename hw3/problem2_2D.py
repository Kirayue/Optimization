import sys
from sympy import *
import equation_2D as eq
import solver as solver
import numpy as np
import numdifftools as nd
from random import uniform
from numpy.linalg import norm
from numpy.linalg import inv
import solver as sl
def inBound(num, lower, upper):
    return num >= lower and num <= upper
if __name__ == '__main__':
    epsilon = float(sys.argv[1])
    n = 2
    x0 = [float(sys.argv[2]), float(sys.argv[3])]
    points = [np.array(x0)]
    print("Fletcher-Reeves conjugate gradient method.")
    l = Symbol('l')
    iteration = -1
    j = 1
    gradient_now = nd.Gradient(eq.f)(points[0])
    direction = -1 * gradient_now
    while norm(direction) > epsilon:
        #Solve lumbda for minimizing f(x + lambda * gradient)
        current_P = points[-1]
        #print(current_P)
        #print(direction)
        gradient_now = nd.Gradient(eq.f)(current_P)
        temp_new_P = current_P + l * direction
        #print(temp_new_P)
        Lambda = sl.findLambda(eq.f(temp_new_P), l)
        #print(Lambda)
        #print(Lambda)
        new_P = current_P + Lambda * direction
        #print(new_P)
        points.append(new_P)
        gradient_next = nd.Gradient(eq.f)(new_P)
        if j < n:
            beta = np.matmul(gradient_next, gradient_next) / np.matmul(gradient_now, gradient_now)
        #    print(beta)
            direction = -1 * gradient_next + beta * direction
            j += 1
        else:
            direction = -1 * gradient_next
            j = 1
        iteration += 1
    if inBound(points[-1][0], -10, 10) and inBound(points[-1][1], -10, 10): #and inBound(points[-1][2], -10, 10):
        print("Using {} iterations to optimize!".format(iteration))
        print("The optimal point is  X = [{}, {}] with f(X) = {}".format(points[-1][0], points[-1][1], eq.f(points[-1])))
    else:
        print("The point is out of bound!")
        print("Please try again!")
