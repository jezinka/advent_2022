def get_result(file_name, show_preview):
    with open(file_name) as f:
        h_x, h_y = 0, 4
        t_x, t_y = 0, 4
        visited_places = [','.join(map(str, [t_x, t_y]))]

        if show_preview: print_result(h_x, h_y, t_x, t_y)

        for line in f:
            line = line.strip()

            if show_preview: print(line)

            direction = line[0]
            steps = int(line[1:].strip())

            for i in range(steps):
                if direction == 'R':
                    h_x += 1
                elif direction == 'L':
                    h_x -= 1
                elif direction == 'U':
                    h_y -= 1
                elif direction == 'D':
                    h_y += 1

                if not (t_x in range(h_x - 1, h_x + 2) and
                        t_y in range(h_y - 1, h_y + 2)) and t_y != h_y and t_x != h_x:
                    t_x = move(h_x, t_x)
                    t_y = move(h_y, t_y)
                elif abs(t_x - h_x) > 1:
                    t_x = move(h_x, t_x)
                elif abs(t_y - h_y) > 1:
                    t_y = move(h_y, t_y)

                if show_preview: print_result(h_x, h_y, t_x, t_y)

                visited_places.append(','.join(map(str, [t_x, t_y])))

    return len(set(visited_places))


def move(h, t):
    if t < h:
        t += 1
    else:
        t -= 1
    return t


def print_result(h_x, h_y, t_x, t_y):
    for y in range(5):
        row = ''
        for x in range(6):
            if h_x == x and h_y == y:
                row += 'H'
            elif t_x == x and t_y == y:
                row += 'T'
            else:
                row += '.'
        print(row)
    print()


if __name__ == '__main__':
    assert get_result('test_data/9', True) == 13
    print(get_result('data/9', False))
