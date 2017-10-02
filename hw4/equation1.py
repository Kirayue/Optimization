import numpy as np
def f(F):
    A = np.array([11.5, 92.5, 44.3, 98.1, 20.1, 6.1, 45.5, 31, 44.3])
    #A = np.array([1, 2, 3, 4])
    return np.sum((F/A) ** 2) #+ np.sum((F/A) ** 3)

#print(f(np.array([1,2,9,4])))

