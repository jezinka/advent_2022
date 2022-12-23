from collections import Counter


def get_result(file_name, show_preview=True):
    elf_map, occupied_positions = prepare_elves(file_name)
    if show_preview:
        show_us(occupied_positions)

    directions = ['N', 'S', 'W', 'E']
    for _ in range(10):
        move_elves(directions, elf_map, occupied_positions)
        if show_preview:
            show_us(occupied_positions)

    max_x, max_y, min_x, min_y = find_rectangle(occupied_positions)

    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elf_map.keys())


def move_elves(directions, elf_map, occupied_positions):
    they_move = False
    possible_positions = []
    for elf_key, elf in elf_map.items():
        adjacent_positions = []
        x, y = elf['position']
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i != x or j != y:
                    adjacent_positions.append([i, j])

        if all([p not in occupied_positions for p in adjacent_positions]):
            continue

        for direction in directions:
            if direction == 'N':
                wall_to_check = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1]]
                if any([neighbour in occupied_positions for neighbour in wall_to_check]):
                    continue
                else:
                    elf['possible_position'] = wall_to_check[1]
                    elf['considered_direction'] = direction
                    possible_positions.append(stringify_position(elf))
                    break

            elif direction == 'S':
                wall_to_check = [[x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]
                if any([neighbour in occupied_positions for neighbour in wall_to_check]):
                    continue
                else:
                    elf['possible_position'] = wall_to_check[1]
                    elf['considered_direction'] = direction
                    possible_positions.append(stringify_position(elf))
                    break
            elif direction == 'W':
                wall_to_check = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1]]
                if any([neighbour in occupied_positions for neighbour in wall_to_check]):
                    continue
                else:
                    elf['possible_position'] = wall_to_check[1]
                    elf['considered_direction'] = direction
                    possible_positions.append(stringify_position(elf))
                    break

            elif direction == 'E':
                wall_to_check = [[x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]
                if any([neighbour in occupied_positions for neighbour in wall_to_check]):
                    continue
                else:
                    elf['possible_position'] = wall_to_check[1]
                    elf['considered_direction'] = direction
                    possible_positions.append(stringify_position(elf))
                    break

    dir = directions[0]
    directions.remove(dir)
    directions.append(dir)

    how_many_elves = Counter(possible_positions)

    for elf_key, elf in elf_map.items():
        if 'possible_position' in elf.keys():
            if elf['possible_position'] is not None:
                if how_many_elves[stringify_position(elf, 'possible_position')] == 1:
                    occupied_positions.remove(elf['position'])
                    elf['position'] = [*elf['possible_position']]
                    occupied_positions.append(elf['position'])
                    they_move = True

        elf['possible_position'] = None
        elf['considered_direction'] = ''

    return they_move


def stringify_position(elf, key='possible_position'):
    return ','.join([str(e) for e in elf[key]])


def prepare_elves(file_name):
    elf_map = {}
    occupied_positions = []
    elf_no = 0
    with open(file_name, 'r') as f:
        for x, line in enumerate(f):
            for y, tile in enumerate([*line]):
                if tile == '#':
                    elf_map[elf_no] = {'position': [x, y]}
                    occupied_positions.append([x, y])
                    elf_no += 1
    return elf_map, occupied_positions


def show_us(occupied_positions):
    max_x, max_y, min_x, min_y = find_rectangle(occupied_positions)

    for x in range(min_x - 1, max_x + 2):
        row = ''
        for y in range(min_y - 1, max_y + 2):
            if [x, y] in occupied_positions:
                row += '#'
            else:
                row += '.'
        print(row)
    print()


def find_rectangle(occupied_positions):
    min_x, min_y = 100, 100
    max_x, max_y = -100, -100
    for item in occupied_positions:
        min_x = min(item[0], min_x)
        min_y = min(item[1], min_y)
        max_x = max(item[0], max_x)
        max_y = max(item[1], max_y)
    return max_x, max_y, min_x, min_y


if __name__ == '__main__':
    assert get_result('test_data/23_0') == 25
    assert get_result('test_data/23') == 110
    print(get_result('data/23', False))
