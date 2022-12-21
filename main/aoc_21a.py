import re

SIGN_REGEXP = r'[\+\-*/]'


def get_result(file_name):
    cpu, monkeys = prepare_monkeys(file_name)

    while 'root' not in cpu.keys():
        for monkey, op in monkeys.items():
            if monkey not in cpu.keys():
                monkey_1, monkey_2 = [m.strip() for m in re.split(SIGN_REGEXP, op)]
                if monkey_1 in cpu.keys() and monkey_2 in cpu.keys():
                    cpu[monkey] = eval(op, {monkey_1: cpu[monkey_1], monkey_2: cpu[monkey_2]})

    return cpu['root']


def prepare_monkeys(file_name):
    monkeys = {}
    cpu = {}
    with open(file_name, 'r') as f:
        for ind, line in enumerate(f):
            line = line.strip()
            name, operation = line.split(': ')
            if operation.isnumeric():
                cpu[name] = int(operation)
            monkeys[name] = operation
    return cpu, monkeys


if __name__ == '__main__':
    assert get_result('test_data/21') == 152
    print(get_result('data/21'))
