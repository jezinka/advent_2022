from collections import Counter


def get_result(file_name):
    start_points = prepare_start_points(file_name)
    singular_walls = get_singular_walls(start_points)
    return len(singular_walls)


def get_singular_walls(start_points):
    walls = []
    for x, y, z in [*start_points]:
        a = (x, y, z)
        b = (x + 1, y, z)
        c = (x + 1, y + 1, z)
        d = (x, y + 1, z)
        e = (x, y, z + 1)
        f = (x + 1, y, z + 1)
        g = (x + 1, y + 1, z + 1)
        h = (x, y + 1, z + 1)
        walls.append(f"{a},{b},{c},{d}")
        walls.append(f"{a},{d},{h},{e}")
        walls.append(f"{a},{b},{f},{e}")
        walls.append(f"{e},{f},{g},{h}")
        walls.append(f"{b},{c},{g},{f}")
        walls.append(f"{d},{c},{g},{h}")
    countr = Counter(walls)
    return [w for w in countr if countr[w] == 1]


def prepare_start_points(file_name):
    start_points = []
    with open(file_name, 'r') as f:
        for line in f:
            x, y, z = [*line.strip().split(',')]
            start_points.append([int(x), int(y), int(z)])
    return start_points


if __name__ == '__main__':
    assert get_result('test_data/18') == 10
    assert get_result('test_data/18_2') == 64
    print(get_result('data/18'))
