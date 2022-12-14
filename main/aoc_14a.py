source = [500, 0]


def get_result(file_name, show=False):
    rested_rocks = prepare_rested_rocks(file_name)
    rested_sand_size = falling_sand(rested_rocks, show)
    return rested_sand_size


def falling_sand(rested_rocks, show):
    max_y = max([r[1] for r in rested_rocks])
    min_x = min([r[0] for r in rested_rocks])
    max_x = max([r[0] for r in rested_rocks])

    rested_sand = []
    moving_in_picture = True
    while moving_in_picture:
        sand = source[:]
        rest_on_rock = False
        while not rest_on_rock and moving_in_picture:

            if not [sand[0], sand[1] + 1] in rested_rocks:
                rest_on_rock = False
                sand = [sand[0], sand[1] + 1]
            elif not [sand[0] - 1, sand[1] + 1] in rested_rocks:
                rest_on_rock = False
                sand = [sand[0] - 1, sand[1] + 1]
            elif not [sand[0] + 1, sand[1] + 1] in rested_rocks:
                rest_on_rock = False
                sand = [sand[0] + 1, sand[1] + 1]
            else:
                rest_on_rock = True
                rested_rocks.append([sand[0], sand[1]])
                rested_sand.append([sand[0], sand[1]])

            moving_in_picture = min_x < sand[0] < max_x and 0 < sand[1] < max_y
    if show:
        show_cave(rested_rocks, rested_sand)

    return len(rested_sand)


def prepare_rested_rocks(file_name):
    rested_rocks = []

    max_x = 0
    min_x = 1000
    max_y = 0

    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            rocks = line.split(' -> ')

            for i in range(0, len(rocks) - 1):
                x_1, y_1 = [int(r) for r in rocks[i].split(',')]
                x_2, y_2 = [int(r) for r in rocks[i + 1].split(',')]

                min_x = min(min_x, x_1, x_2)
                max_x = max(max_x, x_1, x_2)
                max_y = max(max_y, y_1, y_2)

                for x in range(min(x_1, x_2), max(x_1, x_2) + 1):
                    for y in range(min(y_1, y_2), max(y_1, y_2) + 1):
                        rested_rocks.append([x, y])

    return rested_rocks


def show_cave(rested_rocks, rested_sand):
    max_y = max([s[1] for s in rested_sand + rested_rocks])
    min_x = min([s[0] for s in rested_sand + rested_rocks])
    max_x = max([s[0] for s in rested_sand + rested_rocks])

    for y in range(max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            if x == source[0] and y == source[1]:
                row += '+'
            elif [x, y] in rested_sand:
                row += 'o'
            elif [x, y] in rested_rocks:
                row += '#'
            else:
                row += '.'
        print(row)


if __name__ == '__main__':
    assert get_result('test_data/14', True) == 24
    print(get_result('data/14'))
