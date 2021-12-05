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

def check_rows(board):
    """Check if there is a complete row"""
    if (len(board) == 1):
        return 0
    for line in board:
        sum = 0
        for number in line:
            sum += int(number)
        if sum == -5:
            return 1
    return 0

def check_columns(board):
    """Check if there is a complete column"""
    if (len(board) == 1):
        return 0
    for n in range(5):
        sum = 0
        for line in board:
            sum += int(line[n])
        if sum == -5:
            return 1
    return 0



boards = []
numbers = list_from_file("day_4_input", boards)
last_board_index = 0

# For every number to draw
for i_nums, number in enumerate(numbers):
    # Marking all -1 first
    # For every board
    for i_boards, board in enumerate(boards):
        # For every line
        for i_board, line in enumerate(board):
            if number in line:
                line = ["-1" if num == number else num for num in line]
                boards[i_boards][i_board] = line

    # For board, check if completed; if so, empty it
    for i_boards, board in enumerate(boards):
        # Check for rows and columns
        if check_rows(board) or check_columns(board) == 1:
            boards[i_boards] = [[]]
    
    # Break if there's only one non completed board left
    sum = 0
    for i_boards, board in enumerate(boards):
        if len(board) == 5:
            sum += len(board)
            last_board_index = i_boards
    if sum == 5:
        break

# Keep filling last one till one row or column is complete
last_number = 0
# For every number still to draw
for i_nums, number in enumerate(numbers[numbers.index(number) + 1:]):
    # For every line
    for i_board, line in enumerate(boards[last_board_index]):
        # Adding -1 where necessary
        if number in line:
            line = ["-1" if num == number else num for num in line]
            boards[last_board_index][i_board] = line
    # If it's complete, break
    if check_rows(boards[last_board_index]) or check_columns(boards[last_board_index]) == 1:
        last_number = number
        break

# Summing all non marked numbers
sum = 0
for line in boards[last_board_index]:
    for number in line:
        if number != "-1":
            sum += int(number)

output = open("day_4_output_part_2", "w")
output.write(str(sum * int(last_number)))
output.close()