import sys
import math
import matplotlib.pyplot as plt

def equation(x):
    return x ** 2 * math.cos(x)# math.cos(x)

def dichotomous(upper, lower, model, l):
    listOfx1 = []
    listOfx2 = []
    listOfupper = [upper]
    listOflower = [lower]
    listOfx1value = []
    listOfx2value = []
    init = equation(upper) if equation(upper) < equation(lower) else equation(lower)
    listOfvalue = [init] 
    while upper - lower > l:
        x1 = (lower + upper) / 2 - epsilon
        x2 = (lower + upper) / 2 + epsilon
        listOfx1.append(x1)
        listOfx2.append(x2)
        listOfx1value.append(equation(x1))
        listOfx2value.append(equation(x2))
        if model == 'min':
            if equation(x1) <= equation(x2):
                listOfvalue.append(equation(x1))
                upper = x2
            else:
                listOfvalue.append(equation(x2))
                lower = x1
        else:
            if equation(x1) <= equation(x2):
                listOfvalue.append(equation(x2))
                lower = x1
            else:
                listOfvalue.append(equation(x1))
                upper = x2
        listOfupper.append(upper)
        listOflower.append(lower)
    print("{}: x = {}, y = {}".format(m, listOfupper[-1], listOfvalue[-1]))
    return listOfvalue
if __name__ == "__main__":
    l = float(sys.argv[1])
    upper = float(sys.argv[3])
    lower = float(sys.argv[2])
    epsilon = l/10
    m = sys.argv[4]
    listOfvalue = dichotomous(upper, lower, m, l)
    x = list(range(len(listOfvalue)))
    plt.scatter(x, listOfvalue)
    plt.ylabel('function value')
    plt.xlabel('iteration')
    plt.show()
