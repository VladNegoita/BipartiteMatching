import subprocess
from time import time
import numpy as np
from matplotlib import pyplot as plt

TEST_CNT = 62
algorithms = ["Hopcroft_Karp_Karzanov", "chains_optimised", "chains_simple" , "Edmonds_Karp"]
times = np.zeros([4, 1 + TEST_CNT])

subprocess.run(["make"])

for i, algo in enumerate(algorithms):
	for file_index in range(1, TEST_CNT + 1):
		input_file = "test" + str(file_index) + ".in"
		output_file = "test" + str(file_index) + ".out"

		subprocess.run(["cp", f"in/{input_file}", "."])
		subprocess.run(["mv", input_file, "test.in"])

		start = time()
		subprocess.run(f"./{algo}")
		finish = time()

		times[i][file_index] = finish - start

		subprocess.run(["mv", "test.out",  output_file])
		subprocess.run(["mv",  output_file,  "./out/"])

subprocess.run(["make",  "clean"])

# tests distribution
# 1 - 21 sparse E ~ V
# 22 - 30 dense E ~ V ^ 2
# 31 - 44 E ~ V ^ 3/2
# 45 - 62 E ~ V log V

nodes = [0, 5, 20, 50, 100, 250, 300, 350, 400, 500, 750, 800, 1000, 2000, 2500, 4000, 5000, 10000, 20000, 40000, 45000, 50000]

# sparse graph
plt.plot(nodes[:22], times[0][:22], c="r", label=algorithms[0])
plt.plot(nodes[:22], times[1][:22], c="g", label=algorithms[1])
plt.plot(nodes[:22], times[2][:22], c="b", label=algorithms[2])
plt.plot(nodes[:22], times[3][:22], c="y", label=algorithms[3])
plt.xlabel("nodes")
plt.ylabel("time(s)")
plt.title("Sparse Graph")
plt.legend()
plt.show()

# dense graph
plt.plot(nodes[1:10], times[0][22:31], c="r", label=algorithms[0])
plt.plot(nodes[1:10], times[1][22:31], c="g", label=algorithms[1])
plt.plot(nodes[1:10], times[2][22:31], c="b", label=algorithms[2])
plt.plot(nodes[1:10], times[3][22:31], c="y", label=algorithms[3])
plt.xlabel("nodes")
plt.ylabel("time(s)")
plt.title("Dense Graph")
plt.legend()
plt.show()

# less dense graph
plt.plot(nodes[1:15], times[0][31:45], c="r", label=algorithms[0])
plt.plot(nodes[1:15], times[1][31:45], c="g", label=algorithms[1])
plt.plot(nodes[1:15], times[2][31:45], c="b", label=algorithms[2])
plt.plot(nodes[1:15], times[3][31:45], c="y", label=algorithms[3])
plt.xlabel("nodes")
plt.ylabel("time(s)")
plt.title("E ~ V * sqrt(V) Graph")
plt.legend()
plt.show()

# log-sparse graph
plt.plot(nodes[1:19], times[0][45:63], c="r", label=algorithms[0])
plt.plot(nodes[1:19], times[1][45:63], c="g", label=algorithms[1])
plt.plot(nodes[1:19], times[2][45:63], c="b", label=algorithms[2])
plt.plot(nodes[1:19], times[3][45:63], c="y", label=algorithms[3])
plt.xlabel("nodes")
plt.ylabel("time(s)")
plt.title("E ~ V * log(V) Graph")
plt.legend()
plt.show()
