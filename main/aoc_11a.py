import math

from monkey import Monkey


def get_result(file_name):
    monkeys = prepare_monkeys(file_name)
    play(monkeys, 20, True)

    return math.prod(sorted([m.items_inspected for m in monkeys], reverse=True)[:2])


def play(monkeys, max_round, with_relief):
    round = 0
    supermodulo = math.prod([m.test_condition for m in monkeys])

    while round < max_round:
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)

                if not with_relief:
                    item = item % supermodulo

                item = monkey.inspects(item)

                if with_relief:
                    item //= 3
                if monkey.test(item):
                    monkeys[monkey.true_monkey].items.append(item)
                else:
                    monkeys[monkey.false_monkey].items.append(item)
                monkey.items_inspected += 1

        round += 1


def prepare_monkeys(file_name):
    monkeys = []
    with open(file_name) as f:
        for line in f:
            monkey = None

            if line.startswith('Monkey'):
                monkey = Monkey()

            items = f.readline().strip().removeprefix('Starting items: ').split(', ')
            monkey.items = [int(i) for i in items]
            monkey.operation = f.readline().strip().removeprefix('Operation: new = ')

            monkey.test_condition = int(f.readline().strip().removeprefix('Test: divisible by '))
            monkey.true_monkey = int(f.readline().strip().removeprefix('If true: throw to monkey '))
            monkey.false_monkey = int(f.readline().strip().removeprefix('If false: throw to monkey '))
            if f.readline().strip() == '':
                monkeys.append(monkey)
    return monkeys


if __name__ == '__main__':
    assert get_result('test_data/11') == 10605
    print(get_result('data/11'))
