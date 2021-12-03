

input = open("input.txt")
lines = [int(line.strip()) for line in input]
input.close()

increase_count = 0
prev_sum = 0

for i in range(len(lines)):
	sum = lines[i]
	if prev_sum > 0 and len(lines) > i + 2:
		sum = lines[i] + lines[i + 1] + lines[i + 2]
		if sum > prev_sum:
			increase_count += 1
	prev_sum = sum

print(increase_count)

