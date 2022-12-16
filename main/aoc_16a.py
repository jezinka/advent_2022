import copy
import re

MAX_TIME = 30


def get_result(file_name):
    graph, worth_open = prepare_file(file_name)

    result = {'max_pressure': 0}

    traverse(graph, 'AA', {}, 0, result, dict(sorted(worth_open.items(), key=lambda item: item[1], reverse=True)))
    return result['max_pressure']


def prepare_file(file_name):
    graph = {}
    worth_open = {}

    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            parsed_dict = re.search(
                "Valve (?P<node>[A-Z]{2}) has flow rate=(?P<weight>\d+); tunnel[s]? lead[s]? to valve[s]? (?P<edges>[A-Z, ]+)",
                line).groupdict()

            graph[parsed_dict['node']] = [parsed_dict['edges'].split(', '), int(parsed_dict['weight'])]
            if int(parsed_dict['weight']) > 0:
                worth_open[parsed_dict['node']] = int(parsed_dict['weight'])
    return graph, worth_open


def is_it_worth_it(ov, worth_open, time):
    potential_time = time
    potential_pressure = 0
    for v, t in ov.items():
        potential_pressure += (MAX_TIME - t) * worth_open[v]
    for valve in worth_open:
        if valve not in ov.keys():
            potential_time += 2
            if potential_time > MAX_TIME:
                break
            potential_pressure += (MAX_TIME - potential_time) * worth_open[valve]

    return potential_pressure


def traverse(graph, node, opened_valves, time, pressure_dict, worth_open):
    if len(worth_open) == len(opened_valves):
        time_out(worth_open, opened_valves, pressure_dict)
        return

    if time >= MAX_TIME:
        time_out(worth_open, opened_valves, pressure_dict)
        return

    time += 1
    for adjNode in graph[node][0]:

        if time < MAX_TIME and adjNode not in opened_valves.keys() and adjNode in worth_open.keys():
            ov = copy.deepcopy(opened_valves)
            ov[adjNode] = time + 1

            if is_it_worth_it(ov, worth_open, time) >= pressure_dict['max_pressure']:
                traverse(graph, adjNode, ov, time + 1, pressure_dict, worth_open)

        if is_it_worth_it(opened_valves, worth_open, time) >= pressure_dict['max_pressure']:
            traverse(graph, adjNode, opened_valves, time, pressure_dict, worth_open)


def time_out(worth_open, opened_valves, pressure_dict):
    sum = 0
    for k, v in opened_valves.items():
        sum += worth_open[k] * (MAX_TIME - v)
    if pressure_dict['max_pressure'] < sum:
        print(opened_valves, sum)
        pressure_dict['max_pressure'] = sum


if __name__ == '__main__':
    assert get_result('test_data/16') == 1651
    print(get_result('data/16'))
