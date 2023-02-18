from enum import auto, Enum


class BoundNodeKind(Enum):
    """
        Contains all kinds of bound expressions
    """
    BINARY_EXPRESSION = auto()
    UNARY_EXPRESSION = auto()
    LITERAL_EXPRESSION = auto()
