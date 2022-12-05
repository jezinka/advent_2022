from main.aoc_5a import prepare_carts, get_parsed_instruction


def get_result(file_name):
    with open(file_name, 'r') as f:
        carts = prepare_carts(f)

        for line in f.readlines():
            counter, dest, src = get_parsed_instruction(line)
            carts[dest] = carts[src][0:counter] + carts[dest]
            del carts[src][0:counter]

    return ''.join([item[0] for item in carts.values()])


if __name__ == '__main__':
    assert get_result('test_data/5') == 'MCD'
    print(get_result('data/5'))
