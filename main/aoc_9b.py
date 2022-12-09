import copy


def get_result(file_name, show_preview):
    with open(file_name) as f:
        h = [15, 15]
        tail = [copy.deepcopy(h) for i in range(9)]
        visited_places = [','.join(map(str, tail[-1]))]

        if show_preview: print_result(h, tail)

        for line in f:
            line = line.strip()

            if show_preview: print(line)

            direction = line[0]
            steps = int(line[1:].strip())

            for i in range(steps):
                if direction == 'R':
                    h[0] += 1
                elif direction == 'L':
                    h[0] -= 1
                elif direction == 'U':
                    h[1] -= 1
                elif direction == 'D':
                    h[1] += 1

                for j, t in enumerate(tail):
                    previous_knot = h if j == 0 else tail[j - 1]
                    if not (t[0] in range(previous_knot[0] - 1, previous_knot[0] + 2) and
                            t[1] in range(previous_knot[1] - 1, previous_knot[1] + 2)) and t[1] != previous_knot[1] and \
                            t[0] != previous_knot[0]:
                        t[0] = move(previous_knot[0], t[0])
                        t[1] = move(previous_knot[1], t[1])
                    elif abs(t[0] - previous_knot[0]) > 1:
                        t[0] = move(previous_knot[0], t[0])
                    elif abs(t[1] - previous_knot[1]) > 1:
                        t[1] = move(previous_knot[1], t[1])

                if show_preview: print_result(h, tail)

                visited_places.append(','.join(map(str, tail[-1])))

    return len(set(visited_places))


def move(h, t):
    if t < h:
        t += 1
    else:
        t -= 1
    return t


def print_result(h, tail):
    for y in range(30):
        row = ''
        for x in range(30):
            item = None
            if h[0] == x and h[1] == y:
                item = 'H'

            if item is None:
                for i, t in enumerate(tail):
                    if t[0] == x and t[1] == y:
                        item = str(i + 1)
                        break

            if item is None:
                item = '.'
            row += item
        print(row)
    print()


if __name__ == '__main__':
    assert get_result('test_data/9', True) == 1
    assert get_result('test_data/9_2', True) == 36
    print(get_result('data/9', False))
