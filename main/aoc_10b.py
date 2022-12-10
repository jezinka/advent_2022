from crt import Crt


def get_result(file_name, dark_pixel='.'):
    crt = Crt(dark_pixel)

    while crt.drawn_lines() < 5:
        with open(file_name) as f:
            for line in f:
                crt.parse_instruction(line)


if __name__ == '__main__':
    get_result('test_data/10')
    print()
    get_result('data/10', ' ')
