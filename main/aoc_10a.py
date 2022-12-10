from main.crt import Crt


def get_result(file_name):
    crt = Crt(' ')

    while crt.cycle_no < 221:
        with open(file_name) as f:
            for line in f:
                crt.parse_instruction(line)
    return sum(crt.results)


if __name__ == '__main__':
    assert get_result('test_data/10') == 13140
    print(get_result('data/10'))
