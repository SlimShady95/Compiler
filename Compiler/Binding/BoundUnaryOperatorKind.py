from enum import auto, Enum


class BoundUnaryOperatorKind(Enum):
    """
        Contains all kinds of bound unary operators
    """
    IDENTITY = auto()
    NEGATION = auto()
    LOGICAL_NEGATION = auto()
