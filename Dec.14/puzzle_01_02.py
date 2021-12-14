import time


input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

polymer = input_lines[0]
pair_insertion_rules = {}
for line in input_lines[2:]:
	pair_insertion_rules[line.split(" -> ")[0]] = line.split(" -> ")[1]

total_depth = 40 # 10 for Part 1 and 40 for Part 2
elements = {}

print("{:,} calculations needed" .format(pow(2, total_depth)))

class Node:

	def __init__(self, pair):
		self.pair = pair
		self.parent = None
		self.depth = None
	
	def run(self):
		if self.depth >= total_depth:
			return

		element = pair_insertion_rules[self.pair]
		if element in elements:
			elements[element] += 1
		else:
			elements[element] = 1

		pair_1 = self.pair[0] + element
		child_1 = Node(pair_1)
		child_1.depth = self.depth + 1
		child_1.parent = self
		child_1.run()

		pair_2 = element + self.pair[1]
		child_2 = Node(pair_2)
		child_2.depth = self.depth + 1
		child_2.parent = self
		child_2.run()


for element in polymer:
	if element in elements:
			elements[element] += 1
	else:
		elements[element] = 1

global_timer = time.time()
length = len(polymer)
for i in range(length - 1):
	local_timer = time.time()
	pair = polymer[i:i+2]
	sub_path = 0
	node = Node(pair)
	node.depth = 0
	node.run()
	local_timer = time.time() - local_timer
	print("{} \t {}% \t {}s".format(polymer[i:i+2], round(100 * (i+2) / length, 2), round(local_timer, 2)))

global_timer = time.time() - global_timer
print("Total time needed: {}s".format(round(global_timer, 2)))

most_common_element = {
	"element": "",
	"count": 0
}
least_common_element = {
	"element": "",
	"count": 0
}
for element in elements:
	if elements[element] > most_common_element["count"]:
		most_common_element["element"] = element
		most_common_element["count"] = elements[element]
	if elements[element] < least_common_element["count"] or least_common_element["count"] == 0:
		least_common_element["element"] = element
		least_common_element["count"] = elements[element]

print("The most common element subtracted with the least common element is: {}" .format(most_common_element["count"] - least_common_element["count"]))
