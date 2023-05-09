# função
from enum import Enum


class Elevator():
    def __init__(self):
        self.current_floor = 0
        self.door_is_open = True
        self._status = ElevatorStatus.STOPPED

    def move(self, destinations_floor):
        if self.current_floor == destinations_floor:
            self._status = ElevatorStatus.STOPPED
            self.door_is_open = True
            return
        self.door_is_open = False

        if destinations_floor > self.current_floor:
            self._status = ElevatorStatus.GOING_UP
        else:
            self._status = ElevatorStatus.GOING_DOWN

        self.current_floor = destinations_floor


class ElevatorStatus(Enum):
    STOPPED = 0
    GOING_UP = 1
    GOING_DOWN = 2
    LOCKED = 3
