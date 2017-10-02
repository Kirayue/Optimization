from scipy.optimize import minimize
import numpy as np
import equation2 as eq
import sys

if __name__ == "__main__":
    x0 = np.random.random_sample((2,))
    #print(res.x)
    cons = (
            {"type": 'ineq', 'fun': lambda y: 12 - 3 * y[0] + 2 * y[1]},
            {"type": 'ineq', 'fun': lambda y: 2 * y[0] + y[1] - 8}, 
            {"type": 'eq', 'fun': lambda y: y[0] + y[1] - 6}
            )
    bnds = ((0, None), (None, None))
    res = minimize(eq.f, x0, method="SLSQP", bounds = bnds, constraints = cons, options = {'maxiter': 1e6, 'disp': False})
    print("SLSQP method:")
    print("    Starting point: {}".format(x0))
    print("    Iterations: {}".format(res.nit))
    print("    Y: {}".format(res.x))
    print("    f(Y): {}".format(res.fun))
