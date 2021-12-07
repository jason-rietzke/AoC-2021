

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

# filter for horizontal and vertical lines
vector_lines = [line for line in vector_lines if line["x1"] == line["x2"] or line["y1"] == line["y2"]]


# build the vent map
maxWidth = max(max([line["x1"] for line in vector_lines]) + 1, max([line["x2"] for line in vector_lines]) + 1)
maxHeight = max(max([line["y1"] for line in vector_lines]) + 1, max([line["y2"] for line in vector_lines]) + 1)
vent_map = [[0 for x in range(maxWidth)] for y in range(maxHeight)]

for line in vector_lines:
	if line["x1"] == line["x2"]:
		for y in range(min(line["y1"], line["y2"]), max(line["y1"], line["y2"]) + 1):
			vent_map[y][line["x1"]] += 1

	if line["y1"] == line["y2"]:
		for x in range(min(line["x1"], line["x2"]), max(line["x1"], line["x2"]) + 1):
			vent_map[line["y1"]][x] += 1


points = 0
for line in vent_map:
	for x in line:
		if x >= 2:
			points += 1

print("{} points have at least two lines overlapping" .format(points))
