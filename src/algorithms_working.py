import algorithms_functions #custom module
import matplotlib.pyplot as plt

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
