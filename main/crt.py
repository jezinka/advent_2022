class Crt:
    registerx = 1
    cycle_no = 0
    results = []
    observed_cycle = [x for x in range(20, 240, 40)]

    def __init__(self) -> None:
        super().__init__()
        self.registerx = 1
        self.cycle_no = 0
        self.results = []

    def check_cycle(self):
        if self.cycle_no in self.observed_cycle:
            print(self.cycle_no, ': ', self.registerx)
            self.results.append(self.get_signal_strength())

    def addx(self, value):
        for i in range(2):
            self.cycle_no += 1
            self.check_cycle()

        self.registerx += value

    def noop(self):
        self.cycle_no += 1
        self.check_cycle()

    def get_signal_strength(self):
        return self.cycle_no * self.registerx

    def parse_instruction(self, line):
        if line.startswith('addx'):
            operation, value = line.strip().split(' ')
            self.addx(int(value))
        if line.startswith('noop'):
            self.noop()
