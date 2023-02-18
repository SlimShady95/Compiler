from Compiler.Syntax.SyntaxFacts import SyntaxFacts
from Compiler.Syntax.SyntaxToken import SyntaxToken
from Compiler.Syntax.SyntaxKind import SyntaxKind

from string import digits, whitespace


class Lexer:
    """
        The lexer takes the source code and turns it into tokens
    """

    # Contains the whole source code
    _source = ''

    # The position the lexer is at currently
    _position = 0

    # A list containing all diagnostics
    _diagnostics = []

    def __init__(self, source: str) -> None:
        """
            Initializes certain properties

            :param source: string
                The source which should get tokenized
            :return None
        """
        self._source = source
        self._diagnostics = []

    def next_token(self) -> SyntaxToken:
        """
            Detects the next token and returns it

            :return SyntaxToken
                Returns the next syntax token
        """

        # Reached end of file here, so return end of file token
        if self._position >= len(self._source):
            return SyntaxToken(SyntaxKind.END_OF_FILE_TOKEN, self._position, '\0', None)

        # Handle numbers
        if self._current in digits:
            start = self._position
            while self._current in digits:
                self._next()

            length = self._position - start
            source = self._source[start:start+length]
            value = None
            try:
                value = int(source)
            except ValueError:
                self._diagnostics.append(f'The number {source} can not be represented by INT32.')

            return SyntaxToken(SyntaxKind.NUMBER_TOKEN, start, source, value)

        # Handle alpha characters/keywords
        elif self._current.isalpha():
            start = self._position
            while self._current.isalpha():
                self._next()

            length = self._position - start
            source = self._source[start:start+length]
            kind = SyntaxFacts.get_keyword_kind(source)

            return SyntaxToken(kind, start, source, source)

        # Handle whitespaces
        elif self._current in whitespace:
            start = self._position
            while self._current in whitespace:
                self._next()

            length = self._position - start
            source = self._source[start:start+length]

            return SyntaxToken(SyntaxKind.WHITESPACE_TOKEN, start, source, source)

        # Handle operators
        elif self._current in '+-*/()!&|':
            token_list = {
                '+':  SyntaxKind.PLUS_TOKEN,             '-':  SyntaxKind.MINUS_TOKEN,
                '*':  SyntaxKind.STAR_TOKEN,             '/':  SyntaxKind.SLASH_TOKEN,
                '(':  SyntaxKind.OPEN_PARENTHESIS_TOKEN, ')':  SyntaxKind.CLOSE_PARENTHESIS_TOKEN,
                '!':  SyntaxKind.BANG_TOKEN,             '&':  SyntaxKind.AMPERSAND_TOKEN,
                '|':  SyntaxKind.PIPE_TOKEN,             '&&': SyntaxKind.AMPERSAND_AMPERSAND_TOKEN,
                '||': SyntaxKind.PIPE_PIPE_TOKEN,
            }

            sign = self._current
            token = token_list.get(sign)
            if sign in '&|':
                if self._lookahead == sign:
                    self._next()
                    sign = 2 * sign
                    token = token_list.get(sign)

            self._next()

            return SyntaxToken(token, self._position, sign, None)

        # Found a bad token here
        self._next()
        source = self._source[self._position - 1]
        self._diagnostics.append(f'ERROR: Invalid token found: {source} at position {self._position - 1}')

        return SyntaxToken(SyntaxKind.BAD_TOKEN, self._position, source, source)

    def _next(self) -> None:
        """
            Increments the current position by one

            :return None
        """
        self._position += 1

    @property
    def _current(self) -> str:
        """
            Returns the current char

            :return string
                Returns the current character
        """
        return self._peek(0)

    @property
    def _lookahead(self) -> str:
        """
            Looks one character ahead

            :return string
                Returns the next character
        """
        return self._peek(1)

    def _peek(self, offset) -> str:
        """
            Takes a peek at the given offset

            :param offset: int
                The offset of the current position
            :return string
                Returns the character at the given offset
        """
        index = self._position + offset
        if index >= len(self._source):
            return '\0'

        return self._source[index]

    def get_diagnostics(self) -> list:
        """
            Returns the list of diagnostics

            :return list
                Returns all diagnostics in a list
        """
        return self._diagnostics
