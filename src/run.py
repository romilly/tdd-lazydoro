import tdd_lazydoro.runner


def run(speed=1):
    runner = tdd_lazydoro.runner.build()
    runner.run(speed)

run(30)