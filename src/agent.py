""" Implements the Agents"""

# TODO: Implement the Vacuum cleaner Agent
# TODO: Method that checks if a place at the world is dirty or not
# TODO: Move In the World
# TODO: Save the moves history

from utils.dimentions import Dimention


class VacuumCleanerAgent:
    history: list[Dimention]
    current_postion: Dimention

    def __init__(self, start_postion: Dimention):
        self.current_postion = Dimention(*start_postion)
        self.history = [self.current_postion]

    def is_clean(self, feature: int) -> bool:
        return feature != 0

    def move(self, pos: Dimention):
        self.current_postion = pos
        self.history.append(pos)
