from enum import Enum


class BoundNodeKind(Enum):
    BINARY_EXPRESSION = 1
    UNARY_EXPRESSION = 2
    LITERAL_EXPRESSION = 3