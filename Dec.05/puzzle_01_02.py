

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

vector_lines = []
for line in input_lines:
	start_x = int(line.split(" -> ")[0].split(",")[0])
	start_y = int(line.split(" -> ")[0].split(",")[1])
	end_x = int(line.split(" -> ")[1].split(",")[0])
	end_y = int(line.split(" -> ")[1].split(",")[1])
	vector_lines.append({
		"x1": start_x,
		"y1": start_y,
		"x2": end_x,
		"y2": end_y
	})

# filter for horizontal and vertical lines (and diagonal lines)
hv_vector_lines = [line for line in vector_lines if line["x1"] == line["x2"] or line["y1"] == line["y2"]]
hvd_vector_lines = [line for line in vector_lines if line["x1"] == line["x2"] or line["y1"] == line["y2"] or (line["x1"] - line["x2"]) == (line["y1"] - line["y2"]) or (line["x1"] - line["x2"]) == (line["y2"] - line["y1"])]


# build the vent map
maxWidth = max(max([line["x1"] for line in vector_lines]) + 1, max([line["x2"] for line in vector_lines]) + 1)
maxHeight = max(max([line["y1"] for line in vector_lines]) + 1, max([line["y2"] for line in vector_lines]) + 1)
hv_vent_map = [[0 for x in range(maxWidth)] for y in range(maxHeight)]
hvd_vent_map = [[0 for x in range(maxWidth)] for y in range(maxHeight)]


def interpolate_and_fill_points(vector, map):
	x_start = vector["x1"]
	y_start = vector["y1"]
	x_end = vector["x2"]
	y_end = vector["y2"]

	# horizontal line
	if x_start == x_end:
		for y in range(min(y_start, y_end), max(y_start, y_end) + 1):
			map[y][x_start] += 1

	# vetical line
	elif y_start == y_end:
		for x in range(min(x_start, x_end), max(x_start, x_end) + 1):
			map[y_start][x] += 1

	# diagonal line
	else:
		x_step = 1 if x_start < x_end else -1
		y_step = 1 if y_start < y_end else -1
		x = x_start
		y = y_start
		while x != x_end or y != y_end:
			map[y][x] += 1
			x += x_step
			y += y_step
		map[y][x] += 1


for line in hv_vector_lines:
	interpolate_and_fill_points(line, hv_vent_map)

for line in hvd_vector_lines:
	interpolate_and_fill_points(line, hvd_vent_map)


hv_points = 0
for line in hv_vent_map:
	for x in line:
		if x >= 2:
			hv_points += 1

hvd_points = 0
for line in hvd_vent_map:
	for x in line:
		if x >= 2:
			hvd_points += 1


print("{} points have at least two lines overlapping in the horizontal and vertical assumtion" .format(hv_points))
print("{} points have at least two lines overlapping in the horizontal, vertical and diagonal assumtion" .format(hvd_points))
