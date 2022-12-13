from functools import cmp_to_key

from aoc_13a import compare_lr, LINE_SEPARATOR


def get_result(file_name):
    divider_1 = [[2]]
    divider_2 = [[6]]

    packets = get_all_packets(file_name)
    packets += ([divider_1, divider_2])

    packets.sort(key=cmp_to_key(make_comparator(compare_lr)))

    return (packets.index(divider_1) + 1) * (packets.index(divider_2) + 1)


# thanks to https://stackoverflow.com/q/12749398/7909729
def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0

    return compare


def get_all_packets(file_name):
    packets = []
    with open(file_name, 'r') as f:
        new_line = LINE_SEPARATOR

        while new_line == LINE_SEPARATOR:
            left = eval(f.readline().strip())
            right = eval(f.readline().strip())

            packets.append(left)
            packets.append(right)

            new_line = f.readline()

    return packets


if __name__ == '__main__':
    assert get_result('test_data/13') == 140
    print(get_result('data/13'))
