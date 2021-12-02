

input = open("input.txt")
lines = [line.strip() for line in input]
input.close()

position = {
	"horizontal": 0,
	"depth": 0
}

for line in lines:
	value = int(line.split(" ")[1])
	if line.startswith("forward"):
		position["horizontal"] += value
	elif line.startswith("up"):
		position["depth"] -= value
	elif line.startswith("down"):
		position["depth"] += value

print(position)

result = int(position["horizontal"]) * abs(position["depth"])
print("result: " + str(result))

