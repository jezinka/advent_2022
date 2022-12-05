import re


def prepare_carts(f):
    carts = {}
    while True:
        line = f.readline()
        if line.strip() == '':
            break
        if not ('[' in line):
            continue
        j = 1
        for i in range(0, len(line), 4):
            if not (j in carts.keys()):
                carts[j] = []
            cart = line[i: i + 3].strip('[] ')
            if cart != '':
                carts[j].append(cart)
            j += 1
    return carts


def get_parsed_instruction(line):
    m = re.search("move (\d+) from (\d+) to (\d+)", line)
    counter = int(m.group(1))
    src = int(m.group(2))
    dest = int(m.group(3))
    return counter, dest, src


def get_result(file_name):
    with open(file_name, 'r') as f:

        carts = prepare_carts(f)

        for line in f.readlines():
            counter, dest, src = get_parsed_instruction(line)
            for x in range(counter):
                carts[dest] = carts[src][0:1] + carts[dest]
                del carts[src][0]

    return ''.join([item[0] for item in carts.values()])


if __name__ == '__main__':
    assert get_result('test_data/5') == 'CMZ'
    print(get_result('data/5'))
