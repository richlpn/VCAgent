"""Implements a dimention class"""
from typing import NamedTuple


class Dimention(NamedTuple):
    x: int
    y: int

    def __eq__(self, __value: object) -> bool:
        if not type(__value) == type(self):
            return False

        return (self.x == __value.x) and (self.y == self.y)
