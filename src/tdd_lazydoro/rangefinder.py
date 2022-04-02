from abc import ABC, abstractmethod


class RangeFinder(ABC):
    @abstractmethod
    def range(self) -> int:
        pass




