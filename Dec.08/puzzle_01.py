

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

inputs = [line.split(" | ")[0].split(" ") for line in input_lines]
outputs = [line.split(" | ")[1].split(" ") for line in input_lines]

unique_digits = 0
for output in outputs:
	for digit in output:
		# check for digit 1 (2), 4 (4), 7 (3) and 8 (7) 
		l = len(digit)
		if (l is 2) or (l is 4) or (l is 3) or (l is 7):
			unique_digits += 1

print("There are {} unique digits in the output (1, 4, 7 or 8)" .format(unique_digits))

