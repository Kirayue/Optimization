from pylab import *
import time

def affine_scaling(c, A, b, x0, alpha=0.5, eps=10e-4):
    xk = x0
    delta_x = [inf]
    iteration = 0
    while norm(delta_x) > eps:
        Xk = diagflat(xk.T)
        yk = solve(A*Xk*Xk*A.T, A*Xk*Xk*c)
        zk = c - A.T*yk
        if all(zk==0):
            break
        delta_x = -(Xk*Xk*zk)/norm(Xk*zk)
        xk = xk + alpha*delta_x
        iteration += 1
    
    return xk, iteration


if __name__ == '__main__':
    c = matrix([[-4],
                [-5],
                [0],
                [0]])
    A = matrix([[-1, 1, 1, 0],
                [1, 1, 0, 1]])
    b = matrix([[4], 
                [6]])
    x1, x2 = 1, 1
    x0 = matrix([[x1], 
                 [x2],                
                 [b[0,0] - A[0,0]*x1 - A[0,1]*x2],
                 [b[1,0] - A[1,0]*x1 - A[1,1]*x2]])
     
    start = time.time()
    x_opt, iters = affine_scaling(c, A, b, x0)
    end = time.time()
    
    print("It spent {} seconds to optimize the objective function.".format(end - start))
    print("Test case1:")
    print('Current function value :{}'.format(c.T * x_opt))
    print("Iterations: {}".format(iters))
    print("x1: {}, x2: {}".format(x_opt[0], x_opt[1]))
    c = matrix([[-400],
                [-300],
                [0],
                [0],
                [0]])
    A = matrix([[60, 40, 1, 0, 0],
                [20, 30, 0, 1, 0],
                [20, 10, 0, 0, 1]])
    b = matrix([[3800], 
                [2100],
                [1200]])
    x1, x2 = 20, 10
    x0 = matrix([[x1], 
                 [x2],                
                 [b[0,0] - A[0,0]*x1 - A[0,1]*x2],
                 [b[1,0] - A[1,0]*x1 - A[1,1]*x2],
                 [b[2,0] - A[2,0]*x1 - A[2,1]*x2]])
     
    start = time.time()
    x_opt, iters = affine_scaling(c, A, b, x0)
    end = time.time()
    
    print("It spent {} seconds to optimize the objective function.".format(end - start))
    print("Test case2:")
    print('Current function value :{}'.format(c.T * x_opt))
    print("Iterations: {}".format(iters))
    print("x1: {}, x2: {}".format(x_opt[0], x_opt[1]))

