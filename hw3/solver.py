from sympy import *
def findLambda(equation, x):
    #print(equation)
    df = diff(equation, x)
    ddf = diff(df, x)
    stationary_points = solve(df, x)
    #print(stationary_points)
    #print(df)
    #print(ddf)
    miniums = []
    for stationary_point in stationary_points:
        if ddf.subs(x, stationary_point) >= 0:
            miniums.append(stationary_point)
    if miniums:
        Lambda = sorted(miniums, key = lambda minium: equation.subs(x, minium))[0]
        print("Lambda :{}".format(Lambda))
        return float(Lambda)
    else:
        print("There is no local minium!")
        exit()

#x = Symbol('x')
#findLambda(-x ** 2 - 8 * x)
