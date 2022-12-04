def prepare_elves_territories(line):
    line = line.strip()
    elf_1, elf_2 = line.split(',')
    elf_1_b, elf_1_e = elf_1.split('-')
    elf_2_b, elf_2_e = elf_2.split('-')
    elf_a = set(range(int(elf_1_b), int(elf_1_e) + 1))
    elf_b = set(range(int(elf_2_b), int(elf_2_e) + 1))
    return elf_a, elf_b


def get_result(file_name):
    fully_overlapped_elves = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            elf_a, elf_b = prepare_elves_territories(line)
            if len(elf_a & elf_b) > 0 and (len(elf_a - elf_b) == 0 or len(elf_b - elf_a) == 0):
                fully_overlapped_elves += 1
    return fully_overlapped_elves


if __name__ == '__main__':
    assert get_result('test_data/4') == 2
    print(get_result('data/4'))
