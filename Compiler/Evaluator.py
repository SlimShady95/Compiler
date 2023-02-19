from Compiler.Binding.BoundUnaryExpression import BoundUnaryExpression
from Compiler.Binding.BoundBinaryExpression import BoundBinaryExpression
from Compiler.Binding.BoundLiteralExpression import BoundLiteralExpression
from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundUnaryOperatorKind import BoundUnaryOperatorKind
from Compiler.Binding.BoundBinaryOperatorKind import BoundBinaryOperatorKind
from Compiler.Syntax.Expression.BinaryExpressionSyntax import BinaryExpressionSyntax
from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.Expression.LiteralExpressionSyntax import LiteralExpressionSyntax
from Compiler.Syntax.Expression.ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from Compiler.Syntax.Expression.UnaryExpressionSyntax import UnaryExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind

from typing import Union


class Evaluator:
    """
        Evaluates the given bound expression
    """
    # The root node
    _root = None

    def __init__(self, root: BoundExpression) -> None:
        """
            Sets the root node

            :param root: BoundExpression
                The bound expression which should be evaluated
            :return None
        """
        self._root = root

    def evaluate(self) -> Union[object, float]:
        """
            Evaluates the previously set bound expression

            :return Union[object, float]
                Returns whatever the bound expression returns
        """
        return self._evaluate_expression(self._root)

    def _evaluate_expression(self, node: BoundExpression) -> Union[object, float]:
        """
            Evaluates the given bound expression

            :param node: BoundExpression
                The node which should be evaluated
            :return Union[object, float]
                Returns whatever the bound expression returns
        """
        # If the given expression is any literal just return its value
        if isinstance(node, BoundLiteralExpression):
            return node.get_value()

        # If its a binary expression, evaluate the result of the operation
        elif isinstance(node, BoundBinaryExpression):
            left, operator, right = node.get_children()
            left_expression = self._evaluate_expression(left)
            right_expression = self._evaluate_expression(right)

            # Mathematical operations
            operator_kind = operator.get_kind()
            if operator_kind == BoundBinaryOperatorKind.ADDITION:
                return int(left_expression) + int(right_expression)
            elif operator_kind == BoundBinaryOperatorKind.SUBTRACTION:
                return int(left_expression) - int(right_expression)
            elif operator_kind == BoundBinaryOperatorKind.MULTIPLICATION:
                return int(left_expression) * int(right_expression)
            elif operator_kind == BoundBinaryOperatorKind.DIVISION:
                return int(left_expression) / int(right_expression)

            # Binary operations
            elif operator_kind == BoundBinaryOperatorKind.LOGICAL_AND:
                return bool(left_expression) and bool(right_expression)
            elif operator_kind == BoundBinaryOperatorKind.LOGICAL_OR:
                return bool(left_expression) or bool(right_expression)

            raise RuntimeError(f'Unexpected binary operator {operator_kind}.')

        # If its an unary expression, evaluate the new value of the operand and return it
        elif isinstance(node, BoundUnaryExpression):
            operator, operand = node.get_children()
            operand_result = self._evaluate_expression(operand)

            operator_kind = operator.get_kind()
            if operator_kind == BoundUnaryOperatorKind.IDENTITY:
                return int(operand_result)
            elif operator_kind == BoundUnaryOperatorKind.NEGATION:
                return -int(operand_result)
            elif operator_kind == BoundUnaryOperatorKind.LOGICAL_NEGATION:
                return not bool(operand_result)

            raise RuntimeError(f'Unexpected unary operator {operator_kind}.')

        # elif isinstance(node, ParenthesizedExpressionSyntax):
        #     return self._evaluate_expression(node.get_expression())

        raise RuntimeError(f'Unexpected node {node.get_kind()}')
