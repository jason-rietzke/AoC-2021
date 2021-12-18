import time


input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

def scale_map(map, iterations):
	height = len(map)
	width = len(map[0])
	new_map = []
	for y in range(height):
		new_map.append([])
		for i in range(iterations):
			for x in range(width):
				new_value = map[y][x] + i if map[y][x] + i < 10 else map[y][x] + i - 9
				new_map[-1].append(new_value)
	for i in range(1, iterations):
		for y in range(height):
			new_map.append([])
			for x in range(len(new_map[y])):
				new_value = new_map[y][x] + i if new_map[y][x] + i < 10 else new_map[y][x] + i - 9
				new_map[-1].append(new_value)
	return new_map


# A* search
def a_star_search(map, source, target):
	open_set = [source]
	closed_set = []
	pathway = {}
	g_score = {source: 0}
	f_score = {source: manhattan_distance(source, target)}
	while len(open_set) > 0:
		current = min(open_set, key=lambda point: f_score[point])
		if current == target:
			return f_score[target]
		open_set.remove(current)
		closed_set.append(current)
		for neighbor in get_neighbors(map, current):
			if neighbor in closed_set:
				continue
			tentative_g_score = g_score[current] + map[neighbor[1]][neighbor[0]]
			if neighbor not in open_set:
				open_set.append(neighbor)
			elif tentative_g_score >= g_score[neighbor]:
				continue
			pathway[neighbor] = current
			g_score[neighbor] = tentative_g_score
			f_score[neighbor] = g_score[neighbor] + manhattan_distance(neighbor, target)
	return -1


def manhattan_distance(point1, point2):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def get_neighbors(map, point):
	neighbors = []
	if point[0] > 0:
		neighbors.append((point[0] - 1, point[1]))
	if point[0] < len(map[0]) - 1:
		neighbors.append((point[0] + 1, point[1]))
	if point[1] > 0:
		neighbors.append((point[0], point[1] - 1))
	if point[1] < len(map) - 1:
		neighbors.append((point[0], point[1] + 1))
	return neighbors


start_time = time.time()
map = [[int(x) for x in line] for line in input_lines]
source = (0, 0)
target = (len(map[0]) - 1, len(map) - 1)
risk = a_star_search(map, source, target)
print("Total risk: {}".format(risk))
print("elapsed time: " + str(time.time() - start_time))

start_time = time.time()
map = scale_map(map, 5)
source = (0, 0)
target = (len(map[0]) - 1, len(map) - 1)
risk = a_star_search(map, source, target)
print("Total risk on scaled map: {}".format(risk))
print("elapsed time: " + str(time.time() - start_time))
