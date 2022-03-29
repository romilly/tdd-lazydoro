from tdd_lazydoro.display import Display


class Pomodoro:
    TIME_ELAPSED = 'Time elapsed'
    WAITING = 'Waiting'
    WORKING = 'Working'
    WORKING_TICK = 'Working tick'
    BREAK_DUE = 'Should start a break'
    ON_BREAK = 'On a break'
    BREAK_TICK = 'Break tick'
    BREAK_OVER = 'Break time over'

    def __init__(self, display: Display, duration=25):
        self.display = display
        self.minute_timer = 0
        self.duration = duration
        self.break_time = 5
        self.state = self.WAITING

    def minute_has_passed(self): # a minute has passed
        print('tock %d' % self.minute_timer)
        if self.state == self.WORKING:
            self.minute_timer += 1
            if self.minute_timer >= self.duration:
                self.break_due()
            if 0 ==self.minute_timer % 3:
                self.display.set_led(min(7, self.minute_timer // 3), Display.BLUE)
        elif self.state == self.ON_BREAK:
            self.minute_timer += 1
            if self.minute_timer == 5:
                for i in range(8):
                    self.display.set_led(i, Display.YELLOW)
                self.display.buzz()
            else:
                self.display.set_led(self.minute_timer, Display.GREEN)

    def person_arrives(self):
        print('person arrives')
        if self.state in [self.WAITING, self.ON_BREAK]:
            self.start_working()

    def person_leaves(self):
        print('person leaves')

        if self.state == self.WORKING:
            self.start_waiting()
        elif self.state == self.BREAK_DUE:
            self.start_break()

    def start_working(self):
        self.state = self.WORKING
        self.minute_timer = 0
        self.display.clear_leds()
        self.display.set_led(0, Display.BLUE)

    def break_due(self):
        self.state = self.BREAK_DUE
        for i in range(8):
            self.display.set_led(i, Display.RED)

    def start_waiting(self):
        self.state = self.WAITING
        self.display.clear_leds()

    def start_break(self):
        self.state = self.ON_BREAK
        self.minute_timer = 0
        self.display.clear_leds()
        self.display.set_led(0, Display.GREEN)

