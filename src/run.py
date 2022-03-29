import tdd_lazydoro.runner


def run(speed=30):
    runner = tdd_lazydoro.runner.build()
    runner.run(speed)