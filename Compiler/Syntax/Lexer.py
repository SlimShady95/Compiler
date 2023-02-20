from Compiler.Diagnostic.DiagnosticBag import DiagnosticBag
from Compiler.Syntax.SyntaxFacts import SyntaxFacts
from Compiler.Syntax.SyntaxToken import SyntaxToken
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Type.TextSpan import TextSpan

from string import digits, whitespace


class Lexer:
    """
        The lexer takes the source code and turns it into tokens
    """

    # Contains the whole source code
    _source = ''

    # The position the lexer is at currently
    _position = 0

    # A bag containing all diagnostics
    _diagnostics = None

    def __init__(self, source: str) -> None:
        """
            Initializes certain properties

            :param source: string
                The source which should get tokenized
            :return None
        """
        self._source = source
        self._diagnostics = DiagnosticBag()

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
                self._diagnostics.report_invalid_number(TextSpan(start, length), source, int)

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
        elif self._current in '+-*/%()!&|=':
            token_list = {
                '+':  SyntaxKind.PLUS_TOKEN,                '-':  SyntaxKind.MINUS_TOKEN,
                '*':  SyntaxKind.STAR_TOKEN,                '**': SyntaxKind.STAR_STAR_TOKEN,
                '/':  SyntaxKind.SLASH_TOKEN,               '(':  SyntaxKind.OPEN_PARENTHESIS_TOKEN,
                ')':  SyntaxKind.CLOSE_PARENTHESIS_TOKEN,   '!':  SyntaxKind.BANG_TOKEN,
                '%':  SyntaxKind.PERCENT_TOKEN,             '&':  SyntaxKind.AMPERSAND_TOKEN,
                '|':  SyntaxKind.PIPE_TOKEN,                '&&': SyntaxKind.AMPERSAND_AMPERSAND_TOKEN,
                '||': SyntaxKind.PIPE_PIPE_TOKEN,           '==': SyntaxKind.EQUALS_EQUALS_TOKEN,
                '!=': SyntaxKind.BANG_EQUALS_TOKEN,
            }

            sign = self._current
            lookahead = self._lookahead
            combined_sign = sign + lookahead
            if combined_sign in token_list.keys():
                self._next(2)
                return SyntaxToken(token_list.get(combined_sign), self._position - 2, combined_sign, None)

            self._next()

            return SyntaxToken(token_list.get(sign), self._position - 1, sign, None)

        # Found a bad token here
        self._next()
        position = self._position - 1
        source = self._source[position]
        self._diagnostics.report_bad_character(position, source)

        return SyntaxToken(SyntaxKind.BAD_TOKEN, position, source, source)

    def _next(self, increment: int = 1) -> None:
        """
            Increments the current position by the given number

            :param increment: int
                The amount of times the position should be incremented
            :return None
        """
        self._position += increment

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

    def get_diagnostics(self) -> DiagnosticBag:
        """
            Returns the diagnostic bag

            :return list
                Returns the diagnostic bag
        """
        return self._diagnostics
