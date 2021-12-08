

input = open("test_input.txt")
input_lines = [line.strip() for line in input]
input.close()

horizontal_positions = [int(value) for value in input_lines[0].split(",")]

# calculate the median of the horizontal positions
horizontal_positions.sort()
horizontal_median = horizontal_positions[len(horizontal_positions) // 2]

# calculate the average of the horizontal positions
average_horizontal_positions = float(sum(horizontal_positions)) / float(len(horizontal_positions))
if average_horizontal_positions - int(average_horizontal_positions) > 0.6:
	average_horizontal_positions = int(average_horizontal_positions) + 1
else:
	average_horizontal_positions = int(average_horizontal_positions)

# calculate nessesary fule for median position
median_fuel_required = 0
for position in horizontal_positions:
	median_fuel_required += abs(position - horizontal_median)

average_fuel_required = 0
for position in horizontal_positions:
	# the required fuel increments for each step
	for step in range(1, int(abs(position - average_horizontal_positions) + 1)):
		average_fuel_required += step

print("The median horizontal position is {}" .format(horizontal_median))
print("The fuel required for this is {}" .format(median_fuel_required))
print("----------")
print("The average horizontal position is {}" .format(average_horizontal_positions))
print("The fuel required for this is {}" .format(average_fuel_required))
