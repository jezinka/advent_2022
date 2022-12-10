from aoc_3a import get_priority


def get_result(file_name):
    priorities_sum = 0
    with open(file_name, 'r') as f:
        lines = list(map(lambda l: l.strip(), f.readlines()))
        for i in range(0, len(lines), 3):
            group = lines[i:i + 3]
            common_item = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
            priorities_sum += get_priority(common_item)
    return priorities_sum


if __name__ == '__main__':
    assert get_result('test_data/3') == 70
    print(get_result('data/3'))
