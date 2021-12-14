

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

polymer = input_lines[0]
pair_insertion_rules = {}
for line in input_lines[2:]:
	pair_insertion_rules[line.split(" -> ")[0]] = line.split(" -> ")[1]

iterations = 40 # 10 for Part 1 and 40 for Part 2

for i in range(iterations):
	print("Iteration: {}" .format(i + 1))
	print("Polymer length: {:,}" .format(len(polymer)))
	j = 0
	while j < len(polymer) - 1:
		pair = polymer[j:j+2]
		polymer = polymer[:j + 1] + pair_insertion_rules[pair] + polymer[j + 1:]
		j += 2

element_counts = {}
for element in polymer:
	if element in element_counts:
		element_counts[element] += 1
	else:
		element_counts[element] = 1

most_common_element = {
	"element": "",
	"count": 0
}
least_common_element = {
	"element": "",
	"count": 0
}
for element in element_counts:
	if element_counts[element] > most_common_element["count"]:
		most_common_element["element"] = element
		most_common_element["count"] = element_counts[element]
	if element_counts[element] < least_common_element["count"] or least_common_element["count"] == 0:
		least_common_element["element"] = element
		least_common_element["count"] = element_counts[element]

print("The most common element subtracted with the least common element is: {}" .format(most_common_element["count"] - least_common_element["count"]))

