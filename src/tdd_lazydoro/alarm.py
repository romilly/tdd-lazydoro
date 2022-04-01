class Alarm:
    def __init__(self, seconds=60):
        self.seconds = seconds
        self.ticks = 0

    def tick(self):
        self.ticks += 1
        if self.ticks >= self.seconds:
            self.reset()
            return True
        return False

    def reset(self):
        self.ticks = 0
