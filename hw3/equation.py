def F1(x1, x2, x3):
    return 2 * (x1 ** 3) + 5 * x1 * x2 + 4 * x3 - 2 * (x1 ** 2) * x3 - 18
def F2(x1, x2, x3):
    return x1 + x2 ** 3 + x1 * (x2 ** 2) + x1 * (x3 ** 2) - 22
def F3(x1, x2, x3):
    return 8 * (x1 ** 2) + 2 * x2 * x3 + 2 * (x2 ** 2) + 3 * (x2 ** 3) - 52
def f(x):
    f1 = F1(x[0], x[1], x[2])
    f2 = F2(x[0], x[1], x[2])
    f3 = F3(x[0], x[1], x[2])
    return (f1 * (f2 ** 2) * f3 + f1 * f2 * (f3 ** 2) + f2 ** 2 + (x[0] + x[1] - x[2]) ** 2) ** 2

    #return 4 * (x[0] ** 2) + (x[1] ** 2) - 2 * x[0] - 4 * x[1] + 10
    #return 3 * (x[0] ** 2) + 2 * (x[1] ** 2) - 4 * x[0] * x[1] - 2 * x[0]