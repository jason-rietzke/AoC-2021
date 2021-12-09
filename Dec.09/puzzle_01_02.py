

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


def detect_basin(map, basin, point):
	# check if point["x" and "y"] is in basins (objects also with same x and y)
	x = point["x"]
	y = point["y"]
	if int(map[y][x]) < 9:
		for basin_point in basin:
			if basin_point["x"] == x and basin_point["y"] == y:
				return

		basin.append({
			"x": point["x"],
			"y": point["y"],
		})

		if x > 0:
			detect_basin(map, basin, {"x": x-1, "y": y})
		if x < len(map[0])-1:
			detect_basin(map, basin, {"x": x+1, "y": y})
		if y > 0:
			detect_basin(map, basin, {"x": x, "y": y-1})
		if y < len(map)-1:
			detect_basin(map, basin, {"x": x, "y": y+1})


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

# detect basins
basins = []
for y in range(len(input_lines)):
	for x in range(len(input_lines[0])):
		if lowpoint_map[y][x] == 2:
			basin = []
			detect_basin(input_lines, basin, {"x": x, "y": y})
			basins.append(len(basin))


# extract lowpoints
lowpoints = []
for y in range(len(input_lines)):
	for x in range(len(input_lines[0])):
		if lowpoint_map[y][x] == 2:
			lowpoints.append(int(input_lines[y][x]))

# print lowpoint_map
for y in range(len(lowpoint_map)):
	row = lowpoint_map[y]
	row_str = ""
	for x in range(len(row)):
		col = row[x]
		row_str += "*" if col == 2 else input_lines[y][x]
	print(row_str)

risk_level = sum([lowpoint + 1 for lowpoint in lowpoints])
print("Risk level {}" .format(risk_level))

# get 3 largest basins
basins.sort(reverse=True)
print("3 Largest basins: {}" .format(basins[:3]))
print("They have a total size of {}" .format(basins[0] * basins[1] * basins[2]))
