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

# original Fibonacci definition historicallly starts with 1, 1, but more modern usage starts with 0, 1
def fibonacci_start(n, start):
    modern_start = [0, 1]
    historical_start = [1, 1]
    if start == 0:
        return modern_start[n - 1]
    elif start == 1:
        return historical_start[n - 1]

# function for calculating nth Fibonacci term iteratively
def iterative_fibonacci(n, start):
    if n < 3:
        return fibonacci_start(n, start)
    else:
        last_term = 1
        previous_term = start
        for i in range(3, n+1):
            next_term = last_term + previous_term
            previous_term = last_term
            last_term = next_term
        return last_term

# function for calculating nth Fibonacci term recursively
def recursive_fibonacci(n, start):
    if n < 3:
        return fibonacci_start(n, start)
    else:
        return recursive_fibonacci(n-1, start) + recursive_fibonacci(n-2, start)

def fibonacci_compare(n, start, algorithm_type):
    start_time = time.time()
    if algorithm_type == 'iterative':
        iterative_fibonacci(n, start)
    elif algorithm_type == 'recursive':
        recursive_fibonacci(n, start)
    return time.time() - start_time
