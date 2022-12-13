LINE_SEPARATOR = '\n'


def get_result(file_name):
    indices = 0

    i = 1
    with open(file_name, 'r') as f:
        new_line = LINE_SEPARATOR

        while new_line == LINE_SEPARATOR:
            left = eval(f.readline().strip())
            right = eval(f.readline().strip())

            if compare_lr(left, right):
                indices += i

            i += 1
            new_line = f.readline()

    return indices


def compare_lr(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return False
        return True

    elif isinstance(left, list) and isinstance(right, list):
        packet_item = 0
        while len(left) > packet_item:
            l = left[packet_item]
            try:
                r = right[packet_item]
            except IndexError:
                return False

            if l == r:
                packet_item += 1
                continue

            return compare_lr(l, r)

        if len(right) > packet_item:
            return True

        return True

    elif isinstance(left, int):
        return compare_lr([left], right)

    else:
        return compare_lr(left, [right])


if __name__ == '__main__':
    assert get_result('test_data/13') == 13
    print(get_result('data/13'))
