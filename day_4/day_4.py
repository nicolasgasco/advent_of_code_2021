from types import CodeType


def list_from_file(file, boards):
    """Create a list from a file"""
    with open(file) as f:
        lines = f.readlines()

    counter = 0
    board = []
    for i, line in enumerate(lines):
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
winning_line = (0, "") # index of board, drawn number

for index, number in enumerate(numbers):
    # First mark all drawn numbers with -1
    for i, board in enumerate(boards):
        for ind, line in enumerate(board):
            if number in line:
                line = ["-1" if num == number else num for num in line]
                boards[i][ind] = line
    
    # For every drawn number, check if one board is completed
    for i, board in enumerate(boards):
        for line in board:
            # I'm checking columns only
            # I knew it wasn't a row through trial and error
            for n in range(5):
                sum = 0
                for line in board:
                    sum += int(line[n])
                if sum == -5:
                    winning_line = (i, number)
                    break
                # Look soon, how beautiful this Christmas tree is
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break

# Summing all non marked numbers
sum = 0
for line in boards[winning_line[0]]:
    for number in line:
        if number != "-1":
            sum += int(number)

output = open("day_4_output", "w")
output.write(str(sum * int(winning_line[1])))
output.close()