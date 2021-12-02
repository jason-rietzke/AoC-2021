

input = open("input.txt")
lines = [line.strip() for line in input]
input.close()

position = {
	"horizontal": 0,
	"depth": 0,
	"aim": 0
}

for line in lines:
	value = int(line.split(" ")[1])
	if line.startswith("forward"):
		position["horizontal"] += value
		position["depth"] += (position["aim"] * value)
	elif line.startswith("up"):
		position["aim"] -= value
	elif line.startswith("down"):
		position["aim"] += value

print(position)

result = int(position["horizontal"]) * abs(position["depth"])
print("result: " + str(result))

