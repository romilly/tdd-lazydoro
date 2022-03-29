from abc import ABC, abstractmethod


class Observable(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def changed(self, aspect, *args):
        for observer in self._observers:
            observer.notify(self, aspect, args)


class Observer(ABC):
    @abstractmethod
    def notify(self, observable, aspect, args):
        pass