class OptimizedLanternFish:
    def __init__(self, startingCycles) -> None:
        self.schoolOfFish = []
        for fish in startingCycles:
            self.schoolOfFish.append(int(fish))
        print(self.schoolOfFish)

    def spawn(self):
        newFish = 8
        self.schoolOfFish.append(newFish)

    def dayChange(self):
        for fish in range(len(self.schoolOfFish)):
            self.schoolOfFish[fish] -= 1
            if self.schoolOfFish[fish] < 0:
                self.schoolOfFish[fish] = 6
                self.spawn()