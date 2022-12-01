from aoc_1a import prepare_data


def top_3_most_calorific_elves(file_name):
    prepared_elves = prepare_data(file_name)
    return sum(list(map(lambda e: prepared_elves[e], sorted(prepared_elves, key=prepared_elves.get, reverse=True)))[:3])


if __name__ == '__main__':
    assert top_3_most_calorific_elves('test_data/1') == 45000
    print(top_3_most_calorific_elves('data/1'))
