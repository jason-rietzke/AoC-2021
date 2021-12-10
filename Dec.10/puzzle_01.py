

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

syntax_error_score = 0

braket_scores = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137,
}

for line in input_lines:
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
				syntax_error_score += braket_scores[symbol]
				break

print("Final syntax error score: {}" .format(syntax_error_score))

