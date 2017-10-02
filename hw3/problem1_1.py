import sys
import equation as eq
import numpy as np
import numdifftools as nd
from random import uniform
from numpy.linalg import norm
from numpy.linalg import inv
def inBound(num, lower, upper):
    return num >= lower and num <= upper
if __name__ == '__main__':
    epsilon = float(sys.argv[1])
    x0 = [float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])]
    points = [np.array(x0)]
    #points = [np.array([2, 2])]
    iteration = -1
    print("Newton's method")
    deltaX = [1, 1, 1]  #use for checking to excute at least one time
    while norm(deltaX) > epsilon:
        current_P = points[-1]
        hessian = nd.Hessian(eq.f)(current_P)
        gradient = nd.Gradient(eq.f)(current_P)
        hessian_inv = inv(hessian)
        new_P = current_P - np.matmul(hessian_inv, gradient)
        deltaX = new_P - current_P
        #print(gradient)
        #print(hessian)
        #print(hessian_inv)
        #print(np.matmul(hessian, hessian_inv))
        points.append(new_P)
        iteration += 1
        #print(new_P)
    if inBound(points[-1][0], -10, 10) and inBound(points[-1][1], -10, 10):
        print("Using {} iterations to optimize!".format(iteration))
        print("The optimal point is  X = [{}, {}, {}] with f(X) = {}".format(points[-1][0], points[-1][1], points[-1][2],eq.f(points[-1])))
        #print("The optimal point is  X = [{}, {}] with f(X) = {}".format(points[-1][0], points[-1][1], eq.f(points[-1])))
    else:
        print("The pont is out of bound!")
        print("Please try again!")
