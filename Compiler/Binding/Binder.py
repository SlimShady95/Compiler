from Compiler.Binding.BoundBinaryExpression import BoundBinaryExpression
from Compiler.Binding.BoundBinaryOperator import BoundBinaryOperator
from Compiler.Binding.BoundBinaryOperatorKind import BoundBinaryOperatorKind
from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundLiteralExpression import BoundLiteralExpression
from Compiler.Binding.BoundUnaryExpression import BoundUnaryExpression
from Compiler.Binding.BoundUnaryOperator import BoundUnaryOperator
from Compiler.Binding.BoundUnaryOperatorKind import BoundUnaryOperatorKind
from Compiler.Syntax.Expression.BinaryExpressionSyntax import BinaryExpressionSyntax
from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.Expression.LiteralExpressionSyntax import LiteralExpressionSyntax
from Compiler.Syntax.Expression.UnaryExpressionSyntax import UnaryExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind

from typing import Optional


class Binder:
    """

    """
    _diagnostics = []

    def __init__(self):
        self._diagnostics = []

    def bind_expression(self, syntax: ExpressionSyntax) -> BoundExpression:
        syntax_kind = syntax.get_kind()
        if syntax_kind == SyntaxKind.LITERAL_EXPRESSION:
            return self._bind_literal_expression(syntax)
        elif syntax_kind == SyntaxKind.BINARY_EXPRESSION:
            return self._bind_binary_expression(syntax)
        elif syntax_kind == SyntaxKind.UNARY_EXPRESSION:
            return self._bind_unary_expression(syntax)

        raise RuntimeError(f'Unexpected syntax {syntax_kind}.')

    def _bind_literal_expression(self,  syntax: LiteralExpressionSyntax):
        return BoundLiteralExpression(syntax.get_value())

    def _bind_binary_expression(self,  syntax: BinaryExpressionSyntax):
        left, operator, right = syntax.get_children()
        bound_left = self.bind_expression(left)
        bound_right = self.bind_expression(right)
        bound_operator = BoundBinaryOperator.bind(operator.get_kind(), bound_left.get_type(), bound_right.get_type())

        if bound_operator is None:
            self._diagnostics.append(f'Binary operator {operator.get_kind()} is not defined for types {bound_left.get_type()}/{bound_right.get_type()}.')
            return bound_left

        return BoundBinaryExpression(bound_left, bound_operator, bound_right)

    def _bind_unary_expression(self,  syntax: UnaryExpressionSyntax):
        operator, operand = syntax.get_children()
        bound_operand = self.bind_expression(operand)
        bound_operator = BoundUnaryOperator.bind(operator.get_kind(), bound_operand.get_type())

        if bound_operator is None:
            self._diagnostics.append(f'Unary operator {operator.get_kind()} is not defined for type {bound_operand.get_type()}.')
            return bound_operand

        return BoundUnaryExpression(bound_operator, bound_operand)

    def get_diagnostics(self) -> list:
        return self._diagnostics
