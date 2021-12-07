

input = open("input.txt")
lines = [line.strip() for line in input]
draws = []

# load draws
for number in lines[0].split(","):
	draws.append(int(number))

# load boards
boards = [[]]
for line in lines[2:]:
	if line == "":
		boards.append([])
		continue

	board = boards[-1]
	row = []
	for number in line.split(" "):
		if number != "":
			row.append(int(number))
	board.append(row)
	
input.close()


# number of nessesary draws
def check_line(line, draws):
	needed_numbers = line[:]
	draw_counter = 0
	for i in range(len(draws)):
		draw = draws[i]
		if draw in needed_numbers:
			needed_numbers.remove(draw)
		draw_counter += 1
		if len(needed_numbers) == 0:
			return {
				"count": draw_counter,
				"draw": draw,
			}
	return -1


# calculate subtraction
def calc_subtraction(board, draws):
	subtraction = 0
	for row in board:
		for number in row:
			if number in draws:
				subtraction += number
	return subtraction


# minimum draws per board
def check_board(board, draws):
	min_draws = -1
	draw = -1
	board_sum = sum(sum(row) for row in board)
	rest_sum = 0

	# check horizontal
	for row in board:
		check = check_line(row, draws)
		if min_draws == -1 or min_draws > check["count"]:
			min_draws = check["count"]
			draw = check["draw"]
			rest_sum = board_sum - calc_subtraction(board, draws[0:min_draws])

	# check vertical
	for i in range(len(board[0])):
		column = [row[i] for row in board]
		check = check_line(column, draws)
		if min_draws == -1 or min_draws > check["count"]:
			min_draws = check["count"]
			draw = check["draw"]
			rest_sum = board_sum - calc_subtraction(board, draws[0:min_draws])
	
	return {
		"count": min_draws,
		"draw": draw,
		"rest": rest_sum,
	}


# check all boards
runs = []
for board in boards:
	runs.append(check_board(board, draws))

best_index = runs.index(min(runs, key=lambda x: x["count"]))
best_run = runs[best_index]

print("The best board is #{} with {} draws and {} rest.".format(best_index + 1, best_run["count"], best_run["rest"]))
print("Final score: " + str(best_run["rest"] * best_run["draw"]))
