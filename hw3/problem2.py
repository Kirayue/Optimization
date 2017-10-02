import sys
from sympy import *
import equation as eq
import solver as solver
import numpy as np
import numdifftools as nd
from random import uniform
from numpy.linalg import norm
from numpy.linalg import inv
import solver as sl
import golden as gd 
def inBound(num, lower, upper):
    return num >= lower and num <= upper
if __name__ == '__main__':
    epsilon = float(sys.argv[1])
    n = 3
    x0 = [float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])]
    points = [np.array(x0)]
    print("Fletcher-Reeves conjugate gradient method.")
    l = Symbol('l')
    iteration = 1
    j = 1
    gradient_now = nd.Gradient(eq.f)(points[0])
    direction = -1 * gradient_now
    while norm(direction) > epsilon:
        #Solve lumbda for minimizing f(x + lambda * gradient)
        print("Iteration: " + str(iteration))
        current_P = points[-1]
        print("Point: " + str(current_P) + " value: " + str(eq.f(current_P)))
        print("Gradient: " + str(gradient_now))
        gradient_now = nd.Gradient(eq.f)(current_P)
        temp_new_P = current_P + l * direction
        Lambda = gd.golden(eq.f(temp_new_P), 10, -10, 'min', 0.001)
        print("Lambda: "+str(Lambda))
        new_P = current_P + Lambda * direction
        #print(new_P)
        print("Next Point: " + str(new_P))
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
    if inBound(points[-1][0], -10, 10) and inBound(points[-1][1], -10, 10) and inBound(points[-1][2], -10, 10): #and inBound(points[-1][2], -10, 10):
        print("Using {} iterations to optimize!".format(iteration - 1))
        print("The optimal point is  X = [{}, {}, {}] with f(X) = {}".format(points[-1][0], points[-1][1], points[-1][2],eq.f(points[-1])))
        #print("The optimal point is  X = [{}, {}] with f(X) = {}".format(points[-1][0], points[-1][1], eq.f(points[-1])))
    else:
        print("The point is out of bound!")
        print("Please try again!")
