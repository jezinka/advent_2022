from main.aoc_8a import get_trees


def get_result(filename):
    trees = get_trees(filename)

    scenic_score = 0
    for x in range(len(trees)):
        for y in range(len(trees[x])):
            if not (y == 0 or y == len(trees[x]) - 1 or x == 0 or x == len(trees) - 1):
                visible_trees_n = 0
                visible_trees_s = 0
                visible_trees_w = 0
                visible_trees_e = 0

                considered_tree = trees[x][y]
                for i in range(x - 1, -1, -1):
                    visible_trees_n += 1
                    if trees[i][y] >= considered_tree:
                        break
                for i in range(x + 1, len(trees[x])):
                    visible_trees_s += 1
                    if trees[i][y] >= considered_tree:
                        break
                for i in range(y - 1, -1, -1):
                    visible_trees_w += 1
                    if trees[x][i] >= considered_tree:
                        break
                for i in range(y + 1, len(trees[x])):
                    visible_trees_e += 1
                    if trees[x][i] >= considered_tree:
                        break
                scenic_score = max(visible_trees_n * visible_trees_e * visible_trees_s * visible_trees_w, scenic_score)
    return scenic_score


if __name__ == '__main__':
    assert get_result('test_data/8') == 8
    print(get_result('data/8'))
