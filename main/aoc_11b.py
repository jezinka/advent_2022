import math

from aoc_11a import prepare_monkeys, play


def get_result(file_name):
    monkeys = prepare_monkeys(file_name)
    play(monkeys, 10000, False)

    return math.prod(sorted([m.items_inspected for m in monkeys], reverse=True)[:2])


if __name__ == '__main__':
    assert get_result('test_data/11') == 2713310158
    print(get_result('data/11'))
