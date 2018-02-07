# This script calculates the times need for various algorithms used
# for finding factorials and Fibonocci Series terms. It makes use
# of a module called algorithms_functions, which contains defined functions
# used in the script


import algorithms_functions #custom module with functions for algorithms
import matplotlib.pyplot as plt

# FACTORIAL
# collect the calculation times for each of three factorial algorithm types
algorithm_types = ['iterative', 'recursive', 'math']
time_dict = {k: [] for k in algorithm_types}
n_points = list(range(50, 2000, 50))

for n in n_points:
    for algorithm_type in algorithm_types:
        time_elapsed = algorithms_functions.factorial_compare(n, algorithm_type)
        time_dict[algorithm_type].append(time_elapsed)

# plot calculation time vs n for each factorial algorithm type
plt.figure(figsize=(15, 10))
for k, v in time_dict.items():
    plt.plot(n_points, v, label=k)

plt.ylim(ymin=0, ymax=0.003)
plt.legend()
plt.title("Time to Calculate n!")
plt.savefig("factorial_times.png", transparent=False)




# FIBONACCI
# collect the calculation times for two Fibonacci algorithm types
algorithm_types = ['iterative', 'recursive']
time_dict = {k: [] for k in algorithm_types}
n_points = list(range(1, 31, 1))

start = -1
while (start + 1 != 1) and (start + 1 != 2):
    start = int(input("Do you want to start the series with 0 or 1? "))

for n in n_points:
    for algorithm_type in algorithm_types:
        time_elapsed = algorithms_functions.fibonacci_compare(n, start, algorithm_type)
        time_dict[algorithm_type].append(time_elapsed)

# plot calculation time vs n for each factorial algorithm type
f, axes = plt.subplots(2, sharex=True, figsize=(15,10))
for k, v in time_dict.items():
    axis_index = algorithm_types.index(k)
    axes[axis_index].plot(n_points, v, label=k)
    axes[axis_index].set_ylabel('Seconds')
    axes[axis_index].legend()

axes[1].set_xlabel('Number of iterations')
f.suptitle('Time to Calculate nth Fibonacci Term')
plt.savefig("fibonacci_times.png", transparent=False)
