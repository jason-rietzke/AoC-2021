

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

coordinates = []
fold_instructions = []

def remove_duplicates(coordinates):
	coordinates_no_duplicates = []
	for coordinate in coordinates:
		if coordinate not in coordinates_no_duplicates:
			coordinates_no_duplicates.append(coordinate)
	return coordinates_no_duplicates

def print_map():
	for y in range(paper_height + 1):
		line = ""
		for x in range(paper_width + 1):
			for coordinate in coordinates:
				if coordinate["x"] == x and coordinate["y"] == y:
					line += "#"
					break
			else:
				line += "."
		print(line)

for line in input_lines:
	if line is "": continue
	if line[0] is "f":
		# fold instruction
		instruction = line[11:].split("=")
		fold_instructions.append({
			"axis": instruction[0],
			"position": int(instruction[1])
		})
	else:
		# coordinates
		x = line.split(",")[0]
		y = line.split(",")[1]
		coordinates.append({
			"x": int(x),
			"y": int(y)
		})

paper_width = max([coordinates[i]["x"] for i in range(len(coordinates))])
paper_height = max([coordinates[i]["y"] for i in range(len(coordinates))])

coordinates.sort()

for instruction in fold_instructions:
	if instruction["axis"] is "y":
		for coordinate in coordinates:
			if coordinate["y"] > instruction["position"]:
				new_y = paper_height - coordinate["y"]
				if new_y < 0: 
					coordinates.remove(coordinate)
					continue
				coordinate["y"] = new_y
	else:
		for coordinate in coordinates:
			if coordinate["x"] > instruction["position"]:
				new_x = paper_width - coordinate["x"]
				if new_x < 0: 
					coordinates.remove(coordinate)
					continue
				coordinate["x"] = new_x

	paper_width = max([coordinates[i]["x"] for i in range(len(coordinates))])
	paper_height = max([coordinates[i]["y"] for i in range(len(coordinates))])

	coordinates = remove_duplicates(coordinates)
	if instruction == fold_instructions[0]:
		print("There are {} dots visible after the first fold" .format(len(coordinates)))

