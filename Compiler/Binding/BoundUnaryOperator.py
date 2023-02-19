from Compiler.Binding.BoundUnaryOperatorKind import BoundUnaryOperatorKind
from Compiler.Syntax.SyntaxKind import SyntaxKind

from typing import Union


class BoundUnaryOperator:
    """
        Handles bound binary operators
    """
    # The kind of syntax
    _syntax_kind = None

    # The kind of operator
    _kind = None

    # The type of the operand
    _operand_type = None

    # The type of the result
    _result_type = None

    def __init__(self, syntax_kind: SyntaxKind, kind: BoundUnaryOperatorKind, operand_type: object, result_type: object = None) -> None:
        """
            Initializes all needed properties

            :param syntax_kind: SyntaxKind
                The kind of syntax to handle
            :param kind: BoundUnaryOperatorKind
                The operator which is used
            :param operand_type: object
                The type of the operand
            :param result_type: object
                The type of the result
            :return None
        """
        self._syntax_kind = syntax_kind
        self._kind = kind
        self._operand_type = operand_type
        self._result_type = result_type if result_type is not None else operand_type

    def get_syntax_kind(self) -> SyntaxKind:
        """
            Returns the kind of syntax used in the binding

            :return SyntaxKind
                Returns the kind of syntax used in the binding
        """
        return self._syntax_kind

    def get_kind(self) -> BoundUnaryOperatorKind:
        """
            Returns the bound operator type

            :return BoundUnaryOperatorKind
                Returns the bound operator type
        """
        return self._kind

    def get_operand_type(self) -> object:
        """
            Returns the type of the operand

            :return object
                Returns the type of the operand
        """
        return self._operand_type

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
                Returns a list of all bound unary operators
        """
        return [
            BoundUnaryOperator(SyntaxKind.BANG_TOKEN, BoundUnaryOperatorKind.LOGICAL_NEGATION, bool),
            BoundUnaryOperator(SyntaxKind.PLUS_TOKEN, BoundUnaryOperatorKind.IDENTITY, int),
            BoundUnaryOperator(SyntaxKind.MINUS_TOKEN, BoundUnaryOperatorKind.NEGATION, int),
        ]

    @staticmethod
    def bind(syntax_kind: SyntaxKind, operand_type: object) -> Union['BoundUnaryOperator', None]:
        """
            Binds the given syntax

            :param syntax_kind: SyntaxKind
                The syntax to bind
            :param operand_type: object
                The type of the operand
            :return:
                Returns an instance of a bound unary operator
        """
        for operator in BoundUnaryOperator.get_operators():
            if operator.get_syntax_kind() == syntax_kind and operator.get_operand_type() == operand_type:
                return operator

        return None
