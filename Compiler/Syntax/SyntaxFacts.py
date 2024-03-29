from Compiler.Syntax.SyntaxKind import SyntaxKind


class SyntaxFacts:
    """
        Contains helper functions related to the syntax of the compiler.
    """
    # List with precedences of binary operators
    binary_operators_precedence = {
        SyntaxKind.STAR_TOKEN:                5,
        SyntaxKind.SLASH_TOKEN:               5,
        SyntaxKind.STAR_STAR_TOKEN:           5,
        SyntaxKind.PERCENT_TOKEN:             5,
        SyntaxKind.PLUS_TOKEN:                4,
        SyntaxKind.MINUS_TOKEN:               4,
        SyntaxKind.BANG_EQUALS_TOKEN:         3,
        SyntaxKind.EQUALS_EQUALS_TOKEN:       3,
        SyntaxKind.AMPERSAND_AMPERSAND_TOKEN: 2,
        SyntaxKind.PIPE_PIPE_TOKEN:           1,
    }

    # List with precedences of unary operators
    unary_operators_precedence = {
        SyntaxKind.PLUS_TOKEN:  6,
        SyntaxKind.MINUS_TOKEN: 6,
        SyntaxKind.BANG_TOKEN:  6,
    }

    @staticmethod
    def get_binary_operator_precedence(kind: SyntaxKind) -> int:
        """
            Returns the precedence of the given binary operator kind

            :param kind: SyntaxKind
                The token kind where the precedence is requested
            :return int
                Returns the precedence of the given token kind
        """
        return SyntaxFacts.binary_operators_precedence.get(kind, 0)

    @staticmethod
    def get_unary_operator_precedence(kind: SyntaxKind) -> int:
        """
            Returns the precedence of the given unary operator kind

            :param kind: SyntaxKind
                The token kind where the precedence is requested
            :return int
                Returns the precedence of the given token kind
        """
        return SyntaxFacts.unary_operators_precedence.get(kind, 0)

    @staticmethod
    def get_keyword_kind(text: str) -> SyntaxKind:
        """
            Returns either a the kind of a keyword or, if the given text is no keyword, an identifier token

            :param text: string
                The text to check
            :return
                Returns either a the kind of a keyword or, if the given text is no keyword, an identifier token
        """
        if text == 'true':
            return SyntaxKind.TRUE_KEYWORD
        elif text == 'false':
            return SyntaxKind.FALSE_KEYWORD

        return SyntaxKind.IDENTIFIER_TOKEN
