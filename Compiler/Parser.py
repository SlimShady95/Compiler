from Compiler.Lexer import Lexer
from Compiler.Syntax.BinaryExpressionSyntax import BinaryExpressionSyntax
from Compiler.Syntax.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.LiteralExpressionSyntax import LiteralExpressionSyntax
from Compiler.Syntax.ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from Compiler.Syntax.UnaryExpressionSyntax import UnaryExpressionSyntax
from Compiler.SyntaxFacts import SyntaxFacts
from Compiler.SyntaxKind import SyntaxKind
from Compiler.SyntaxToken import SyntaxToken
from Compiler.SyntaxTree import SyntaxTree


class Parser:
    _tokens = []
    _position = 0
    _diagnostics = []

    def __init__(self, source: str) -> None:
        self._diagnostics = []
        self._lex(source)

    def _lex(self, source: str) -> None:
        lexer = Lexer(source)
        self._tokens = []
        while True:
            token = lexer.next_token()
            if token.get_kind() not in [SyntaxKind.BAD_TOKEN, SyntaxKind.WHITESPACE_TOKEN]:
                self._tokens.append(token)

            if token.get_kind() == SyntaxKind.END_OF_FILE_TOKEN:
                break

        self._diagnostics += lexer.get_diagnostics()

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

    def _match_token(self, kind: SyntaxKind) -> SyntaxToken:
        if self._current.get_kind() == kind:
            return self._next_token()

        self._diagnostics.append(f'ERROR: Unexpected token <{self._current.get_kind()}>, expected <{kind}>')

        return SyntaxToken(kind, self._current.get_position(), '', None)

    @property
    def _current(self) -> SyntaxToken:
        return self._tokens[self._position]

    def _parse_primary_expression(self) -> ExpressionSyntax:
        current_kind = self._current.get_kind()
        if current_kind == SyntaxKind.OPEN_PARENTHESIS_TOKEN:
            left = self._next_token()
            expression = self._parse_expression()
            right = self._match_token(SyntaxKind.CLOSE_PARENTHESIS_TOKEN)

            return ParenthesizedExpressionSyntax(left, expression, right)

        elif current_kind == SyntaxKind.NUMBER_TOKEN:
            number_token = self._match_token(SyntaxKind.NUMBER_TOKEN)

            return LiteralExpressionSyntax(number_token)

        raise RuntimeError(f'Unexpected token of kind {current_kind} at position {self._position}')

    def _parse_expression(self, parent_precedence: int = 0) -> ExpressionSyntax:
        unary_operator_precedence = SyntaxFacts.get_unary_operator_precedence(self._current.get_kind())
        if unary_operator_precedence != 0 and unary_operator_precedence >= parent_precedence:
            operator_token = self._next_token()
            operand = self._parse_expression(unary_operator_precedence)

            left = UnaryExpressionSyntax(operator_token, operand)
        else:
            left = self._parse_primary_expression()

        while True:
            precedence = SyntaxFacts.get_binary_operator_precedence(self._current.get_kind())
            if precedence == 0 or precedence <= parent_precedence:
                break

            operator_token = self._next_token()
            right = self._parse_expression(precedence)
            left = BinaryExpressionSyntax(left, operator_token, right)

        return left

    def parse(self) -> SyntaxTree:
        expression = self._parse_expression()
        end_of_file_token = self._match_token(SyntaxKind.END_OF_FILE_TOKEN)

        return SyntaxTree(expression, end_of_file_token, self._diagnostics)

    def get_diagnostics(self) -> list:
        return self._diagnostics
