from abc import ABC, abstractmethod
from typing import Tuple


class UI(ABC):
    RED =    (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN =  (0, 255, 0)
    BLUE =   (0, 0, 255)

    @abstractmethod
    def clear_leds(self):
        pass

    @abstractmethod
    def set_led(self, number, rgb: Tuple[int]):
        pass