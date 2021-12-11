

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

map = []
for y in range(len(input_lines)):
	map.append([])
	for x in range(len(input_lines[y])):
		map[y].append(int(input_lines[y][x]))


flash_count = 0

for i in range(100):
	flash_map = []

	# increase energy by 1
	for y in range(len(map)):
		for x in range(len(map[y])):
			if map[y][x] <= 9:
				map[y][x] += 1
			if map[y][x] > 9:
				flash_map.append([x, y])
	
	# increment energy based on neighborhood
	for flash in flash_map:
		new_flash_map = []
		x = flash[0]
		y = flash[1]
		# vertical flash
		if y > 0 and map[y-1][x] <= 9:
			map[y-1][x] += 1
			if map[y-1][x] > 9: new_flash_map.append([x, y-1])
		if y < len(map)-1 and map[y+1][x] <= 9:
			map[y+1][x] += 1
			if map[y+1][x] > 9: new_flash_map.append([x, y+1])
		# horizontal flash
		if x > 0 and map[y][x-1] <= 9:
			map[y][x-1] += 1
			if map[y][x-1] > 9: new_flash_map.append([x-1, y])
		if x < len(map[y])-1 and map[y][x+1] <= 9:
			map[y][x+1] += 1
			if map[y][x+1] > 9: new_flash_map.append([x+1, y])
		# diagonal flash
		if x > 0 and y > 0 and map[y-1][x-1] <= 9:
			map[y-1][x-1] += 1
			if map[y-1][x-1] > 9: new_flash_map.append([x-1, y-1])
		if x < len(map[y])-1 and y < len(map)-1 and map[y+1][x+1] <= 9:
			map[y+1][x+1] += 1
			if map[y+1][x+1] > 9: new_flash_map.append([x+1, y+1])
		if x > 0 and y < len(map)-1 and map[y+1][x-1] <= 9:
			map[y+1][x-1] += 1
			if map[y+1][x-1] > 9: new_flash_map.append([x-1, y+1])
		if x < len(map[y])-1 and y > 0 and map[y-1][x+1] <= 9:
			map[y-1][x+1] += 1
			if map[y-1][x+1] > 9: new_flash_map.append([x+1, y-1])
		flash_map += new_flash_map

	# flash and adjust energy levels
	for y in range(len(map)):
		for x in range(len(map[y])):
			if map[y][x] > 9:
				map[y][x] = 0
				flash_count += 1


	# print energy map
	for row in map:
		print(row)
	print("----------")

print("There where {} flashes" .format(flash_count))
