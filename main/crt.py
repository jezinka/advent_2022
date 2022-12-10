class Crt:
    registerx = None
    cycle_no = None
    results = None
    crt_row = None

    lines = None
    dark_pixel = None
    observed_cycle = [x for x in range(20, 240, 40)]

    def __init__(self, dark_pixel) -> None:
        super().__init__()
        self.registerx = 1
        self.cycle_no = 0
        self.results = []
        self.crt_row = ''
        self.lines = 0
        self.dark_pixel = dark_pixel

    def check_cycle(self):
        sprite_positions = list(range(self.registerx - 1, self.registerx + 2))
        if ((self.cycle_no - 1) % 40) in sprite_positions:
            self.crt_row += '#'
        else:
            self.crt_row += self.dark_pixel

        if len(self.crt_row) == 40:
            print(self.crt_row)
            self.lines += 1
            self.crt_row = ''

        if self.cycle_no in self.observed_cycle:
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

    def drawn_lines(self):
        return self.lines
