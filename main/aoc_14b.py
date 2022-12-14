from main.aoc_14a import prepare_rested_rocks, show_cave

source = [500, 0]


def get_result(file_name, show=False):
    rested_rocks = prepare_rested_rocks(file_name)

    sands = 0
    rested_sand = []
    for y in range(0, max([r[1] for r in rested_rocks]) + 2):
        sand = 1 + 2 * y
        for x in range(source[0] - y, source[0] + y + 1):

            if [x, y] in rested_rocks:
                sand -= 1
            else:
                rocks_above = all(True if [above, y - 1] in rested_rocks else False for above in range(x - 1, x + 2))
                if rocks_above:
                    rested_rocks.append([x, y])
                    sand -= 1
                else:
                    rested_sand.append([x, y])

        sands += sand

    if show:
        show_cave(rested_rocks, rested_sand)
    return sands


if __name__ == '__main__':
    assert get_result('test_data/14', True) == 93
    print(get_result('data/14'))
