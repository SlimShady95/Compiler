from enum import auto, Enum


class SyntaxKind(Enum):
    """
        Contains all kinds of syntax the compiler knows

        There are three categories:

        - Token
        - Keywords
        - Expressions
    """

    """
        Tokens
    """
    # Special tokens
    BAD_TOKEN = auto()
    WHITESPACE_TOKEN = auto()
    END_OF_FILE_TOKEN = auto()

    # "Valued" tokens
    NUMBER_TOKEN = auto()
    IDENTIFIER_TOKEN = auto()

    # Operator tokens
    PLUS_TOKEN = auto()
    MINUS_TOKEN = auto()
    STAR_TOKEN = auto()
    SLASH_TOKEN = auto()
    BANG_TOKEN = auto()
    OPEN_PARENTHESIS_TOKEN = auto()
    CLOSE_PARENTHESIS_TOKEN = auto()

    # Comparison operator tokens
    EQUALS_TOKEN = auto()
    EQUALS_EQUALS_TOKEN = auto()
    BANG_EQUALS_TOKEN = auto()
    AMPERSAND_TOKEN = auto()
    AMPERSAND_AMPERSAND_TOKEN = auto()
    PIPE_TOKEN = auto()
    PIPE_PIPE_TOKEN = auto()

    """
         Keywords
    """
    TRUE_KEYWORD = auto()
    FALSE_KEYWORD = auto()

    """
        Expressions
    """
    LITERAL_EXPRESSION = auto()
    UNARY_EXPRESSION = auto()
    BINARY_EXPRESSION = auto()
    PARENTHESIZED_EXPRESSION = auto()
