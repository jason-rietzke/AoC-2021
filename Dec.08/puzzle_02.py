

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

inputs = [line.split(" | ")[0].split(" ") for line in input_lines]
outputs = [line.split(" | ")[1].split(" ") for line in input_lines]

# analyze digit pattern of line (using inputs and considering the explicit numbers 1, 4, 7 and 8)
def analyze_pattern(inputs):
	pattern = ["" for i in range(10)]

	sixLetterDigits = []
	fiveLetterDigits = []

	# parse known digits
	for i in range(len(inputs)):
		if len(inputs[i]) == 2:		# 1
			pattern[1] = inputs[i][:]
		elif len(inputs[i]) == 4:	# 4
			pattern[4] = inputs[i][:]
		elif len(inputs[i]) == 3:	# 7
			pattern[7] = inputs[i][:]
		elif len(inputs[i]) == 7:	# 8
			pattern[8] = inputs[i][:]
		elif len(inputs[i]) == 6:
			sixLetterDigits.append(inputs[i][:])
		elif len(inputs[i]) == 5:
			fiveLetterDigits.append(inputs[i][:])
	
	# determin the six letter digits
	for i in range(len(sixLetterDigits)):
		digit = sixLetterDigits[i]
		if not is_subset_of(digit, pattern[1]):				# 6
			pattern[6] = digit[:]
		elif len(subtract_digit(digit, pattern[4])) == 2:	# 9
			pattern[9] = digit[:]
		elif len(subtract_digit(digit, pattern[4])) == 3:	# 0
			pattern[0] = digit[:]
	
	# determin the five letter digits
	for i in range(len(fiveLetterDigits)):
		digit = fiveLetterDigits[i]
		rest = subtract_digit(digit, pattern[1])
		if len(rest) == 3:													# 3
			pattern[3] = digit[:]
		elif len(rest) == 4 and len(subtract_digit(rest, pattern[4])) == 3:	# 2
			pattern[2] = digit[:]
		elif len(rest) == 4 and len(subtract_digit(rest, pattern[4])) == 2:	# 5
			pattern[5] = digit[:]

	return pattern


def is_subset_of(set, check):
	set_letters = [letter for letter in set]
	check_letters = [letter for letter in check]
	for letter in check_letters:
		if letter not in set_letters:
			return False
	return True


def subtract_digit(minuend, subtrahend):
	minuend_letters = [letter for letter in minuend]
	subtrahend_letters = [letter for letter in subtrahend]
	for letter in subtrahend_letters:
		if letter in minuend_letters:
			minuend_letters.remove(letter)
	return minuend_letters


# determin the output number using the analyized pattern
def decode_digit(digit, pattern):
	digit_letters = [letter for letter in digit]
	slotted_pattern = []
	for i in range(len(pattern)):
		slotted_pattern.append([])
		for j in range(len(pattern[i])):
			slotted_pattern[i].append(pattern[i][j])
	
	output = ""
	for i in range(len(slotted_pattern)):
		pattern = slotted_pattern[i][:]
		if len(pattern) != len(digit_letters):
			continue
		for letter in digit_letters:
			if letter in pattern:
				pattern.remove(letter)
			else:
				break
		
		if len(pattern) == 0:
			output += str(i)
	
	return output


# sum the output numbers and print the result
digit_sum = 0
for i in range(len(inputs)):
	input = inputs[i]
	output = outputs[i]
	pattern = analyze_pattern(input)
	decoded_digits = ""
	for digits in output:
		decoded_digits += decode_digit(digits, pattern)

	digit_sum += int(decoded_digits)


print("The sum of all decoded values is {}" .format(digit_sum))
