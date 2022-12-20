import subprocess
from time import time
import numpy as np
from matplotlib import pyplot as plt

TEST_CNT = 62
algorithms = ["Hopcroft_Karp_Karzanov", "chains_optimised", "chains_simple" , "Edmonds_Karp"]
checker = "check"
matching_size = np.zeros([1 + TEST_CNT])

subprocess.run(["make"])

for i, algo in enumerate(algorithms):
	for file_index in range(1, TEST_CNT + 1):

		if (i == 3 and file_index >= TEST_CNT - 2):
			continue

		input_file = "test" + str(file_index) + ".in"
		output_file = "test" + str(file_index) + ".out"

		subprocess.run(["cp", f"in/{input_file}", "."])
		subprocess.run(["mv", input_file, "test.in"])

		subprocess.run(f"./{algo}")
		subprocess.run(f"./{checker}")

		f = open("test.out", "r")
		line = f.readline()

		if matching_size[file_index] == 0:
			matching_size[file_index] = int(line)
		elif matching_size[file_index] != int(line):
			print(f"Found different matching sizes {algo}: {matching_size[file_index]}, {int(line)}")

		subprocess.run(["mv", "test.out",  output_file])
		subprocess.run(["mv",  output_file,  "./out/"])

subprocess.run(["make",  "clean"])
