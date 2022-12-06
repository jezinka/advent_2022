def get_result(message, marker_length=4):
    index = -1
    for i in range(0, len(message) - marker_length + 1):
        marker = message[i:i + marker_length]
        if len(set(marker)) == marker_length:
            index = i + marker_length
            break
    return index


if __name__ == '__main__':
    assert get_result('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
    assert get_result('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert get_result('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert get_result('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert get_result('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
    with open('data/6', 'r') as f:
        print(get_result(f.readline()))
