from Compiler.Syntax.Lexer import Lexer
from Compiler.Syntax.Expression.BinaryExpressionSyntax import BinaryExpressionSyntax
from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.Expression.LiteralExpressionSyntax import LiteralExpressionSyntax
from Compiler.Syntax.Expression.ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from Compiler.Syntax.Expression.UnaryExpressionSyntax import UnaryExpressionSyntax
from Compiler.Syntax.SyntaxFacts import SyntaxFacts
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Syntax.SyntaxToken import SyntaxToken
from Compiler.Syntax.SyntaxTree import SyntaxTree


class Parser:
    """
        Parses the given tokens
    """

    # List containing all tokens
    _tokens = []

    # The current position at which token the parser is at
    _position = 0

    # List containing all diagnostic for the current parsing
    _diagnostics = []

    def __init__(self, source: str) -> None:
        """
            Starts the lexing process

            :param source: string
                The source code to parse
            :return None
        """
        self._diagnostics = []
        self._lex(source)

    def _lex(self, source: str) -> None:
        """
            Lexes the given source code

            :param source: string
                The source code to lex
            :return None
        """
        lexer = Lexer(source)
        self._tokens = []
        while True:
            # Remove bad tokens and whitespace tokens
            token = lexer.next_token()
            if token.get_kind() not in [SyntaxKind.BAD_TOKEN, SyntaxKind.WHITESPACE_TOKEN]:
                self._tokens.append(token)

            # Break out if we hit the EOF token
            if token.get_kind() == SyntaxKind.END_OF_FILE_TOKEN:
                break

        self._diagnostics += lexer.get_diagnostics()

    def _peek(self, offset: int) -> SyntaxToken:
        """
            Looks the given amount of tokens ahead

            :param offset: int
                The offset to look ahead
            :return SyntaxToken
                Returns the syntax token at the offset position
        """
        index = self._position + offset
        tokens_length = len(self._tokens)
        if index >= tokens_length:
            return self._tokens[tokens_length - 1]

        return self._tokens[index]

    def _next_token(self) -> SyntaxToken:
        """
            Returns the next token

            :return SyntaxToken
                Returns the next token in the list
        """
        current = self._current
        self._position += 1

        return current

    def _match_token(self, kind: SyntaxKind) -> SyntaxToken:
        """
            Checks if the current token matches the given one, and if so return the next token. Otherwise throw an error
            and return a token of the given kind.

            :param kind:
            :return SyntaxToken
                 Returns either the next token if the current token matches the given kind, otherwise return a token of
                 the given kind.
        """
        if self._current.get_kind() == kind:
            return self._next_token()

        self._diagnostics.append(f'ERROR: Unexpected token <{self._current.get_kind()}>, expected <{kind}>')

        return SyntaxToken(kind, self._current.get_position(), '', None)

    @property
    def _current(self) -> SyntaxToken:
        """
            Returns the current token

            :return SyntaxToken
                Returns the current token.
        """
        return self._tokens[self._position]

    def _parse_primary_expression(self) -> ExpressionSyntax:
        """
            Parses a primary expression

            :return ExpressionSyntax
                Returns a subtype of ExpressionSyntax which matches the kind of the current token
        """
        current_kind = self._current.get_kind()

        # Parenthesized expression
        if current_kind == SyntaxKind.OPEN_PARENTHESIS_TOKEN:
            left = self._next_token()
            expression = self._parse_expression()
            right = self._match_token(SyntaxKind.CLOSE_PARENTHESIS_TOKEN)

            return ParenthesizedExpressionSyntax(left, expression, right)

        # true/false keywords
        elif current_kind in [SyntaxKind.TRUE_KEYWORD, SyntaxKind.FALSE_KEYWORD]:
            key_word_token = self._next_token()
            value = key_word_token.get_kind() == SyntaxKind.TRUE_KEYWORD

            return LiteralExpressionSyntax(key_word_token, value)

        # Number
        elif current_kind == SyntaxKind.NUMBER_TOKEN:
            number_token = self._match_token(SyntaxKind.NUMBER_TOKEN)

            return LiteralExpressionSyntax(number_token)

        raise RuntimeError(f'Unexpected token of kind {current_kind} at position {self._position}')

    def _parse_expression(self, parent_precedence: int = 0) -> ExpressionSyntax:
        """
            Parses an expression

            :param parent_precedence: int
                The precedence of the parent node
            :return ExpressionSyntax
                Returns the parsed expression syntax
        """
        # If there is an unary operator, parse it first
        unary_operator_precedence = SyntaxFacts.get_unary_operator_precedence(self._current.get_kind())
        if unary_operator_precedence != 0 and unary_operator_precedence >= parent_precedence:
            operator_token = self._next_token()
            operand = self._parse_expression(unary_operator_precedence)

            left = UnaryExpressionSyntax(operator_token, operand)
        else:
            left = self._parse_primary_expression()

        # Parse the child expressions recursively and in the correct order
        while True:
            precedence = SyntaxFacts.get_binary_operator_precedence(self._current.get_kind())
            if precedence == 0 or precedence <= parent_precedence:
                break

            operator_token = self._next_token()
            right = self._parse_expression(precedence)
            left = BinaryExpressionSyntax(left, operator_token, right)

        return left

    def parse(self) -> SyntaxTree:
        """
            Parses the root expression

            :return SyntaxTree
                Returns the syntax tree of the whole expression
        """
        expression = self._parse_expression()
        end_of_file_token = self._match_token(SyntaxKind.END_OF_FILE_TOKEN)

        return SyntaxTree(expression, end_of_file_token, self._diagnostics)

    def get_diagnostics(self) -> list:
        """
            Returns a list with all diagnostics

            :return list
                Returns a list with all diagnostics
        """
        return self._diagnostics
