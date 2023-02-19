from Compiler.Binding.BoundBinaryOperatorKind import BoundBinaryOperatorKind
from Compiler.Syntax.SyntaxKind import SyntaxKind

from typing import Optional


class BoundBinaryOperator:
    """
        Handles bound binary operators
    """
    # The kind of syntax
    _syntax_kind = None

    # The kind of operator
    _kind = None

    # The type of the left expression
    _left_type = None

    # The type of the right expression
    _right_type = None

    # The type of the result
    _result_type = None

    def __init__(self, syntax_kind: SyntaxKind, kind: BoundBinaryOperatorKind, left_type: object, right_type: object = None, result_type: object = None) -> None:
        """
            Initializes all needed properties

            :param syntax_kind: SyntaxKind
                The kind of syntax to handle
            :param kind: BoundBinaryOperatorKind
                The operator which is used
            :param left_type: object
                The type of the left expression
            :param right_type: object
                The type of the right expression
            :param result_type: object
                The type of the result
            :return None
        """
        self._syntax_kind = syntax_kind
        self._kind = kind
        self._left_type = left_type
        self._right_type = right_type if right_type is not None else left_type
        self._result_type = result_type if result_type is not None else left_type

    def get_syntax_kind(self) -> SyntaxKind:
        """
            Returns the kind of syntax used in the binding

            :return SyntaxKind
                Returns the kind of syntax used in the binding
        """
        return self._syntax_kind

    def get_kind(self) -> BoundBinaryOperatorKind:
        """
            Returns the bound operator type

            :return BoundBinaryOperatorKind
                Returns the bound operator type
        """
        return self._kind

    def get_left_type(self) -> object:
        """
            Returns the type of the left expression

            :return object
                Returns the type of the operand
        """
        return self._left_type

    def get_right_type(self) -> object:
        """
            Returns the type of the right expression

            :return object
                Returns the type of the operand
        """
        return self._right_type

    def get_result_type(self) -> object:
        """
            Returns the type of the result

            :return object
                Returns the type of the result
        """
        return self._result_type

    @staticmethod
    def get_operators() -> list:
        """
            Returns a list of all bound unary operators

            :return list
                Returns a list of all bound binray operators
        """
        return [
            # Integers
            BoundBinaryOperator(SyntaxKind.PLUS_TOKEN, BoundBinaryOperatorKind.ADDITION, int),
            BoundBinaryOperator(SyntaxKind.MINUS_TOKEN, BoundBinaryOperatorKind.SUBTRACTION, int),
            BoundBinaryOperator(SyntaxKind.STAR_TOKEN, BoundBinaryOperatorKind.MULTIPLICATION, int),
            BoundBinaryOperator(SyntaxKind.SLASH_TOKEN, BoundBinaryOperatorKind.DIVISION, int),

            # Booleans
            BoundBinaryOperator(SyntaxKind.AMPERSAND_AMPERSAND_TOKEN, BoundBinaryOperatorKind.LOGICAL_AND, bool),
            BoundBinaryOperator(SyntaxKind.PIPE_PIPE_TOKEN, BoundBinaryOperatorKind.LOGICAL_OR, bool),
        ]

    @staticmethod
    def bind(syntax_kind: SyntaxKind, left_type: object, right_type: object) -> Optional['BoundBinaryOperator']:
        """
            Binds the given syntax

            :param syntax_kind: SyntaxKind
                The syntax to bind
            :param left_type: object
                The type of the left expression
            :param right_type: object
                The type of the right expression
            :return:
                Returns an instance of a bound unary operator
        """
        for operator in BoundBinaryOperator.get_operators():
            if operator.get_syntax_kind() == syntax_kind and operator.get_left_type() == left_type and operator.get_right_type() == right_type:
                return operator

        return None
