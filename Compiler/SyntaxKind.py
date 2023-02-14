from enum import Enum

class SyntaxKind(Enum):
    BAD_TOKEN = -1
    WHITESPACE_TOKEN = 0
    NUMBER_TOKEN = 1

    PLUS_TOKEN = 2
    MINUS_TOKEN = 3
    STAR_TOKEN = 4
    SLASH_TOKEN = 5

    END_OF_FILE_TOKEN = 1337