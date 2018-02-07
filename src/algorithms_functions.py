"""Implement functions used by algorithms_working.py"""
import time
import math
import sys
sys.setrecursionlimit(2000)

# FACTORIAL FUNCTIONS

def iterative_factorial(n):
    """Calculate factorial iteratively."""
    factorial = 1
    for i in range(n, 1, -1):
        factorial *= n
        n -= 1
    return factorial


def recursive_factorial(n):
    """Calculate factorial recursively."""
    if n<= 1:
        return 1
    return n * recursive_factorial(n-1)


def factorial_compare(n, algorithm_type):
"""Capture time to calculate a factorial using a specified algorithm."""
    start_time = time.time()
    if algorithm_type == 'iterative':
        iterative_factorial(n)
    elif algorithm_type == 'recursive':
        recursive_factorial(n)
    else:
        math.factorial(n)
    return time.time() - start_time



# FIBONACCI FUNCTIONS

def fibonacci_start(n, start):
    """Return first or second term of Fibonacci series.

    Invoked only if n < 3. Arg start enables option to start series with 0 (historical definition) or with 1 (modern practice) as the first term.
    """
    modern_start = [0, 1]
    historical_start = [1, 1]
    if start == 0:
        return modern_start[n - 1]
    elif start == 1:
        return historical_start[n - 1]


def iterative_fibonacci(n, start):
    """Calculate nth term of Fibonacci series iteratively."""
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


def recursive_fibonacci(n, start):
    """Calculate nth term of Fibonacci series recursively."""
    if n < 3:
        return fibonacci_start(n, start)
    else:
        return recursive_fibonacci(n-1, start) + recursive_fibonacci(n-2, start)


def fibonacci_compare(n, start, algorithm_type):
    """Capture time to calculate nth Fibo term using a specified algorithm."""
    start_time = time.time()
    if algorithm_type == 'iterative':
        iterative_fibonacci(n, start)
    elif algorithm_type == 'recursive':
        recursive_fibonacci(n, start)
    return time.time() - start_time
