from scipy.optimize import linprog
from pprint import pprint
import time

if __name__ == '__main__':
    c = [-4, -5]
    A = [[-1, 1], [1, 1]]
    b = [4, 6]
    x0_bound = (0, None)
    x1_bound = (0, None)
    #x2_bound = (0, None)
    start = time.time()
    res = linprog(c, A_ub = A, b_ub = b, bounds = (x0_bound, x1_bound), options = {"disp": True})
    end = time.time()
    pprint("It spent {} seconds to optimize the objective functin.".format((end - start)))
    pprint("Test Case 1:")
    pprint(res)

    c = [-400, -300]
    A = [[60, 40], [20, 30], [20, 10]]
    b = [3800, 2100, 1200]
    x0_bound = (0, None)
    x1_bound = (0, None)
    start = time.time()
    res = linprog(c, A_ub = A, b_ub = b, bounds = (x0_bound, x1_bound), options = {"disp": True})
    end = time.time()
    pprint("It spent {} seconds to optimize the objective functin.".format((end - start)))
    pprint("Test Case 2:")
    pprint(res)
