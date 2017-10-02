import sys
import math
import matplotlib.pyplot as plt
import equation as eq
from sympy import *

def golden(equation, upper, lower, model, e):
    alpha = 0.618
    listOfx1 = []
    listOfx2 = []
    listOfupper = [upper]
    listOflower = [lower]
    listOfx1value = []
    listOfx2value = []
    l = Symbol('l')
    init = equation.subs(l, upper) if equation.subs(l, upper) < equation.subs(l, lower) else equation.subs(l, lower)
    listOfvalue = [init] 
    count = 0
    while upper - lower > e:
        #print(e)
        #print(upper - lower)
        x1 = alpha * lower + (1 - alpha) * upper
        x2 = alpha * upper + (1 - alpha) * lower
        #print(x1, x2)
        count += 1
        listOfx1.append(x1)
        listOfx2.append(x2)
        listOfx1value.append(equation.subs(l, x1))
        listOfx2value.append(equation.subs(l, x2))
        if model == 'min':
            if equation.subs(l, x1) <= equation.subs(l, x2):
                listOfvalue.append(equation.subs(l, x1))
                upper = x2
            else:
                listOfvalue.append(equation.subs(l, x2))
                lower = x1
        listOfupper.append(upper)
        listOflower.append(lower)
    #print("{}: x = {}, y = {}".format(m, listOfupper[-1], listOfvalue[-1]))
    #print('Done: ' + str((listOfupper[-1] + listOflower[-1]) / 2))
    print("Golden search done!")
    return (listOfupper[-1] + listOflower[-1]) / 2
if __name__ == "__main__":
    l = 3
    upper = 99
    lower = 1
    #m = sys.argv[1]
