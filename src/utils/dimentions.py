"""Implements a dimention class"""
from typing import NamedTuple
import numpy as np


class Dimention:
    _coords: np.ndarray

    def __init__(self, x: int, y: int) -> None:
        self._coords = np.ndarray([x, y], dtype=np.int16)

    def __eq__(self, __value: object) -> bool:
        if not type(__value) == type(self):
            return False

        return (self == __value.x) and (self.y == self.y)

    @property
    def x(self) -> int:
        return self._coords[0]

    @property
    def y(self) -> int:
        return self._coords[1]

    def __add__(self, other: 'Dimention') -> np.ndarray:
        return self._coords + other._coords

    def __gt__(self, other: 'Dimention') -> np.ndarray:
        return self._coords > other._coords

    def __lt__(self, other: 'Dimention') -> np.ndarray:
        return self._coords < other._coords
