from enum import auto, Enum


class BoundBinaryOperatorKind(Enum):
    """
        Contains all kinds of bound binary operator kinds
    """
    ADDITION = auto()
    SUBTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()

    LOGICAL_AND = auto()
    LOGICAL_OR = auto()
