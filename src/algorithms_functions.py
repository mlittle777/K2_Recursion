# functions used by algorithms script
import time
import math
import sys
sys.setrecursionlimit(2000)

#function for calculating factorials iteratively
def iterative_factorial(n):
    factorial = 1
    for i in range(n, 1, -1):
        factorial *= n
        n -= 1
    return factorial

# function for calculating factorials recursively
def recursive_factorial(n):
    if n<= 1:
        return 1
    return n * recursive_factorial(n-1)

# function for capturing the elapsed time to calculate n! using one of three specified algorithm
# output is a dict with algorithm types as keys and times as values
def factorial_compare(n, algorithm_type):
    start_time = time.time()
    if algorithm_type == 'iterative':
        iterative_factorial(n)
    elif algorithm_type == 'recursive':
        recursive_factorial(n)
    else:
        math.factorial(n)
    return time.time() - start_time
