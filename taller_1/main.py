import numpy as np
from numpy.lib.function_base import average

if __name__ == '__main__':
    #Exercise 1
    a = np.array([2, 3, 5, 1, 4 ,7, 9, 8, 6, 10])
    print("Exercise 1", a)

    #Exercise 2
    b = np.array([])
    for i in range(11, 20):
        b = np.append(b, [i,])
    
    print("Exercise 2", b)

    #Exercise 3
    c = np.concatenate((a,b), axis=0)
    print("Exercise 3", c)

    #Exercise 4
    print("Exercise 4", np.amin(c))

    #Exercise 5
    print("Exercise 5", np.max(c))

    #Exercise 6
    print("Exercise 6", np.size(c))

    #Exercise 7
    print("Exercise 7", np.sum(c))

    #Exercise 8
    average = 0
    for i in np.nditer(c):
        average += i
    
    average /= np.size(c)

    print("Exercise 8", average)

    #Exercise 9
    print("Exercise 9", np.mean(c))

    #Exercise 12
    d = c[c>5]
    print("Exercise 12", d)

    #Exercise 13
    e = c[(c>5)&(c<15)]
    print("Exercise 13", e)

    #Exercise 14
    c[5] = 7
    c[15] = 7
    print("Exercise 14", c)

    #Exercise 15
    print("Exercise 15", np.sort(c))

    #Exercise 16
    c = c * 10
    print("Exercise 16", c)

    #Exercise 17
    index = [6,7,8]
    news = [60, 70, 80]
    c.put(index, news)
    print("Exercise 17", c)

    #Exercise 18
    index = np.array([14,15,16])
    news = index * 10
    c.put(index, news)
    print("Exercise 18", c)