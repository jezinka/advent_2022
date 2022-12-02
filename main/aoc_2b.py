points = {'A': 1,
          'B': 2,
          'C': 3}


def get_result(file_name):
    total_score = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            e_move, result = line.strip().split(' ')
            if result == 'Y':
                total_score += 3 + points[e_move]
            elif result == 'Z':
                if e_move == 'A':
                    score = points['B']
                elif e_move == 'B':
                    score = points['C']
                else:
                    score = points['A']
                total_score += 6 + score
            else:
                if e_move == 'A':
                    score = points['C']
                elif e_move == 'B':
                    score = points['A']
                else:
                    score = points['B']
                total_score += score
    return total_score


if __name__ == '__main__':
    assert get_result('test_data/2') == 12
    print(get_result('data/2'))
