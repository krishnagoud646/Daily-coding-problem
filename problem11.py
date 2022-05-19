import math
import os
import random
import re
import sys

memo_dict = {}  

def staircase(n, steps_list): 

    if n in memo_dict:
        return memo_dict[n]

    if n < 0:
        return 0
    if n == 0:
        memo_dict[n] =1
        return 1
    memo_dict[n] = 0
    for step in steps_list:
        memo_dict[n]+= staircase(n-step, steps_list)

    return memo_dict[n]

def stepPerms(n): 
    if n in memo_dict:
        return memo_dict[n]
    if n < 0:
        return 0
    if n == 0:
        memo_dict[n] = 1
        return 1

    memo_dict[n] = stepPerms(n-1) + stepPerms(n-2)
    return memo_dict[n]

if __name__ == '__main__':

    N = 4  
    step_list = [1, 3, 10]
    res = staircase(N, step_list)
    print(res)
