from Compiler.Lexer import Lexer
from Compiler.Syntax.BinaryExpressionSyntax import BinaryExpressionSyntax
from Compiler.Syntax.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.NumberExpressionSyntax import NumberExpressionSyntax
from Compiler.SyntaxKind import SyntaxKind
from Compiler.SyntaxToken import SyntaxToken

class Parser:
    _lexer = None
    _tokens = []

    _position = 0

    def __init__(self, text: str) -> None:
        self._lexer = Lexer(text)
        
        while True:
            token = self._lexer.next_token()
            if token.get_kind() not in [SyntaxKind.BAD_TOKEN, SyntaxKind.WHITESPACE_TOKEN]:
                self._tokens.append(token)

            if token.get_kind() == SyntaxKind.END_OF_FILE_TOKEN:
                break

    def _peek(self, offset: int) -> SyntaxToken:
        index = self._position + offset
        tokens_length = len(self._tokens)
        if index >= tokens_length:
            return self._tokens[tokens_length - 1]

        return self._tokens[index]

    def _next_token(self) -> SyntaxToken:
        current = self._current
        self._position += 1

        return current

    def _match(self, kind: SyntaxKind) -> SyntaxToken:
        if self._current.get_kind() == kind:
            return self._next_token()

        return SyntaxToken(kind, self._current._position, None, None)

    @property
    def _current(self) -> SyntaxToken:
        return self._tokens[self._position]

    def _parse_primary_expression(self):
        number_token = self._match(SyntaxKind.NUMBER_TOKEN)

        return NumberExpressionSyntax(number_token)

    def parse(self) -> ExpressionSyntax:
        left = self._parse_primary_expression()
        while self._current.get_kind() in [SyntaxKind.PLUS_TOKEN, SyntaxKind.MINUS_TOKEN]:
            operator_token = self._next_token()
            right = self._parse_primary_expression()
            left = BinaryExpressionSyntax(left, operator_token, right)

        return left
