import random
from abc import ABCMeta, abstractmethod
from typing import Mapping
from typing import Iterable

from .random_variable import DRV


class AbstractMagicLamp(metaclass=ABCMeta):
    @abstractmethod
    def get_experience(self) -> int:
        raise NotImplementedError()


class BaseMagicLamp(AbstractMagicLamp, DRV[int]):
    PROBABILITIES = {}

    @property
    def probabilities(self) -> Mapping[int, float]:
        return self.PROBABILITIES

    def get_experience(self) -> int:
        return random.choices(
            population=list(self.PROBABILITIES.keys()),
            weights=list(self.PROBABILITIES.values()),
            k=1,
        )[0]


class UsualMagicLamp(BaseMagicLamp):
    PROBABILITIES = {
        5000000: 0.26,
        10000000: 0.71,
        30000000: 0.02,
        100000000: 0.01,
    }


class ExtendedMagicLamp(BaseMagicLamp):
    PROBABILITIES = {
        1200000000: 0.01,
        360000000: 0.02,
        120000000: 0.69,
        60000000: 0.28,
    }


class AbstractMagicLampService(metaclass=ABCMeta):
    @abstractmethod
    def calculate_average_experience(self, lamps: Iterable[AbstractMagicLamp]) -> int:
        raise NotImplementedError()


class MagicLampService(AbstractMagicLampService):
    def calculate_average_experience(self, lamps: Iterable[AbstractMagicLamp]) -> int:
        return sum(lamp.get_experience() for lamp in lamps)
