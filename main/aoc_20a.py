import copy


def find_item_on_list(new_list, n, id):
    return [i for i, x in new_list.items() if id == x['id'] and n == x['value']][0]


def get_result(file_name):
    original_order = prepare_original_order(file_name)

    new_list = mix(original_order)

    index_zero = [x['value'] for x in new_list.values()].index(0)

    return sum([new_list[(1000 + index_zero) % len(new_list)]['value'],
                new_list[(2000 + index_zero) % len(new_list)]['value'],
                new_list[(3000 + index_zero) % len(new_list)]['value']])


def mix(original_order, new_list=None):

    if new_list is None:
        new_list = copy.deepcopy(original_order)

    for id, props in original_order.items():
        print(id)
        n = props['value']
        if n == 0:
            continue
        ind = find_item_on_list(new_list, n, id)
        new_index = (n + ind) % (len(new_list) - 1)
        tmp_list = copy.deepcopy(new_list)
        if new_index == 0:
            new_index = len(new_list) - 1
        tmp_list[new_index] = props
        if ind < new_index:
            for i in range(ind, new_index):
                tmp_list[i] = new_list[i + 1]
        else:
            for i in range(new_index + 1, ind + 1):
                tmp_list[i] = new_list[i - 1]
        new_list = copy.deepcopy(tmp_list)
    return new_list


def prepare_original_order(file_name, decription_key=1):
    original_order = {}
    with open(file_name, 'r') as f:
        for ind, line in enumerate(f):
            number = int(line.strip())
            original_order[ind] = {'value': number * decription_key, 'id': ind}
    return original_order


if __name__ == '__main__':
    assert get_result('test_data/20') == 3
    print(get_result('data/20'))
