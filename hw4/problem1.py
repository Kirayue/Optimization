from scipy.optimize import minimize
import numpy as np
import equation1 as eq
import sys

if __name__ == "__main__":
    x0 = np.random.random_sample((9,))
    #print(res.x)
    d = [0.0298, 0.044, 0.044, 0.0138, 0.0329, 0.0329, 0.0279, 0.025, 0.025, 0.0619, 0.0317, 0.0368] 
    cons = ({"type": 'eq', 'fun': lambda F: d[0] * F[0] - d[1] * F[1] - d[2] * F[2] - 4},
            {"type": 'eq', 'fun': lambda F: -d[3] * F[2] + d[4] * F[3] + d[5] * F[4] - d[7] * F[5] - d[8] * F[6] - 33},
            {"type": 'eq', 'fun': lambda F: d[6] * F[4] - d[9] * F[6] + d[10] * F[7] - d[11] * F[8] - 31}
            )
    bnds = ((0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None))
    res = minimize(eq.f, x0, method="SLSQP", bounds = bnds, constraints = cons, options = {'maxiter': 1e6, 'disp': False})
    print("SLSQP method:")
    print("    Starting point: {}".format(x0))
    print("    Iterations: {}".format(res.nit))
    print("    F: {}".format(res.x))
    print("    Z(F): {}".format(res.fun))
