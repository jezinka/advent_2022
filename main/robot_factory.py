class RobotFactory:
    id = None
    ore_robot_cost_ore = None
    clay_robot_cost_ore = None
    obsidian_robot_cost_ore = None
    obsidian_robot_cost_clay = None
    geode_robot_cost_ore = None
    geode_robot_cost_obsidian = None

    def __init__(self, blueprint_dict):
        self.id = int(blueprint_dict['id'])
        self.ore_robot_cost_ore = int(blueprint_dict['ore_robot_cost_ore'])
        self.clay_robot_cost_ore = int(blueprint_dict['clay_robot_cost_ore'])
        self.obsidian_robot_cost_ore = int(blueprint_dict['obsidian_robot_cost_ore'])
        self.obsidian_robot_cost_clay = int(blueprint_dict['obsidian_robot_cost_clay'])
        self.geode_robot_cost_ore = int(blueprint_dict['geode_robot_cost_ore'])
        self.geode_robot_cost_obsidian = int(blueprint_dict['geode_robot_cost_obsidian'])

    def get_max(self, resource):
        if resource == 'ore':
            return max(self.ore_robot_cost_ore, self.obsidian_robot_cost_ore, self.clay_robot_cost_ore,
                       self.geode_robot_cost_ore)
        if resource == 'clay':
            return self.obsidian_robot_cost_clay
        if resource == 'obsidian':
            return self.geode_robot_cost_obsidian

    def get_max_resource(self):
        return self.get_max('obsidian')
