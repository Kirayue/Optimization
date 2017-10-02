import sys
import math
import matplotlib.pyplot as plt

def equation(w, n, k):
    return n * math.log(w, 10) + 2 * (k + 1) * (n / (n - k - 2)) if n / (k + 1) < 40 else n * math.log(w, 10) + 2 *(k + 1)# math.cos(x)
def golden(upper, lower, model, l):
    alpha = 0.618
    listOfx1 = []
    listOfx2 = []
    listOfupper = [upper]
    listOflower = [lower]
    listOfx1value = []
    listOfx2value = []
    init = equation(upper) if equation(upper) < equation(lower) else equation(lower)
    listOfvalue = [init] 
    while upper - lower > l:
        x1 = alpha * lower + (1 - alpha) * upper
        x2 = alpha * upper + (1 - alpha) * lower
        listOfx1.append(x1)
        listOfx2.append(x2)
        listOfx1value.append(equation(x1))
        listOfx2value.append(equation(x2))
        if model == 'min':
            if equation(x1) <= equation(x2):
                listOfvalue.append(equation(x1))
                upper = math.floor(x2)
            else:
                listOfvalue.append(equation(x2))
                lower = math.floor(x1)
        else:
            if equation(x1) <= equation(x2):
                listOfvalue.append(equation(x2))
                lower = math.floor(x1)
            else:
                listOfvalue.append(equation(x1))
                upper = math.floor(x2)
        listOfupper.append(upper)
        listOflower.append(lower)
    print("{}: x = {}, y = {}".format(m, listOfupper[-1], listOfvalue[-1]))
    return listOfvalue
if __name__ == "__main__":
    l = 3
    upper = 99
    lower = 1
    m = sys.argv[1]
    equation(5, 500, 3)
    exit()
    listOfvalue = golden(upper, lower, m, l)
    x = list(range(len(listOfvalue)))
    #plt.scatter(x, listOfvalue)
    #plt.ylabel('function value')
    #plt.xlabel('iteration')
    #plt.show()
