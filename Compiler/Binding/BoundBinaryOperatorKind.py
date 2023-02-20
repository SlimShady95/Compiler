from enum import auto, Enum


class BoundBinaryOperatorKind(Enum):
    """
        Contains all kinds of bound binary operator kinds
    """
    # Calculations
    ADDITION = auto()
    SUBTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()
    MODULO = auto()

    # Logical stuff
    LOGICAL_AND = auto()
    LOGICAL_OR = auto()
    EQUALS = auto()
    NOT_EQUALS = auto()
