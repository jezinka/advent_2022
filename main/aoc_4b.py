from main.aoc_4a import prepare_elves_territories


def get_result(file_name):
    overlapped_elves = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            elf_a, elf_b = prepare_elves_territories(line)
            if len(elf_a & elf_b) > 0:
                overlapped_elves += 1
    return overlapped_elves


if __name__ == '__main__':
    assert get_result('test_data/4') == 4
    print(get_result('data/4'))
