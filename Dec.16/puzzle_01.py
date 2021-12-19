

input = open("input.txt")
input_line = [line.strip() for line in input][0]
input.close()

binary_input = (bin(int(input_line, 16))[2:].zfill(len(input_line) * 4))
print(binary_input)

def sum_lengths(packet):
	length = packet["length"]
	for sub_packet in packet["sub_packets"]:
		length += sum_lengths(sub_packet)
	return length


def decode_packet(packet):
	version = int(packet[0:3], 2)
	type_id = int(packet[3:6], 2)
	data = packet[6:]
	length = 0
	literal = None
	sub_packets = []
	# print("Packat Version {}; Type ID {}; Data {}".format(version, type_id, packet))

	if type_id == 4: # literal
		literal_binary = ""
		literal_groups = []
		while len(literal_groups) < 1 or literal_groups[-1][0] == "1":
			literal_group = data[len(literal_groups) * 5:(len(literal_groups) * 5) + 5]
			literal_groups.append(literal_group)
			literal_binary += str(literal_group[1:])
		literal = int(literal_binary, 2)
		length = 6 + (len(literal_groups) * 5)

	else: # operator
		length_type_id = int(data[0:1], 2)
		data = data[1:]
		
		if length_type_id == 0:
			total_length = int(data[0:15], 2)
			data = data[15:]
			detected_length = 0
			while detected_length < total_length:
				try:
					sub_packet = decode_packet(data[detected_length:])
					sub_packets.append(sub_packet)
					detected_length += sum_lengths(sub_packet)
				except:
					return {
						"version": version,
						"type_id": type_id,
						"length": len(packet),
						"literal": literal,
						"sub_packets": sub_packets
					}
		else:
			sub_packet_count = int(data[0:11], 2)
			data = data[11:]
			detected_length = 0
			for _ in range(sub_packet_count):
				try:
					sub_packet = decode_packet(data[detected_length:])
					sub_packets.append(sub_packet)
					detected_length += sum_lengths(sub_packet)
				except:
					return {
						"version": version,
						"type_id": type_id,
						"length": len(packet),
						"literal": literal,
						"sub_packets": sub_packets
					}
		
	if len(sub_packets) > 0:
		for sub_packet in sub_packets:
			length += sub_packet["length"]

	return {
		"version": version,
		"type_id": type_id,
		"length": length,
		"literal": literal,
		"sub_packets": sub_packets
	}


def comulate_versions(packet):
	version = packet["version"]
	for sub_packet in packet["sub_packets"]:
		version += comulate_versions(sub_packet)
	return version


def print_packet(packet, indent = 0):
	print(" " * indent + "Version {} - Type {}".format(packet["version"], packet["type_id"]))
	if packet["literal"] != None:
		print(" " * indent + "Literal: {}".format(packet["literal"]))
	for sub_packet in packet["sub_packets"]:
		print_packet(sub_packet, indent + 1)


packet = decode_packet(binary_input)
print_packet(packet)
comulated_version = comulate_versions(packet)
print("Comulated version: {}".format(comulated_version))
