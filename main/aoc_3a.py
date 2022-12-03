import string

priorities = dict(zip(list(string.ascii_lowercase) + list(string.ascii_uppercase), range(1, 53)))


def get_priority(letter):
    return priorities.get(letter)


def get_result(file_name):
    priorities_sum = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            first_half = line[0:len(line) // 2]
            second_half = line[len(line) // 2:]
            common_item = list(set(first_half) & set(second_half))[0]
            priorities_sum += get_priority(common_item)
    return priorities_sum


if __name__ == '__main__':
    assert get_result('test_data/3') == 157
    print(get_result('data/3'))
