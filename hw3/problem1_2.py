import sys
import equation as eq
import numpy as np
import numdifftools as nd
from random import uniform
from numpy.linalg import norm
from numpy.linalg import inv
from sympy import *
import solver as sl
import golden as gd 
def inBound(num, lower, upper):
    return num >= lower and num <= upper
if __name__ == '__main__':
    golden_upper = 10
    golden_lower = -10
    epsilon = float(sys.argv[1])
    x0 = [float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])]
    points = [np.array(x0)]
    B = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    l = Symbol('l')
    iteration = 1
    print("Quasi-Newton's method: DFP")
    gradient_next = nd.Gradient(eq.f)(points[0])
    while norm(gradient_next) > epsilon and iteration < 1000:
        print("Iteration: " + str(iteration))
        current_P = points[-1]
        gradient_now = nd.Gradient(eq.f)(current_P)
        print("Point: " + str(current_P) + " value: " + str(eq.f(current_P)))
        print("Gradient: " + str(gradient_now))
        direction = -1 * np.matmul(B, gradient_now)
        temp_new_P = current_P + l * direction
        #print(eq.f(temp_new_P))
        #Lambda = sl.findLambda(eq.f(temp_new_P), l)
        Lambda = gd.golden(eq.f(temp_new_P), 10, -10, 'min', 0.001)
        print("Lambda: "+str(Lambda))
        print(current_P)
        print(direction)
        new_P = current_P + Lambda * direction
        print("Next Point: " + str(new_P))
        points.append(new_P)
        gradient_next = nd.Gradient(eq.f)(new_P)
        g = gradient_next - gradient_now
        M = Lambda * np.outer(direction, direction) / np.matmul(direction, g)
        N = -1 * np.outer(np.matmul(B, g), np.matmul(B, g)) / np.matmul(g, np.matmul(B, g))
        B = B + M + N
        iteration += 1
    if iteration >= 1000:
        print("Running too many iterations.")

    if inBound(points[-1][0], -10, 10) and inBound(points[-1][1], -10, 10)and inBound(points[-1][2], -10, 10): #and inBound(points[-1][2], -10, 10):
        print("Using {} iterations to optimize!".format(iteration - 1))
        print("The optimal point is  X = [{}, {}, {}] with f(X) = {}".format(points[-1][0], points[-1][1], points[-1][2], eq.f(points[-1])))
        #print("The optimal point is  X = [{}, {}] with f(X) = {}".format(points[-1][0], points[-1][1], eq.f(points[-1])))
    else:
        print("The point is out of bound!")
        print("Please try again!")
