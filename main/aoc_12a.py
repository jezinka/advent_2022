import string
from collections import defaultdict

START_MAZE = 'S'
END_MAZE = 'E'


def find_edges(maze, location, goal):
    edges = []
    x, y = [*location]
    for i, j in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
        if -1 < i < len(maze) and -1 < j < len(maze[i]):
            if maze[i][j] in [*goal]:
                edges.append(f"{i},{j}")
    return edges


def get_result(file_name):
    maze = prepare_maze(file_name)
    graph, start, end = prepare_graph(maze)

    path, costs = dijkstra(graph, start, end)
    reversed_path = []
    gather_path(path, end, reversed_path)
    reversed_path.remove(end)
    return len(reversed_path)


def dijkstra(graph, start, end):
    visited = set()
    parents_map = {}
    pq = []
    node_costs = defaultdict(lambda: float('inf'))
    node_costs[start] = 0
    pq.append((0, start))

    end_x, end_y = [int(n) for n in end.split(',')]
    while pq:
        _, node = pq.pop(0)
        visited.add(node)

        for adjNode in graph[node]:
            if adjNode in visited:
                continue

            node_x, node_y = [int(n) for n in adjNode.split(',')]
            weight = abs(end_x - node_x) + abs(end_y - node_y)
            new_cost = node_costs[node] + weight
            if node_costs[adjNode] > new_cost:
                parents_map[adjNode] = node
                node_costs[adjNode] = new_cost
                pq.append((new_cost, adjNode))

    return parents_map, node_costs


def gather_path(parent, j, path):
    if not (j in parent.keys()):
        path.append(j)
        return

    gather_path(parent, parent[j], path)
    path.append(j)


def prepare_graph(maze):
    letters = list(string.ascii_lowercase) + [END_MAZE]
    start = None
    end = None
    graph = {}
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == START_MAZE:
                start = f"{x},{y}"
                graph[start] = find_edges(maze, [x, y], letters[0])
            elif maze[x][y] == END_MAZE:
                end = f"{x},{y}"
                graph[end] = []
            else:
                goal = letters[:letters.index(maze[x][y]) + 2]
                if maze[x][y] == 'y':
                    goal.append(END_MAZE)
                graph[f"{x},{y}"] = find_edges(maze, [x, y], goal)
    return graph, start, end


def prepare_maze(file_name):
    maze = []
    with open(file_name) as f:
        for line in f:
            maze.append([*line.strip()])
    return maze


if __name__ == '__main__':
    assert get_result('test_data/12') == 31
    print(get_result('data/12'))
