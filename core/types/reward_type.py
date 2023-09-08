from enum import Enum


class RewardType(Enum):
    WAIT_WHEN_NO_CALLS = 10
    CLOSE_DOOR = 15
    GET_PASSENGER = 50
    DELIVER_PASSENGER = 100
    # add distance between current_level and where to go

    MOVE_BETWEEN_LEVELS = 5
    WAIT_WHEN_CALLS = 50
    OPEN_CLOSE_DOOR = 10
    OPEN_ON_EMPTY_LEVEL = 50
    MOVE_NEXT_TO_EDGE = 1000
    MOVE_WITH_OPEN_DOOR = 1000
