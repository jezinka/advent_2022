import math

from main.aoc_19a import get_blueprints, factory_working

MAX_TIME = 32


def get_result(file_name):
    blueprints = get_blueprints(file_name)[:3]

    blueprint_geode_results = []
    for blueprint in blueprints:
        resources = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
        robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
        time = 0
        max_resource = {'geode': 0}

        factory_working(blueprint, resources, robots, time, max_resource, '', 32)

        max_geode = max_resource['geode']
        blueprint_geode_results.append(max_geode)
        print('blueprint:', blueprint.id, ' ends with:', max_geode, ' open geodes.')

    return math.prod(blueprint_geode_results)


if __name__ == '__main__':
    # assert get_result('test_data/19') == 33
    print(get_result('data/19'))
