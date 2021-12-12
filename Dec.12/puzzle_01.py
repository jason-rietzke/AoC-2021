

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

	def add_node(self, node):
		if node.name in self.nodes: return
		self.nodes[node.name] = node

	def get_node(self, name):
		return self.nodes[name]

	def add_link(self, node1, node2):
		node1.add_link(node2)

	def get_paths(self):
		start = self.get_node("start")
		path = [start]
		self.trace_path(start, path)
		return self.paths

	def trace_path(self, node, path):
		if node.is_end: return self.paths.append(path)

		for link in node.linked:
			if link.is_start: continue
			if not link.large_cave and link in path: continue
			if link == path[-1]: continue
			new_path = path + [link]
			self.trace_path(link, new_path)

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

paths = graph.get_paths()

print(len(paths))

for path in paths:
	output = ""
	for node in path:
		output += node.name + ", "
	output = output[:-2]
	print(output)

print("There are {} paths through the cave system that visit small caves at most once." .format(len(paths)))

