import re

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIRECTIONS_VIS = ['>', 'v', '<', '^']


def get_result(file_name, show_preview=False):
    board, instructions = prepare_board(file_name)

    d = 0
    direction = DIRECTIONS[d]
    x, y = get_starting_point(board)

    visited = {f'{x},{y}': DIRECTIONS_VIS[d]}
    if show_preview:
        show_us(board, visited)

    while len(instructions) > 0:
        instruction = re.search('(\d+)[RL]?', instructions).group(1)
        instructions = instructions.removeprefix(instruction)

        for i in range(int(instruction)):
            next_x, next_y = x + direction[0], y + direction[1]

            next_x, next_y = catch_out_of_board(board, next_x, next_y)

            while board[next_x][next_y] == ' ':
                next_x += direction[0]
                next_y += direction[1]
                next_x, next_y = catch_out_of_board(board, next_x, next_y)

            if board[next_x][next_y] == '#':
                break

            x = next_x
            y = next_y

            visited[f'{x},{y}'] = DIRECTIONS_VIS[d]

        if len(instructions) == 0:
            break

        new_direction = instructions[0]
        instructions = instructions.removeprefix(new_direction)
        if new_direction == 'R':
            d = (d + 1) % len(DIRECTIONS)
        elif new_direction == 'L':
            d = (d - 1) % len(DIRECTIONS)

        direction = DIRECTIONS[d]
        visited[f'{x},{y}'] = DIRECTIONS_VIS[d]
        if show_preview:
            show_us(board, visited)

    return 1000 * (x + 1) + 4 * (y + 1) + d


def get_starting_point(board):
    x, y = 0, 0
    for idx, tile in enumerate(board[0]):
        if tile == '.':
            y = idx
            break
    return x, y


def prepare_board(file_name):
    board = []
    instructions = ''
    max_length = 0
    with open(file_name, 'r') as f:
        for line in f:
            if line[0] in [' ', '.', '#']:
                line = line.strip('\n')
                max_length = max(max_length, len(line))
                board.append([*line])
            else:
                instructions = f.readline()
                break
    for x in board:
        while len(x) < max_length:
            x.append(' ')
    return board, instructions


def catch_out_of_board(board, next_x, next_y):
    if next_x < 0:
        next_x = len(board) - 1
    elif next_x > len(board) - 1:
        next_x = 0

    if next_y < 0:
        next_y = len(board[next_x]) - 1
    elif next_y > len(board[next_x]) - 1:
        next_y = 0
    return next_x, next_y


def show_us(board, visited):
    for x in range(len(board)):
        row = ''
        for y in range(len(board[x])):
            if f'{x},{y}' in visited.keys():
                row += visited[f'{x},{y}']
            else:
                row += board[x][y]
        print(row)
    print()


if __name__ == '__main__':
    assert get_result('test_data/22', True) == 6032
    print(get_result('data/22'))
