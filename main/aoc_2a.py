points = {'A': 1,
          'B': 2,
          'C': 3,
          'X': 1,
          'Y': 2,
          'Z': 3}


def get_result(file_name):
    total_score = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            e_move, m_move = line.strip().split(' ')
            if points[e_move] == points[m_move]:
                total_score += 3 + points[m_move]
            elif (m_move == 'X' and e_move == 'C') or (m_move == 'Y' and e_move == 'A') or (
                    m_move == 'Z' and e_move == 'B'):
                total_score += 6 + points[m_move]
            else:
                total_score += points[m_move]
        return total_score


if __name__ == '__main__':
    assert get_result('test_data/2') == 15
    print(get_result('data/2'))
