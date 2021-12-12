

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()


class Node:
	def __init__(self, name):
		self.name = name
		self.linked = []
		self.large_cave = True if name.isupper() else False
		self.is_start = True if name == "start" else False
		self.is_end = True if name == "end" else False

	def add_link(self, node):
		if node not in self.linked:
			self.linked.append(node)
		if self not in node.linked:
			node.linked.append(self)


class Graph:
	def __init__(self):
		self.nodes = {}
		self.paths = []
		self.trace_step = 0

	def add_node(self, node):
		if node.name in self.nodes: return
		self.nodes[node.name] = node

	def get_node(self, name):
		return self.nodes[name]

	def add_link(self, node1, node2):
		node1.add_link(node2)

	def get_paths(self, small_cave_max):
		self.paths = []
		start = self.get_node("start")
		path = [start]
		self.trace_path(start, path, small_cave_max)
		return self.paths

	def trace_path(self, node, path, small_cave_max):
		if node.is_end: return self.paths.append(path)

		self.trace_step += 1
		print("Trace step: {:,}" .format(self.trace_step))

		for link in node.linked:
			if link.is_start: continue
			if not link.large_cave:
				small_caves = [n for n in path if not n.large_cave]
				exit_loop = False
				for small_cave in small_caves:
					count = small_caves.count(small_cave)
					if count > small_cave_max: exit_loop = True
				if exit_loop: continue

				small_caved = [n for n in path if not n.large_cave and n.name != "start" and n.name != "end"]
				small_caved.sort(key=lambda x: x.name)
				caves = {}
				for cave in small_caved:
					caves[cave.name] = caves[cave.name] + 1 if cave.name in caves else 1
				number_of_second_visits = 0
				for cave in caves:
					if caves[cave] == 2: number_of_second_visits += 1

				if number_of_second_visits > 1: continue

			if link == path[-1]: continue
			new_path = path + [link]
			self.trace_path(link, new_path, small_cave_max)

	def print_graph(self):
		for node in self.nodes.values():
			output = node.name + " -> "
			for link in node.linked:
				output += link.name + ", "
			print(output)


graph = Graph()

for line in input_lines:
	node1 = line.split("-")[0].strip()
	node2 = line.split("-")[1].strip()

	graph.add_node(Node(node1))
	graph.add_node(Node(node2))
	graph.add_link(graph.get_node(node1), graph.get_node(node2))

paths_1 = graph.get_paths(1)
paths_2 = graph.get_paths(2)

print("There are {} paths through the cave system that visit small caves at most once." .format(len(paths_1)))
print("There are {} paths through the cave system that visits one small caves at most twice." .format(len(paths_2)))
