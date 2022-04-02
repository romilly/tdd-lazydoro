from typing import List, Tuple

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description

from tdd_lazydoro.display import Display
from tdd_lazydoro.rangefinder import RangeFinder
from tdd_lazydoro.colors import OFF, color_map


class ColorList:
    def __init__(self, colors: List[Tuple[int, int, int]]):
        self.colors = colors

    def __getitem__(self, item: int):
        return self.colors[item]


    def __len__(self):
        return len(self.colors)

    def __repr__(self):
        return ', '.join(color_map[rgb] for rgb in self.colors if rgb is not OFF)


class ShowsOnly(BaseMatcher):
    def __init__(self, expected_colors: List[Tuple[int, int, int]]):
        self.expected_colors = ColorList(expected_colors)


    def _matches(self, display: 'MockDisplay') -> bool:
        actual_colors = ColorList(display.led_colors)
        for i in range(8):
            if i < len(self.expected_colors):
                if actual_colors[i] != self.expected_colors[i]:
                    return False
            else:
                if actual_colors[i] != OFF:
                    return False
        return True

    def describe_to(self, description: Description) -> None:
        description.append_text(repr(self.expected_colors))


def shows_only(*expected_colors: Tuple[int, int, int]):
    return ShowsOnly(list(expected_colors))


def shows_all(expected_color: Tuple[int, int, int]):
    return ShowsOnly(8*[expected_color])

class MockDisplay(Display):
    def __init__(self):
        self.led_colors = None
        self.clear_leds()
        self.buzzing = False

    def clear_leds(self):
        self.led_colors = 8*[OFF]

    def set_led(self, number, rgb):
        self.led_colors[number] = rgb
        self.buzzing = False

    def buzz(self):
        self.buzzing = True

    def __repr__(self):
        return repr(ColorList(self.led_colors))


class MockRangeFinder(RangeFinder):
    RANGE_WHEN_PERSON_PRESENT = 300
    RANGE_WHEN_PERSON_ABSENT = 8191

    def __init__(self):
        self.current_range = self.RANGE_WHEN_PERSON_ABSENT

    def range(self) -> int:
        return self.current_range

    def person_absent(self):
        self.current_range = self.RANGE_WHEN_PERSON_ABSENT

    def person_present(self):
        self.current_range = self.RANGE_WHEN_PERSON_PRESENT




