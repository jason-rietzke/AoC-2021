

input = open("input.txt")
input_lines = [line.strip() for line in input]
input.close()

# load fish list
fish_list = [int(value) for value in input_lines[0].split(",")] # input
# fish_list = [int(value) for value in input_lines[0].split(":")[1].split(",")] # test

fish_data = [0 for i in range(0, 9)]

for fish in fish_list:
	fish_data[fish] += 1

def forecast_popultation(data, day_count):
	fish_data = data[:]
	day = 1
	fish_data_update = fish_data[:]
	while day <= day_count:
		for i in range(0, 9):
			if i > 0:
				fish_data_update[i - 1] += fish_data[i]
				fish_data_update[i] -= fish_data[i]
			else:
				fish_data_update[6] += fish_data[0]
				fish_data_update[8] += fish_data[0]
				fish_data_update[0] -= fish_data[0]
		fish_data = fish_data_update[:]
		day += 1
	return fish_data


# forecast fish list for 80 generations
fish_data_80 = forecast_popultation(fish_data, 80)
fish_sum_80 = sum( data for data in fish_data_80 )
print("There are {} fishes in day 80" .format(fish_sum_80))

# forecast fish list for 256 generations
fish_data_256 = forecast_popultation(fish_data, 256)
fish_sum_256 = sum( data for data in fish_data_256 )
print("There are {} fishes in day 256" .format(fish_sum_256))

