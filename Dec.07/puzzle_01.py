

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

horizontal_positions = [int(value) for value in input_lines[0].split(",")]

# calculate the median of the horizontal positions
horizontal_positions.sort()
horizontal_median = horizontal_positions[len(horizontal_positions) // 2]

# calculate nessesary fule
fuel_required = 0
for position in horizontal_positions:
	fuel_required += abs(position - horizontal_median)

print("The average horizontal position is:", horizontal_median)
print("The fuel required is:", fuel_required)
