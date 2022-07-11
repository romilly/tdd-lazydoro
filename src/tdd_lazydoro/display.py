# abstract class
from abc import abstractmethod, ABC


class Display(ABC):
    @abstractmethod
    def clear_leds(self): #pragma: no cover
        pass

    @abstractmethod
    def set_led(self, number, rgb):  #pragma: no cover
        pass

    @abstractmethod
    def buzz(self):  #pragma: no cover
        pass
