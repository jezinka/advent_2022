import re


def get_result(file_name):
    folder_tree = create_folder_tree(file_name)
    results = []
    count_size(folder_tree, results)
    return sum(filter(lambda item: item < 100000, results))


def count_size(folder_tree, results):
    if isinstance(folder_tree, int):
        return folder_tree

    folder_size = 0
    for key in folder_tree.keys():
        folder_size += count_size(folder_tree[key], results)
    results.append(folder_size)
    return folder_size


def create_folder_tree(file_name):
    folder_tree = {'/': {}}
    current_tree = None
    path = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if line.startswith('$'):
                if 'cd' in line:
                    new_folder = line.removeprefix('$ cd ')
                    if new_folder != '..':
                        path.append(new_folder)
                        current_tree = get_current_tree(current_tree, folder_tree, new_folder)
                    else:
                        path.pop(-1)
                        current_tree = None
                        for p in path:
                            current_tree = get_current_tree(current_tree, folder_tree, p)

                if 'ls' in line:
                    continue
            else:
                if 'dir' in line:
                    current_tree[line.removeprefix('dir ')] = {}
                else:
                    folder = re.search("(\d+) ([\w\.]+)", line)
                    current_tree[folder.group(2)] = int(folder.group(1))
    return folder_tree


def get_current_tree(current_tree, folder_tree, new_folder):
    return folder_tree[new_folder] if current_tree is None else current_tree[new_folder]


if __name__ == '__main__':
    assert get_result('test_data/7') == 95437
    print(get_result('data/7'))
