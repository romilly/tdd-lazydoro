import tdd_lazydoro.runner


def run(speed=1, alarm_time=60, duration=25):
    runner = tdd_lazydoro.runner.build()
    runner.run(speed, alarm_time, duration)


run(3, alarm_time=10, duration=5)

