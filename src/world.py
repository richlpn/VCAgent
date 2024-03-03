"""Implements the World for the simulation"""
from dataclasses import dataclass
from enum import Enum
from functools import reduce
from random import choice

from utils.dimentions import Dimention


class LocalStatus(Enum):
    DIRTY = 0
    CLEAN = 1


class Local:
    coord: Dimention
    status: LocalStatus

    def __init__(self, dim: Dimention | tuple[int, int], status: LocalStatus = LocalStatus.CLEAN) -> None:
        self.coord = Dimention(*dim)
        self.status = status

    def __str__(self) -> str:
        if self.status == LocalStatus.CLEAN:
            return ' '
        return "*"


class World:
    _map: list[Local]
    _dim: Dimention

    def __init__(self, dim: Dimention | tuple[int, int], local_size: int) -> None:
        self._dim = dim if type(dim) == Dimention else Dimention(*dim)
        self._map = [Local((0, x), LocalStatus(choice([0, 1])))
                     for x in range(0, self._dim.x, local_size)]

    def __str__(self) -> str:

        return reduce(lambda ant, val: ant + str(val) + "|", self._map, '|')
