import copy
import re

from main.robot_factory import RobotFactory


def get_result(file_name):
    blueprints = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            blueprint = re.search(
                "Blueprint (?P<id>\d+): Each ore robot costs (?P<ore_robot_cost>\d+) ore. Each clay robot costs (?P<clay_robot_cost>\d+) ore. Each obsidian robot costs (?P<obsidian_robot_cost_ore>\d+) ore and (?P<obsidian_robot_cost_clay>\d+) clay. Each geode robot costs (?P<geode_robot_cost_ore>\d+) ore and (?P<geode_robot_cost_obsidian>\d+) obsidian\.",
                line)
            blueprints.append(RobotFactory(blueprint.groupdict()))

    blueprint_geode_results = []
    for blueprint in blueprints:
        resources = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
        robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
        time = 0
        max_resource = {'geode': 0}

        factory_working(blueprint, resources, robots, time, max_resource, '')

        max_geode = max_resource['geode']
        blueprint_geode_results.append(blueprint.id * max_geode)
        print('blueprint:', blueprint.id, ' ends with:', max_geode, ' open geodes.')

    return sum(blueprint_geode_results)


def factory_working(blueprint, resources, robots, time, max_resource, log):
    if time >= 24:
        if resources['geode'] > max_resource['geode']:
            print(log)
            print('open geodes:', resources['geode'])
            max_resource['geode'] = resources['geode']
        return

    time += 1
    log += f"{time}: "

    what_can_be_build = []
    if can_afford_geode_robot(blueprint, resources):
        what_can_be_build.append('geode')
    if can_afford_obsidian_robot(blueprint, resources):
        what_can_be_build.append('obsidian')
    if can_afford_clay_robot(blueprint, resources):
        what_can_be_build.append('clay')
    if can_afford_ore_robot(blueprint, resources):
        what_can_be_build.append('ore')
    what_can_be_build.append('nothing')

    for can_afford in what_can_be_build:
        if can_afford == 'ore':
            scenario_log = copy.deepcopy(log)
            scenario_log += " build ore robot\n"
            scenario_resources = copy.deepcopy(resources)
            scenario_robots = copy.deepcopy(robots)
            bought_ore_robot(blueprint, scenario_resources, scenario_robots)
            for robot, quantity in robots.items():
                scenario_resources[robot] += quantity
            if is_it_worth_it(scenario_robots, scenario_resources, time, blueprint, max_resource):
                factory_working(blueprint, scenario_resources, scenario_robots, time, max_resource, scenario_log)
        elif can_afford == 'clay':
            scenario_log = copy.deepcopy(log)
            scenario_log += " build clay robot\n"
            scenario_resources = copy.deepcopy(resources)
            scenario_robots = copy.deepcopy(robots)
            bought_clay_robot(blueprint, scenario_resources, scenario_robots)
            for robot, quantity in robots.items():
                scenario_resources[robot] += quantity
            if is_it_worth_it(scenario_robots, scenario_resources, time, blueprint, max_resource):
                factory_working(blueprint, scenario_resources, scenario_robots, time, max_resource, scenario_log)
        elif can_afford == 'obsidian':
            scenario_log = copy.deepcopy(log)
            scenario_log += " build obsidian robot\n"
            scenario_resources = copy.deepcopy(resources)
            scenario_robots = copy.deepcopy(robots)
            bought_obsidian_robot(blueprint, scenario_resources, scenario_robots)
            for robot, quantity in robots.items():
                scenario_resources[robot] += quantity
            if is_it_worth_it(scenario_robots, scenario_resources, time, blueprint, max_resource):
                factory_working(blueprint, scenario_resources, scenario_robots, time, max_resource, scenario_log)
        elif can_afford == 'geode':
            scenario_log = copy.deepcopy(log)
            scenario_log += " build geode robot \n"
            scenario_resources = copy.deepcopy(resources)
            scenario_robots = copy.deepcopy(robots)
            bought_geode_robot(blueprint, scenario_resources, scenario_robots)
            for robot, quantity in robots.items():
                scenario_resources[robot] += quantity
            if is_it_worth_it(scenario_robots, scenario_resources, time, blueprint, max_resource):
                factory_working(blueprint, scenario_resources, scenario_robots, time, max_resource, scenario_log)
        else:
            scenario_resources = copy.deepcopy(resources)
            scenario_robots = copy.deepcopy(robots)
            for robot, quantity in robots.items():
                scenario_resources[robot] += quantity
            if is_it_worth_it(scenario_robots, scenario_resources, time, blueprint, max_resource):
                scenario_log = copy.deepcopy(log)
                scenario_log += " nothing was build \n"
                factory_working(blueprint, scenario_resources, scenario_robots, time, max_resource,
                                scenario_log)


def bought_ore_robot(blueprint, scenario_resources, scenario_robots):
    scenario_resources['ore'] -= blueprint.ore_robot_cost
    scenario_robots['ore'] += 1


def bought_clay_robot(blueprint, scenario_resources, scenario_robots):
    scenario_resources['ore'] -= blueprint.clay_robot_cost
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
    return blueprint.clay_robot_cost <= resources['ore']


def can_afford_ore_robot(blueprint, resources):
    return blueprint.ore_robot_cost <= resources['ore']


def is_it_worth_it(robots, resources, time, blueprint, max_resource):
    return (24 - time) * max(1, robots['geode']) > max_resource['geode']


if __name__ == '__main__':
    assert get_result('test_data/19') == 33
    print(get_result('data/19'))
