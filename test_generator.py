# nodes: 5 - 50.000
# edges: 5 - 200.000

# types:
# 	1. sparse E ~ V
# 	2. dense E ~ V ^ 2
# 	3. general E ~ V ^ 3/2
# 	4. general E ~ V log V

import random
import math

NODES_COUNT_MAX = 50000
EDGES_COUNT_MAX = 200000

def edges_from_nodes(nodes_count, type_index):
	if type_index == 1:
		return random.randint(int(0.5 * nodes_count), int(1.5 * nodes_count))
	elif type_index == 2:
		return random.randint(int(0.3 * nodes_count * nodes_count), int(0.7 * nodes_count * nodes_count))
	elif type_index == 3:
		return random.randint(int(0.5 * math.pow(nodes_count, 1.5)), int(1.5 * math.pow(nodes_count, 1.5)))
	else:
		return random.randint(int(0.5 * nodes_count * math.log2(nodes_count)), int(1.5 * nodes_count * math.log2(nodes_count)))


def generate_test(nodes_count, edges_count, file_name):
	nodes = [x for x in range(0, nodes_count)]
	random.shuffle(nodes)

	left_count = random.randint(int(0.4 * nodes_count), int(0.6 * nodes_count))
	left = [nodes[x] for x in range(0, left_count)]

	right_count = nodes_count - left_count
	right = [nodes[x] for x in range(left_count, nodes_count)]

	f = open(file_name, "w")
	f.write(str(nodes_count) + " " + str(edges_count) + "\n")
	
	for _ in range(0, edges_count):
		left_index = random.randint(0, left_count - 1)
		right_index = random.randint(0, right_count - 1)
		f.write(str(left[left_index]) + " " + str(right[right_index]) + "\n")

	f.close()


input_dimension = [5, 20, 50, 100, 250, 300, 350, 400, 500, 750, 800, 1000, 2000, 2500, 4000, 5000, 10000, 20000, 40000, 45000, 50000]

file_no = 1
for type_index in range(1, 5):
	for nodes_count in input_dimension:
		file_name = "test" + str(file_no) + ".in"
		edges_count = edges_from_nodes(nodes_count, type_index)
		if (edges_count > EDGES_COUNT_MAX):
			continue

		generate_test(nodes_count, edges_count, file_name)
		print(str(file_no) + ": " + str(type_index) + " " + str(nodes_count))
		file_no += 1

file_name = "test" + str(file_no) + ".in"
generate_test(NODES_COUNT_MAX, EDGES_COUNT_MAX, file_name)
