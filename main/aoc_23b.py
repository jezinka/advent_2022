from aoc_23a import prepare_elves, move_elves


def get_result(file_name):
    elf_map, occupied_positions = prepare_elves(file_name)

    directions = ['N', 'S', 'W', 'E']
    move_counter = 0
    they_move = True
    while they_move:
        they_move = move_elves(directions, elf_map, occupied_positions)
        move_counter += 1
    return move_counter


if __name__ == '__main__':
    assert get_result('test_data/23_0') == 4
    assert get_result('test_data/23') == 20
    print(get_result('data/23'))
