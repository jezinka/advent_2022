def get_result(filename):
    trees = get_trees(filename)

    visible_trees = 0
    for x in range(len(trees)):
        for y in range(len(trees[x])):
            if y == 0 or y == len(trees[x]) - 1 or x == 0 or x == len(trees) - 1:
                visible_trees += 1
            else:
                neighbour_trees_n = -1
                neighbour_trees_s = -1
                neighbour_trees_w = -1
                neighbour_trees_e = -1
                for i in range(0, x):
                    neighbour_trees_n = max(trees[i][y], neighbour_trees_n)
                for i in range(x + 1, len(trees[i])):
                    neighbour_trees_s = max(trees[i][y], neighbour_trees_s)
                for i in range(0, y):
                    neighbour_trees_w = max(trees[x][i], neighbour_trees_w)
                for i in range(y + 1, len(trees[x])):
                    neighbour_trees_e = max(trees[x][i], neighbour_trees_e)
                if (neighbour_trees_n < trees[x][y] or neighbour_trees_s < trees[x][y] or
                        neighbour_trees_w < trees[x][y] or neighbour_trees_e < trees[x][y]):
                    visible_trees += 1

    return visible_trees


def get_trees(filename):
    with open(filename, 'r') as f:
        trees = []
        for line in f:
            trees.append(list(map(lambda tree: int(tree), [*line.strip()])))
    return trees


if __name__ == '__main__':
    assert get_result('test_data/8') == 21
    print(get_result('data/8'))
