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


class Evaluator:
    _root = None

    def __init__(self, root: BoundExpression) -> None:
        self._root = root

    def evaluate(self) -> float:
        return self._evaluate_expression(self._root)

    def _evaluate_expression(self, node: BoundExpression) -> float:
        if isinstance(node, BoundLiteralExpression):
            return node.get_value()

        elif isinstance(node, BoundBinaryExpression):
            left, operator, right = node.get_children()
            left_expression = self._evaluate_expression(left)
            right_expression = self._evaluate_expression(right)

            if operator == BoundBinaryOperatorKind.ADDITION:
                return left_expression + right_expression
            elif operator == BoundBinaryOperatorKind.SUBTRACTION:
                return left_expression - right_expression
            elif operator == BoundBinaryOperatorKind.MULTIPLICATION:
                return left_expression * right_expression
            elif operator == BoundBinaryOperatorKind.DIVISION:
                return left_expression / right_expression
            else:
                raise RuntimeError(f'Unexpected binary operator {operator_kind}.')

        elif isinstance(node, BoundUnaryExpression):
            operator, operand = node.get_children()
            operand_result = self._evaluate_expression(operand)

            if operator == BoundUnaryOperatorKind.IDENTITY:
                return operand_result
            elif operator == BoundUnaryOperatorKind.NEGATION:
                return -operand_result
            else:
                raise RuntimeError(f'Unexpected unary operator {operator}.')

        # elif isinstance(node, ParenthesizedExpressionSyntax):
        #     return self._evaluate_expression(node.get_expression())

        raise RuntimeError(f'Unexpected node {node.get_kind()}')
