

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

day_count = 80

# load fish list
fish_list = [[int(value) for value in input_lines[0].split(",")]]

print(fish_list)

# # test input
# for line in input_lines:
# 	values = line.split(":")[1].split(",")
# 	fishes = [int(value) for value in values]
# 	fish_list.append(fishes)

# forecast fish list for 80 generations
while len(fish_list) <= day_count:
	new_fish_generation = fish_list[-1]
	for i in range(len(fish_list[-1])):
		fish = fish_list[-1][i]
		if fish > 0:
			new_fish_generation[i] = fish - 1
		else:
			new_fish_generation[i] = 6
			new_fish_generation.append(8)
	fish_list.append(new_fish_generation)

print("There are {} fishes in generation {}" .format(len(fish_list[-1]), day_count))

