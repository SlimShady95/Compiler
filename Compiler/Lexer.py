from Compiler.SyntaxToken import SyntaxToken
from Compiler.SyntaxKind import SyntaxKind

from string import digits, whitespace

class Lexer:
    _text = ''

    _position = 0

    _diagnostics = []

    def __init__(self, text: str) -> None:
        self._text = text

    def next_token(self) -> SyntaxToken:
        if self._position >= len(self._text):
            return SyntaxToken(SyntaxKind.END_OF_FILE_TOKEN, self._position, '\0', None)

        if self._current in digits:
            start = self._position
            while self._current in digits:
                self._next()

            length = self._position - start
            text = self._text[start:start+length]

            return SyntaxToken(SyntaxKind.NUMBER_TOKEN, start, text, int(text))

        elif self._current in whitespace:
            start = self._position
            while self._current in whitespace:
                self._next()

            length = self._position - start
            text = self._text[start:start+length]

            return SyntaxToken(SyntaxKind.WHITESPACE_TOKEN, start, text, text)

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
        text = self._text[self._position - 1]
        self._diagnostics.append(f'ERROR: Invalid token found: {text} at position {self._position - 1}')

        return SyntaxToken(SyntaxKind.BAD_TOKEN, self._position, text, text)

    def _next(self) -> None:
        self._position += 1

    @property
    def _current(self) -> str:
        if (self._position >= len(self._text)):
            return '\0'

        return self._text[self._position]

    def get_diagnostics(self) -> list:
        return self._diagnostics
