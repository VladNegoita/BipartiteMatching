import os
import subprocess
from time import time
import numpy as np
from matplotlib import pyplot as plt

TEST_CNT = 63
algorithms = ["Hopcroft_Karp_Karzanov", "chains_optimised", "chains_simple", "Edmonds_Karp"]
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
		subprocess.run(["cp",  output_file,  "./out/"])

		subprocess.run(["rm", output_file])
		subprocess.run(["rm", "test.in"])

subprocess.run(["make",  "clean"])

print(repr(times))
plt.plot(times[0][:])
plt.show()
