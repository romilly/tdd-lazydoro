from abc import ABC, abstractmethod
from typing import Tuple


class Display(ABC):
    @abstractmethod
    def clear_leds(self): #pragma: no cover
        pass

    @abstractmethod
    def set_led(self, number, rgb: Tuple[int]):  #pragma: no cover
        pass

    @abstractmethod
    def buzz(self):  #pragma: no cover
        pass

