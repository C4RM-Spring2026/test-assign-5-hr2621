import numpy as np

def FizzBuzz(start, finish):

    numvec = np.arange(start, finish + 1)
    objvec = np.array(numvec, dtype=object)

    mask15 = (numvec % 15 == 0)
    mask3 = (numvec % 3 == 0) & (~mask15)
    mask5 = (numvec % 5 == 0) & (~mask15)

    objvec[mask15] = "fizzbuzz"
    objvec[mask3] = "fizz"
    objvec[mask5] = "buzz"

    return objvec