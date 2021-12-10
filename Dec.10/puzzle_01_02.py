

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

navigation_lines = input_lines[:]
cleaned_navigation_lines = navigation_lines[:]

syntax_error_score = 0

braket_error_scores = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137,
}

for line in navigation_lines:
	expected_symbols = []
	for symbol in line:
		if symbol == "(" or symbol == "[" or symbol == "{" or symbol == "<":
			expected_symbols.append(symbol)

		elif symbol == ")" or symbol == "]" or symbol == "}" or symbol == ">":
			if expected_symbols[-1] == "(" and symbol == ")":
				expected_symbols.pop()
			elif expected_symbols[-1] == "[" and symbol == "]":
				expected_symbols.pop()
			elif expected_symbols[-1] == "{" and symbol == "}":
				expected_symbols.pop()
			elif expected_symbols[-1] == "<" and symbol == ">":
				expected_symbols.pop()
			else:
				syntax_error_score += braket_error_scores[symbol]
				cleaned_navigation_lines.remove(line)
				break

print("Final syntax error score: {}" .format(syntax_error_score))


syntax_completion_scores = []

braket_completion_scores = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4,
}

for line in cleaned_navigation_lines:
	syntax_completion_score = 0
	expected_symbols = []
	for symbol in line:
		if symbol == "(" or symbol == "[" or symbol == "{" or symbol == "<":
			expected_symbols.append(symbol)

		elif symbol == ")" or symbol == "]" or symbol == "}" or symbol == ">":
			expected_symbols.pop()

	for i in range(len(expected_symbols)):
		symbol = expected_symbols[ len(expected_symbols) - 1 - i ]
		syntax_completion_score *= 5
		if symbol == "(":
			syntax_completion_score += braket_completion_scores[")"]
		elif symbol == "[":
			syntax_completion_score += braket_completion_scores["]"]
		elif symbol == "{":
			syntax_completion_score += braket_completion_scores["}"]
		elif symbol == "<":
			syntax_completion_score += braket_completion_scores[">"]

	syntax_completion_scores.append(syntax_completion_score)

syntax_completion_scores.sort()
print("Final middle score: {}" .format(syntax_completion_scores[len(syntax_completion_scores) // 2]))

