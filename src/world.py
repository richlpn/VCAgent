"""Implements the World for the simulation"""
from dataclasses import dataclass
from enum import Enum
from functools import reduce
from random import choice
import numpy as np


from utils.dimentions import Dimention


class LocalStatus(Enum):
    DIRTY = 0
    CLEAN = 1


class Local:
    coord: Dimention
    status: LocalStatus
    neighbors: list['Local']

    def __init__(self, dim: Dimention, neighbors: list['Local'] = [], status: LocalStatus = LocalStatus.CLEAN) -> None:
        self.coord = dim
        self.status = status

        if len(neighbors) > 4:
            raise Exception('A local cant have more the 4 Neighbors')

        self.neighbors = neighbors

    def __str__(self) -> str:
        if self.status == LocalStatus.CLEAN:
            return ' '
        return "*"

    def __eq__(self, __value: object) -> bool:
        if type(__value) != type(self):
            return False

        return self.coord == __value.coord and self.status == __value.coord


class World:
    _map: list[Local]
    _dim: Dimention

    def __init__(self, dim: Dimention | tuple[int, int], local_size: int) -> None:
        self._dim = dim if type(dim) == Dimention else Dimention(*dim)

        self._map = []

    def __init_map__(self, size: int):
        for y in range(0, self._dim.y, size):
            for x in range(0, self._dim.x, size):
                coords = Dimention(x, y)
                self._map.append(Local(coords))

        # Set neighbors
        neighbors_locations = np.array([
            [0, -size],
            [0, size],
            [-size, 0],
        ])
        for local in self._map:
            for neighbor_location in neighbors_locations:
                neighbor_location = local.coord + neighbor_location

                if (neighbor_location > self._dim).any():
                    continue
                local.neighbors.append(self.get_local(neighbor_location))

    def __str__(self) -> str:

        return reduce(lambda ant, val: ant + str(val) + "|", self._map, '|')

    def get_local(self, dim: Dimention) -> Local:
        locals = list(filter(lambda local: local.coord == dim, self._map))

        if len(locals) == 0:
            raise Exception("The informed coordinates aren't valid")

        return locals[0]
