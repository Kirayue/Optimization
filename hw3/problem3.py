from scipy.optimize import minimize
import equation as eq
import sys
x0 = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]
res = minimize(eq.f, x0, method="Nelder-Mead", options = {'maxiter': 1e6, 'disp': True})
print(res.x)
