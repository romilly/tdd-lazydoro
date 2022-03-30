import tdd_lazydoro.clockwatcher


def run(speed=1, alarm_time=60, duration=25):
    runner = tdd_lazydoro.clockwatcher.build()
    runner.run(speed, alarm_time, duration)


run(3, alarm_time=10, duration=5)

