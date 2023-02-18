from Compiler.Syntax.SyntaxFacts import SyntaxFacts
from Compiler.Syntax.SyntaxToken import SyntaxToken
from Compiler.Syntax.SyntaxKind import SyntaxKind

from string import digits, whitespace


class Lexer:
    _source = ''

    _position = 0

    _diagnostics = []

    def __init__(self, source: str) -> None:
        self._source = source
        self._diagnostics = []

    def next_token(self) -> SyntaxToken:
        if self._position >= len(self._source):
            return SyntaxToken(SyntaxKind.END_OF_FILE_TOKEN, self._position, '\0', None)

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

        elif self._current.isalpha():
            start = self._position
            while self._current.isalpha():
                self._next()

            length = self._position - start
            source = self._source[start:start+length]
            kind = SyntaxFacts.get_keyword_kind(source)

            return SyntaxToken(kind, start, source, source)

        elif self._current in whitespace:
            start = self._position
            while self._current in whitespace:
                self._next()

            length = self._position - start
            source = self._source[start:start+length]

            return SyntaxToken(SyntaxKind.WHITESPACE_TOKEN, start, source, source)

        elif self._current in '+-*/()':
            token_list = {
                '+': SyntaxKind.PLUS_TOKEN, '-': SyntaxKind.MINUS_TOKEN, 
                '*': SyntaxKind.STAR_TOKEN, '/': SyntaxKind.SLASH_TOKEN,
                '(': SyntaxKind.OPEN_PARENTHESIS_TOKEN, ')': SyntaxKind.CLOSE_PARENTHESIS_TOKEN
            }

            sign = self._current
            token = token_list.get(sign)
            self._next()

            return SyntaxToken(token, self._position, sign, None)

        self._next()
        source = self._source[self._position - 1]
        self._diagnostics.append(f'ERROR: Invalid token found: {source} at position {self._position - 1}')

        return SyntaxToken(SyntaxKind.BAD_TOKEN, self._position, source, source)

    def _next(self) -> None:
        self._position += 1

    @property
    def _current(self) -> str:
        if self._position >= len(self._source):
            return '\0'

        return self._source[self._position]

    def get_diagnostics(self) -> list:
        return self._diagnostics
