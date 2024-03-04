"""Runs The simulation by instantiating the A agent and a world"""

from agent import VacuumCleanerAgent
from utils.dimentions import Dimention
from world import World


class Simulation:

    def __init__(self, dim: Dimention, size: int) -> None:
        self.world = World(dim, size)

        start = Dimention(0, 0)
        self.agent = VacuumCleanerAgent(start)

    def is_done(self) -> bool:
        for self.world._map

    def main_loop(self):