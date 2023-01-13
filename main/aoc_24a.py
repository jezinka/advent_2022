import itertools


def get_result(file_name):
    blizzards, walls, end_position, exp_pos = prepare_maze(file_name)

    graph_dict = {}

    steps = 0
    blizzard_cycle = False
    while not blizzard_cycle:
        potential_steps = [(steps, *n[:]) for n in get_nodes(blizzards_move(blizzards, steps), walls)]
        # print(potential_steps)
        if len(graph_dict) > 0 and [(n[1], n[2]) for n in list(graph_dict.values())[0]] == [(n[1], n[2]) for n in
                                                                                            potential_steps]:
            blizzard_cycle = True
        else:
            graph_dict[steps] = potential_steps
        steps += 1
    print('------------------------------------------')
    return BFS(exp_pos, end_position, graph_dict)


def get_neighbour_nodes(node, nodes, blizzard_cycle):
    time = node[0] + 1
    if time > MAX_X * MAX_Y:
        return []

    potential_nodes = [(time, pot_node[1], pot_node[2]) for pot_node in nodes[time % blizzard_cycle]]
    intersection_nodes = list({(time, node[1], node[2]), (time, node[1] + 1, node[2]), (time, node[1] - 1, node[2]),
                               (time, node[1], node[2] + 1), (time, node[1], node[2] - 1)} & set(potential_nodes))
    return intersection_nodes


def prepare_maze(file_name):
    exp_pos = None
    end_position = None
    blizzards = []
    walls = []
    global MAX_X, MAX_Y
    MAX_X, MAX_Y = 0, 0
    with open(file_name, 'r') as f:
        for x, line in enumerate(f):
            line = line.strip()
            MAX_X = max(MAX_X, x)
            for y, tile in enumerate([*line]):
                if x == 0 and tile == '.':
                    exp_pos = (0, x, y)
                if tile == '.':
                    end_position = (x, y)
                elif tile == '#':
                    walls.append((x, y))
                elif tile in ['>', '<', '^', 'v']:
                    blizzards.append({'dir': tile, 'pos': (x, y)})
                MAX_Y = max(y, MAX_Y)
    return blizzards, walls, end_position, exp_pos


def blizzards_move(blizzards, steps):
    blizzards_set = []
    for blizzard in blizzards:
        x, y = blizzard['pos']
        direction = blizzard['dir']
        new_pos = None

        if direction == '^':
            new_pos = (((x - 1 - steps) % (MAX_X - 1)) + 1, y)

        elif direction == 'v':
            new_pos = (((x - 1 + steps) % (MAX_X - 1)) + 1, y)

        elif direction == '>':
            new_pos = (x, ((y - 1 + steps) % (MAX_Y - 1)) + 1)

        elif direction == '<':
            new_pos = (x, ((y - 1 - steps) % (MAX_Y - 1)) + 1)

        if new_pos not in blizzards_set:
            blizzards_set.append(new_pos)
    return blizzards_set


def get_nodes(blizzards, walls):
    return sorted(
        set([(x, y) for x, y in itertools.product(range(MAX_X + 1), range(MAX_Y + 1))]) - set(walls) - set(blizzards))


def BFS(start, end, graph_dict):
    blizzard_cycle = len(graph_dict)

    # Mark all the vertices as not visited
    visited = []

    # Create a queue for BFS
    queue = []

    # Mark the source node as
    # visited and enqueue it
    queue.append(start)
    visited.append(start)

    steps_needed = None

    while queue and steps_needed is None:

        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)

        if s[1:] == end:
            print(s[0])
            steps_needed = s[0]

        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in [nn for nn in get_neighbour_nodes(s, graph_dict, blizzard_cycle) if nn not in visited]:
            queue.append(i)
            visited.append(i)
    return steps_needed


if __name__ == '__main__':
    assert get_result('test_data/24') == 18
    print(get_result('data/24'))
