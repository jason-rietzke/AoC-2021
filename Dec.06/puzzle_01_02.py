

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

# load fish list
fish_list = [[int(value) for value in input_lines[0].split(",")]]

# # test input
# fish_list = []
# for line in input_lines:
# 	values = line.split(":")[1].split(",")
# 	fishes = [int(value) for value in values]
# 	fish_list.append(fishes)


def forecast_popultation(list, day_count):
	new_fish_list = list[:]
	while len(new_fish_list) <= day_count:
		new_fish_generation = new_fish_list[-1]
		for i in range(len(new_fish_list[-1])):
			fish = new_fish_list[-1][i]
			if fish > 0:
				new_fish_generation[i] = fish - 1
			else:
				new_fish_generation[i] = 6
				new_fish_generation.append(8)
		new_fish_list.append(new_fish_generation)
	return new_fish_list


# forecast fish list for 80 generations
fish_list_80 = forecast_popultation(fish_list, 80)
print("There are {} fishes in day 80" .format(len(fish_list_80[-1])))

# forecast fish list for 256 generations
fish_list_256 = forecast_popultation(fish_list, 256)
print("There are {} fishes in day 256" .format(len(fish_list_256[-1])))
