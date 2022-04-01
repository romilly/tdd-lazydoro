"""
Filter out suspect values from a time sequence of boolean values.

Each time you send it a value, it adds it to a list of recent values and returns the majority verdict.
An occasional change will be ignored but a persistent change will be passed on.
"""


class GlitchFilter:
    def __init__(self, period=11):
        self.period = period
        self.history = period*[False] # when lazydoro is powered up, assume no-one is there

    def filter(self, value: bool) -> bool:
        self.history.append(value)
        self.history.pop(0)
        return sum(self.history) > self.period / 2
