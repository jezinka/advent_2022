from main.aoc_20a import mix, prepare_original_order


def get_result(file_name):
    decription_key = 811589153

    original_order = prepare_original_order(file_name, decription_key)

    nl = None
    for _ in range(10):
        new_list = mix(original_order, nl)
        nl = new_list

    index_zero = [x['value'] for x in new_list.values()].index(0)

    return sum([new_list[(1000 + index_zero) % len(new_list)]['value'],
                new_list[(2000 + index_zero) % len(new_list)]['value'],
                new_list[(3000 + index_zero) % len(new_list)]['value']])


if __name__ == '__main__':
    assert get_result('test_data/20') == 1623178306
    print(get_result('data/20'))
