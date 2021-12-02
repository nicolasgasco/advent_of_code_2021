# First part

def list_from_file(file):
	"""Create a list from a file"""
	cmds_list = []
	with open(file) as f:
		cmds = f.readlines()

	for cmd in cmds:
		cmds_list.append(tuple(cmd.strip().split(" ")))
	f.close()
	return cmds_list

depth = 0
horizontal = 0

cmds = list_from_file("day_2_input")
for direction, moves in cmds:
	if direction == 'forward':
		horizontal += int(moves)
	elif direction == 'up':
		depth -= int(moves)
	elif direction == 'down':
		depth += int(moves)

output = open("day_2_output_part_1", "w")
output.write(str(depth * horizontal))
output.close()

# Second part
depth = 0
horizontal = 0
aim = 0

cmds = list_from_file("day_2_input")
for direction, moves in cmds:
	if direction == 'up':
		aim -= int(moves)
	elif direction == 'down':
		aim += int(moves)
	elif direction == 'forward':
		horizontal += int(moves)
		depth += (aim * int(moves))

output = open("day_2_output_part_2", "w")
output.write(str(depth * horizontal))
output.close()
