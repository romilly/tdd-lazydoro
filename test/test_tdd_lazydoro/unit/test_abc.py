import unittest

from tdd_lazydoro.pico.mp.abc import ABC, abstractmethod, AbstractMethodException


class AbstractClass(ABC):
    def ok_method(self):
        pass

    @abstractmethod
    def should_be_subclassed(self):
        pass


class ConcreteClass(AbstractClass):
    def should_be_subclassed(self):
        pass


class ABCTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.abstract = AbstractClass()
        self.concrete = ConcreteClass()

    def test_ordinary_methods_can_be_called(self):
        self.abstract.ok_method()

    def test_subclass_must_implement_abstract_method(self):
        self.assertRaises(AbstractMethodException, self.abstract.should_be_subclassed)

    def test_subclassed_methods_are_ok_to_call(self):
        self.concrete.should_be_subclassed()


if __name__ == '__main__':
    unittest.main()
