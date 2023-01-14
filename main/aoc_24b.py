from main.aoc_24a import prepare_maze, BFS, create_graph


def get_result(file_name):
    blizzards, walls, end_position, exp_pos = prepare_maze(file_name)
    graph_dict = create_graph(blizzards, walls)

    finish = BFS(exp_pos, end_position, graph_dict)
    start = BFS((finish, *end_position), exp_pos[1:], graph_dict)
    end = BFS((start, *exp_pos[1:]), end_position, graph_dict)
    return end


if __name__ == '__main__':
    assert get_result('test_data/24') == 54
    print(get_result('data/24'))
