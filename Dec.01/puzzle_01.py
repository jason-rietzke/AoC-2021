

input = open("input.txt")
lines = [int(line.strip()) for line in input]
input.close()

increase_count = 0
prev_value = 0

for value in lines:
	if prev_value > 0 and value > prev_value:
		increase_count += 1
	prev_value = value

print(increase_count)

