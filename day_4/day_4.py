def list_from_file(file, boards):
    """Create a list from a file"""
    with open(file) as f:
        lines = f.readlines()

    counter = 0
    board = []
    for i, line in enumerate(lines):
        # print(f"{i}: {line}")
        if i == 0:
            numbers = line.strip().split(",")
        elif line == "\n":
            board = []
            counter = 0
        else:
            board.append(line.strip().split())
            counter += 1
        if counter == 4:
            boards.append(board)
    f.close()
    return numbers


boards = []
numbers = list_from_file("day_4_input", boards)
# N of numbers drawn, line with marked numbers, index of board in array, drawn numbers
winning_line = (0, "", 0, "")

for i, board in enumerate(boards):
    for line in board:
        n_found = 0
        numbers_drawn = 0
        for index, number in enumerate(numbers):
            numbers_drawn += 1
            if number in line:
                n_found += 1
            if n_found == 5:
                if winning_line[0] == 0:
                    winning_line = (numbers_drawn, line, i, number)
                else:
                    if numbers_drawn < winning_line[0]:
                        winning_line = (numbers_drawn, line, i, number)

print(winning_line)
print(numbers[:numbers.index(winning_line[3]) + 1])
sum = 0
for line in boards[winning_line[2]]:
    for num in line:
        if num not in numbers[:numbers.index(winning_line[3]) + 1]:
            sum += int(num)

print(sum * 35)
output = open("day_4_output", "w")
# output.write(str(sum * winning_line[3]))
output.close()