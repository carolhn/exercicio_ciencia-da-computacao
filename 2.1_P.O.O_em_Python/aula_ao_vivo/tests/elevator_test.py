# teste
from elevator_system.elevator import Elevator, ElevatorStatus


def test_create_elevator():
    elevator = Elevator()
    assert elevator.current_floor == 0
    assert elevator.door_is_open is True
    assert elevator.status == ElevatorStatus.STOPPED


def test_move_up():
    elevator = Elevator()
    destinations_floor = 5
    elevator.move(destinations_floor)

    assert elevator.door_is_open is False
    assert elevator._status == ElevatorStatus.GOING_UP
    assert elevator.current_floor == destinations_floor


def teste_move_down():
    elevator = Elevator()
    elevator.current_floor = 5
    destinations_floor = 1
    elevator.move(destinations_floor)

    assert elevator.door_is_open is False
    assert elevator._status == ElevatorStatus.GOING_DOWN
    assert elevator.current_floor == destinations_floor


def teste_move_same():
    elevator = Elevator()
    elevator.current_floor = 5
    destinations_floor = elevator.current_floor
    elevator.move(destinations_floor)

    assert elevator._status == ElevatorStatus.STOPPED
    assert elevator.current_floor == destinations_floor
    assert elevator.door_is_open is True
