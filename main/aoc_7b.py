from aoc_7a import create_folder_tree, count_size

TOTAL_SPACE = 70000000
FREE_NEEDED = 30000000


def get_result(file_name):
    folder_tree = create_folder_tree(file_name)
    results = []
    count_size(folder_tree, results)
    searching = FREE_NEEDED - (TOTAL_SPACE - max(results))
    return min(filter(lambda item: item > searching, results))


if __name__ == '__main__':
    assert get_result('test_data/7') == 24933642
    print(get_result('data/7'))
