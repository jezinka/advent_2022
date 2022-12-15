import re


def get_result(file_name, line):
    items, beacons = get_beacon_sensor_coordinates(file_name, line)
    not_present = []
    for index, item in enumerate(items):
        sensor = item['sensor']
        distance = item['distance']

        y = sensor[1]
        if y - distance < line < y + distance:
            x1 = -distance + abs(y - line) + sensor[0]
            x2 = distance - abs(y - line) + sensor[0]
            not_present += ([x for x in range(min(x1, x2), max(x1, x2) + 1)])
            not_present = list(set(not_present))

    not_present = set(not_present) - beacons

    return len(not_present)


def get_beacon_sensor_coordinates(file_name, y):
    sensors = []
    beacons = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            parsed_dict = re.search(
                "Sensor at x=(?P<sensor_x>\-?\d+), y=(?P<sensor_y>\-?\d+): closest beacon is at x=(?P<beacon_x>\-?\d+), y=(?P<beacon_y>\-?\d+)",
                line).groupdict()
            sensor = [int(parsed_dict['sensor_x']), int(parsed_dict['sensor_y'])]
            beacon = [int(parsed_dict['beacon_x']), int(parsed_dict['beacon_y'])]
            distance = get_manhattan_distance(sensor, beacon)
            sensors.append({'sensor': sensor, 'distance': distance})
            if beacon[1] == y:
                beacons.append(beacon[0])
    return sensors, set(beacons)


def get_manhattan_distance(sensor, beacon):
    return abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])


if __name__ == '__main__':
    assert get_result('test_data/15', 10) == 26
    print(get_result('data/15', 2000000))
