

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

polymer = input_lines[0]
pair_insertion_rules = {}
for line in input_lines[2:]:
    pair_insertion_rules[line.split(" -> ")[0]] = line.split(" -> ")[1]

elements = {}
for element in pair_insertion_rules:
    elements[element] = 0

elements_count = {}
for element in pair_insertion_rules:
    for char in pair_insertion_rules[element]:
        elements_count[char] = 0

for element in polymer:
    elements_count[element] += 1

# load initial polymer in elements
for i in range(0, len(polymer) - 1):
    element_pair = polymer[i:i+2]
    elements[element_pair] += 1

for i in range(40):  # 10 iterations for part 1 and 40 for part 2
    current_elements = elements.copy()
    for element in current_elements:
        elements[element] -= current_elements[element]
        new_element = pair_insertion_rules[element]
        elements_count[new_element] += current_elements[element]
        elements[element[0] + new_element] += current_elements[element]
        elements[new_element + element[1]] += current_elements[element]
    print(i)

max_count = -1
min_count = -1
for element in elements_count:
    if elements_count[element] > max_count:
        max_count = elements_count[element]
    if elements_count[element] < min_count or min_count == -1:
        min_count = elements_count[element]

print("The most common element subtracted with the least common element is: {}" . format(
    max_count - min_count))
