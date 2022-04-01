from tdd_lazydoro.blinkt_adapter import BlinktAdapter
from tdd_lazydoro.blinkt_display import BlinktDisplay
from tdd_lazydoro.clockwatcher import ClockWatcher
from tdd_lazydoro.pomodoro import Pomodoro


def build(seconds=60, duration=25, break_time=5):
    display = BlinktDisplay()
    pomodoro = Pomodoro(BlinktAdapter(display), seconds=seconds, duration=duration, break_time=break_time)
    return ClockWatcher(pomodoro)


def run():
    runner = build()
    runner.run()


def demo():
    runner = build(seconds=5)
    runner.run(speed=5)

run()




