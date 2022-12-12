import string

from aoc_12a import find_edges, dijkstra, prepare_maze, gather_path

START_MAZE = 'S'
END_MAZE = 'E'


def get_result(file_name):
    maze = prepare_maze(file_name)
    paths = []
    graph, starts, end = prepare_graph(maze)

    for start in starts:
        path, costs = dijkstra(graph, start, end)
        reversed_path = []
        gather_path(path, end, reversed_path)
        if len(reversed_path) > 1:
            reversed_path.remove(end)
            paths.append(len(reversed_path))

    return min(paths)


def prepare_graph(maze):
    letters = list(string.ascii_lowercase) + [END_MAZE]
    starts = []
    end = None
    graph = {}
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            cell_id = f"{x},{y}"
            goal = []

            if maze[x][y] == START_MAZE:
                goal = [letters[0]]
                starts.append(cell_id)
            elif maze[x][y] == END_MAZE:
                end = cell_id
            else:
                goal = letters[:letters.index(maze[x][y]) + 2]

                if maze[x][y] == 'a':
                    goal.append(START_MAZE)
                    starts.append(cell_id)
                elif maze[x][y] == 'y':
                    goal.append(END_MAZE)

            graph[cell_id] = find_edges(maze, [x, y], goal)

    return graph, starts, end


if __name__ == '__main__':
    assert get_result('test_data/12') == 29
    print(get_result('data/12'))
