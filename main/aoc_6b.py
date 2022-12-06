from main.aoc_6a import get_result

if __name__ == '__main__':
    assert get_result('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
    assert get_result('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
    assert get_result('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
    assert get_result('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
    assert get_result('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26
    with open('data/6', 'r') as f:
        print(get_result(f.readline(), 14))
