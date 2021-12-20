class lanternfish:
    def __init__(self, cycle) -> None:
        self.cycle = cycle

    def spawn(self):
        newFish = lanternfish(9)
        return newFish

    def dayChange(self):
        self.cycle -= 1
        if self.cycle < 0:
            self.cycle = 6
            return self.spawn()
        else:
            return False