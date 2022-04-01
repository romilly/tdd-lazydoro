import unittest

from hamcrest import assert_that, equal_to

from tdd_lazydoro.glitch_filter import GlitchFilter


class GlitchFilterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.glitch_filter = GlitchFilter(10)

    def test_handles_constant_false_sequences(self):
        output = list(self.glitch_filter.filter(x) for x in 10*[False])
        assert_that(output, equal_to(10*[False]))

    def test_handles_constant_true_sequences(self):
        output = list(self.glitch_filter.filter(x) for x in 10*[True])
        assert_that(output, equal_to(5*[False] + 5*[True]))

    def test_handles_true_glitch(self):
        output = list(self.glitch_filter.filter(x) for x in [False, False, True, False, False, False, False])
        assert_that(output, equal_to(7*[False]))




if __name__ == '__main__':
    unittest.main()
