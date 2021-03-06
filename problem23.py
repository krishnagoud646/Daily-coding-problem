"""Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, 
implement a function rand7() that returns an integer from 1 to 7 (inclusive)."""

import numpy as np

def rand5():
    return np.random.randint(1, 6)

def rand7():

    n1 = rand5()
    n2 = rand5()
    n = 5*(n1-1) + (n2-1) #n is a random number in [0, 24] range
    if n<=20:
        return n%7 + 1
    else:
        return rand7()

A = {}
for _ in range(100000):
    n = rand7()
    if n in A:
        A[n]+=1
    else:
        A[n]=1
print(A)
