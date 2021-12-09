

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()


def find_lowpoint(line):
	lowpoints = []
	for i in range(len(line)):
		if i == 0 and line[i] < line[i+1]:
			lowpoints.append(i)
		elif i == len(line)-1 and line[i] < line[i-1]:
			lowpoints.append(i)
		elif line[i] < line[i-1] and line[i] < line[i+1]:
			lowpoints.append(i)
	return lowpoints


# check horizontal lines
lowpoint_map = [[0 for i in range(len(input_lines[0]))] for j in range(len(input_lines))]
for line in input_lines:
	lowpoints = find_lowpoint(line)
	for lowpoint in lowpoints:
		lowpoint_map[input_lines.index(line)][lowpoint] += 1

# check vertical lines
for i in range(len(input_lines[0])):
	lowpoints = find_lowpoint([line[i] for line in input_lines])
	for lowpoint in lowpoints:
		lowpoint_map[lowpoint][i] += 1

# print lowpoint_map
for row in lowpoint_map:
	row_str = ""
	for col in row:
		row_str += "X" if col == 2 else "."
	print(row_str)


lowpoints = []
for i in range(len(input_lines)):
	for j in range(len(input_lines[0])):
		if lowpoint_map[i][j] == 2:
			lowpoints.append(int(input_lines[i][j]))

risk_level = sum([lowpoint + 1 for lowpoint in lowpoints])
print("Risk level:", risk_level)

