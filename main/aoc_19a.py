import copy
import re

from main.robot_factory import RobotFactory


def get_result(file_name):
    blueprints = get_blueprints(file_name)

    blueprint_geode_results = []
    for blueprint in blueprints:
        resources = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
        robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
        time = 0
        max_resource = {'geode': 0}

        factory_working(blueprint, resources, robots, time, max_resource, '', 24)

        max_geode = max_resource['geode']
        blueprint_geode_results.append(blueprint.id * max_geode)
        print('blueprint:', blueprint.id, ' ends with:', max_geode, ' open geodes.')

    return sum(blueprint_geode_results)


def get_blueprints(file_name):
    blueprints = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            blueprint = re.search(
                "Blueprint (?P<id>\d+): Each ore robot costs (?P<ore_robot_cost_ore>\d+) ore. Each clay robot costs (?P<clay_robot_cost_ore>\d+) ore. Each obsidian robot costs (?P<obsidian_robot_cost_ore>\d+) ore and (?P<obsidian_robot_cost_clay>\d+) clay. Each geode robot costs (?P<geode_robot_cost_ore>\d+) ore and (?P<geode_robot_cost_obsidian>\d+) obsidian\.",
                line)
            blueprints.append(RobotFactory(blueprint.groupdict()))
    return blueprints


def factory_working(blueprint, resources, robots, time, max_resource, log, max_time, what_was_skipped=None):
    if what_was_skipped is None:
        what_was_skipped = set()

    if time >= max_time:
        time_out(log, max_resource, resources)
        return

    time += 1
    time_left = max_time - time
    log += f"{time}: "

    what_can_be_build, should_save_up = get_what_can_be_build(blueprint, resources, robots, time_left)

    for can_afford in what_can_be_build:
        if 'ore' not in what_was_skipped and can_afford == 'ore':
            scenario_log, scenario_resources, scenario_robots = build_ore_robot(blueprint, log, resources, robots)
            factory_working(blueprint, scenario_resources, scenario_robots, time, max_resource, scenario_log, max_time)
        elif 'clay' not in what_was_skipped and can_afford == 'clay':
            scenario_log, scenario_resources, scenario_robots = build_clay_robot(blueprint, log, resources, robots)
            factory_working(blueprint, scenario_resources, scenario_robots, time, max_resource, scenario_log, max_time)
        elif 'obsidian' not in what_was_skipped and can_afford == 'obsidian':
            scenario_log, scenario_resources, scenario_robots = build_obsidian_robot(blueprint, log, resources, robots)
            factory_working(blueprint, scenario_resources, scenario_robots, time, max_resource, scenario_log, max_time)
        elif 'geode' not in what_was_skipped and can_afford == 'geode':
            scenario_log, scenario_resources, scenario_robots = build_geode_robot(blueprint, log, resources, robots)
            factory_working(blueprint, scenario_resources, scenario_robots, time, max_resource, scenario_log, max_time)
        elif can_afford == 'nothing':
            what_was_skipped = list(set(what_can_be_build) - {'nothing'})
            scenario_log, scenario_resources, scenario_robots = build_nothing(log, resources, robots)
            factory_working(blueprint, scenario_resources, scenario_robots, time, max_resource, scenario_log, max_time,
                            what_was_skipped)

    if robots['geode'] > 0 and time_left > 0:
        resources['geode'] += (robots['geode'] * time_left)

    return time_out(log, max_resource, resources)


def time_out(log, max_resource, resources):
    if resources['geode'] > max_resource['geode']:
        print(log)
        print('open geodes:', resources['geode'])
        max_resource['geode'] = resources['geode']


def build_nothing(log, resources, robots):
    scenario_resources = copy.deepcopy(resources)
    scenario_robots = copy.deepcopy(robots)
    scenario_log = copy.deepcopy(log)
    scenario_log += " nothing was build \n"
    for robot, quantity in robots.items():
        scenario_resources[robot] += quantity
    return scenario_log, scenario_resources, scenario_robots


def build_geode_robot(blueprint, log, resources, robots):
    scenario_log = copy.deepcopy(log)
    scenario_log += " build geode robot \n"
    scenario_resources = copy.deepcopy(resources)
    scenario_robots = copy.deepcopy(robots)
    bought_geode_robot(blueprint, scenario_resources, scenario_robots)
    for robot, quantity in robots.items():
        scenario_resources[robot] += quantity
    return scenario_log, scenario_resources, scenario_robots


def build_obsidian_robot(blueprint, log, resources, robots):
    scenario_log = copy.deepcopy(log)
    scenario_log += " build obsidian robot\n"
    scenario_resources = copy.deepcopy(resources)
    scenario_robots = copy.deepcopy(robots)
    bought_obsidian_robot(blueprint, scenario_resources, scenario_robots)
    for robot, quantity in robots.items():
        scenario_resources[robot] += quantity
    return scenario_log, scenario_resources, scenario_robots


def build_clay_robot(blueprint, log, resources, robots):
    scenario_log = copy.deepcopy(log)
    scenario_log += " build clay robot\n"
    scenario_resources = copy.deepcopy(resources)
    scenario_robots = copy.deepcopy(robots)
    bought_clay_robot(blueprint, scenario_resources, scenario_robots)
    for robot, quantity in robots.items():
        scenario_resources[robot] += quantity
    return scenario_log, scenario_resources, scenario_robots


def build_ore_robot(blueprint, log, resources, robots):
    scenario_log = copy.deepcopy(log)
    scenario_log += " build ore robot\n"
    scenario_resources = copy.deepcopy(resources)
    scenario_robots = copy.deepcopy(robots)
    bought_ore_robot(blueprint, scenario_resources, scenario_robots)
    for robot, quantity in robots.items():
        scenario_resources[robot] += quantity
    return scenario_log, scenario_resources, scenario_robots


def get_what_can_be_build(blueprint, resources, robots, time_left):
    if time_left == 0:
        return ['nothing'], False

    what_can_be_build = []
    need_save_up = False

    if can_afford_geode_robot(blueprint, resources):
        what_can_be_build.append('geode')

    if do_i_need_it(blueprint, robots, 'obsidian'):
        if can_afford_obsidian_robot(blueprint, resources):
            what_can_be_build.append('obsidian')
        else:
            need_save_up = True

    if do_i_need_it(blueprint, robots, 'clay'):
        if can_afford_clay_robot(blueprint, resources):
            what_can_be_build.append('clay')
        else:
            need_save_up = True

    if do_i_need_it(blueprint, robots, 'ore'):
        if can_afford_ore_robot(blueprint, resources):
            what_can_be_build.append('ore')
        else:
            need_save_up = True

    if time_left == 1:
        if 'geode' in what_can_be_build:
            return ['geode'], False
        return ['nothing'], False

    if need_save_up:
        what_can_be_build.append('nothing')

    return what_can_be_build, need_save_up


def do_i_need_it(blueprint, robots, resource):
    return blueprint.get_max(resource) > robots[resource]


def bought_ore_robot(blueprint, scenario_resources, scenario_robots):
    scenario_resources['ore'] -= blueprint.ore_robot_cost_ore
    scenario_robots['ore'] += 1


def bought_clay_robot(blueprint, scenario_resources, scenario_robots):
    scenario_resources['ore'] -= blueprint.clay_robot_cost_ore
    scenario_robots['clay'] += 1


def bought_obsidian_robot(blueprint, scenario_resources, scenario_robots):
    scenario_resources['ore'] -= blueprint.obsidian_robot_cost_ore
    scenario_resources['clay'] -= blueprint.obsidian_robot_cost_clay
    scenario_robots['obsidian'] += 1


def bought_geode_robot(blueprint, scenario_resources, scenario_robots):
    scenario_resources['obsidian'] -= blueprint.geode_robot_cost_obsidian
    scenario_resources['ore'] -= blueprint.geode_robot_cost_ore
    scenario_robots['geode'] += 1


def can_afford_obsidian_robot(blueprint, resources):
    return blueprint.obsidian_robot_cost_ore <= resources['ore'] and blueprint.obsidian_robot_cost_clay <= resources[
        'clay']


def can_afford_geode_robot(blueprint, resources):
    return blueprint.geode_robot_cost_obsidian <= resources['obsidian'] and blueprint.geode_robot_cost_ore <= resources[
        'ore']


def can_afford_clay_robot(blueprint, resources):
    return blueprint.clay_robot_cost_ore <= resources['ore']


def can_afford_ore_robot(blueprint, resources):
    return blueprint.ore_robot_cost_ore <= resources['ore']


if __name__ == '__main__':
    assert get_result('test_data/19') == 33
    print(get_result('data/19'))
