import time
import math
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline

# comparision of the time required for each alternative to run
def iterative_factorial(n):
    factorial = 1
    for i in range(n, 1, -1): # this sets range from the factorial (i.e. 5!) down to 1
        factorial *= n        # factorial is the variable the accumulates the product each loop
        n -= 1
    return factorial

def recursive_factorial(n):
    if n<= 1:                 # exit out of the loop once we get down to 1
        return 1
    return n * recursive_factorial(n-1) # core of the recursion

def factorial_compare(n):
    n_points.append(n) # build list of n for plot

    start_time_i = time.time() # start timestamp
    iterative_factorial(n)   # iterative case
    delta_t = time.time() - start_time_i  # elapsed time
    inter.append(delta_t)  # build list of results for plot

    start_time_r = time.time()
    recursive_factorial(n)  # recursive case
    delta_t = time.time() - start_time_r
    recur.append(delta_t)  # build list of results for plot

    start_time_p = time.time()
    math.factorial(n)      # added in the python built-in to show how optimzed it is, as results below show!
    delta_t = time.time() - start_time_p
    pyth.append(delta_t)  # build list of results for plot

# empty lists to collect data for plotting
n_points = []
inter = []
recur = []
pyth = []

for n in range(50, 2000, 50):
    factorial_compare(n)

n_points
#print(inter)
#print(recur)
pyth

plt.plot(n_points, inter, label="Iterative")
plt.plot(n_points, recur, label="Recursive")
plt.plot(n_points, pyth, label="math.factorial(n)")
plt.ylim(ymin=0, ymax=0.0050)
plt.legend()
plt.title("Time to Calculate n!")
plt.show();





import time
import math
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(2000)


# comparision of the time required for each alternative to run

# iterative implementation, takes number of terms and option to start with 0, 1 or 1, 1
# original defintion historicallly starts with 1, 1, but more modern usage starts with 0, 1, default is 0, 1
# 0 uses 0, 1; 1 uses 1, 1
def iterative_fibonacci(n):

    if start == 0:                     # if requesting modern fibonacci (0,1,1,2,3,5...)
        last = 1                       # most recently calculated term, here it is F1
        pen = 0                        # prior term (penultimate), here F0
        for i in range(start+3,n+1):
            next = last + pen
            pen = last
            last = next
        return next

    elif start == 1:                   # if requesting modern fibonacci (0,1,1,2,3,5...)
        last = 1                       # most recently calculated term, here it is F2
        pen = 1                        # prior term (penultimate), here F1
        for i in range(start+2,n+1):
            next = last + pen
            pen = last
            last = next
        return next

def recursive_fibonacci(n):
    f_n = 0

    if start == 0:                     # if requesting modern fibonacci (0,1,1,2,3,5...)
        if n <=3:
            f_n = f_n + 1 + 0
            return f_n
        f_n = recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
        return f_n

    elif start == 1:                   # if requesting modern fibonacci (0,1,1,2,3,5...)
        if n <=2:
            f_n = f_n + 1 + 0
            return f_n
        f_n = recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
        return f_n

def fibonacci_compare(n):
    n_points.append(n) # build list of n for plot

    start_time_i = time.time() # start timestamp
    next = iterative_fibonacci(n)   # iterative case
    delta_t = time.time() - start_time_i  # elapsed time
    print('iter', n, next)
    inter.append(delta_t)  # build list of results for plot

    start_time_r = time.time()
    f_n = recursive_fibonacci(n)  # recursive case
    delta_t = time.time() - start_time_r
    print('recur', n, f_n)
    recur.append(delta_t)  # build list of results for plot

start = -1
while (start + 1 != 1) and (start + 1 != 2):
    start = int(input("Do you want to start the series with 0 or 1? "))

# empty lists to collect data for plotting
n_points = []
inter = []
recur = []

for n in range(3, 43, 5):
    fibonacci_compare(n)

plt.plot(n_points, inter, label="Iterative")
plt.plot(n_points, recur, label="Recursive")
plt.ylim(ymin=0, ymax=0.01)
plt.legend()
plt.title("Time to Calculate nth Fibonacci")
plt.show();
