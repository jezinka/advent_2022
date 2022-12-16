from aoc_15a import get_manhattan_distance, get_beacon_sensor_coordinates


def get_result(file_name, max_size):
    items, _ = get_beacon_sensor_coordinates(file_name, None)
    potential_result = get_points_to_check(items, max_size)
    return potential_result[0] * 4000000 + potential_result[1]


def check_point(x, y, items, max_size, sensor_index):
    if 0 < x <= max_size and 0 < y < max_size:
        for index, item in enumerate(items):

            if index == sensor_index:
                continue

            sensor = item['sensor']
            distance = item['distance']

            if get_manhattan_distance([x, y], sensor) <= distance:
                return None

        return [x, y]

    return None


def get_points_to_check(items, max_size):
    for index, item in enumerate(items):
        sensor = item['sensor']
        distance = item['distance'] + 1

        x1 = sensor[0]
        x2 = sensor[0]
        y = sensor[1] - distance

        if check_point(x1, y, items, max_size, index) is not None:
            return [x1, y]

        for i in range(1, distance + 1):
            x1 += 1
            if check_point(x1, y + i, items, max_size, index) is not None:
                return [x1, y + i]
            x2 -= 1
            if check_point(x2, y + i, items, max_size, index) is not None:
                return [x2, y + i]
        for i in range(distance + 1, sensor[1] + distance - 1):
            x1 -= 1
            if check_point(x1, y + i, items, max_size, index) is not None:
                return [x1, y + i]
            x2 += 1
            if check_point(x2, y + i, items, max_size, index) is not None:
                return [x2, y + i]

        if check_point(sensor[0], sensor[1] + distance, items, max_size, index) is not None:
            return [sensor[0], sensor[1] + distance]

    return None


if __name__ == '__main__':
    assert get_result('test_data/15', 20) == 56000011
    print(get_result('data/15', 4000000))
