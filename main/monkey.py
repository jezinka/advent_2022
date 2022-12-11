class Monkey:
    items = []
    operation = ''
    test_condition = None
    true_monkey = None
    false_monkey = None
    items_inspected = None

    def __init__(self) -> None:
        super().__init__()
        self.items = []
        self.operation = ''
        self.test_condition = None
        self.true_monkey = None
        self.false_monkey = None
        self.items_inspected = 0

    def test(self, item):
        return item % self.test_condition == 0

    def inspects(self, old):
        return eval(self.operation)
