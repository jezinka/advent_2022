def prepare_data(file_name):
    with open(file_name, 'r') as f:
        elf = 1
        elves = {elf: 0}
        for line in f.readlines():
            if line == '\n':
                elf += 1
                elves[elf] = 0
            else:
                elves[elf] += int(line)
    return elves


def get_most_calorific_elf(file_name):
    prepared_elves = prepare_data(file_name)
    return prepared_elves[max(prepared_elves, key=prepared_elves.get)]


if __name__ == '__main__':
    assert get_most_calorific_elf('test_data/1') == 24000
    print(get_most_calorific_elf('data/1'))
