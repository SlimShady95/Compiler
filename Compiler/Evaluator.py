from Compiler.Syntax.Expression.BinaryExpressionSyntax import BinaryExpressionSyntax
from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.Expression.LiteralExpressionSyntax import LiteralExpressionSyntax
from Compiler.Syntax.Expression.ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from Compiler.Syntax.Expression.UnaryExpressionSyntax import UnaryExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind


class Evaluator:
    _root = None

    def __init__(self, root: ExpressionSyntax) -> None:
        self._root = root

    def evaluate(self) -> float:
        return self._evaluate_expression(self._root)

    def _evaluate_expression(self, node: ExpressionSyntax) -> float:
        if isinstance(node, LiteralExpressionSyntax):
            return node.get_token().get_value()

        elif isinstance(node, UnaryExpressionSyntax):
            operator, operand = node.get_children()
            operand_result = self._evaluate_expression(operand)
            operator_kind = operator.get_kind()

            if operator_kind == SyntaxKind.PLUS_TOKEN:
                return operand_result
            elif operator.get_kind() == SyntaxKind.MINUS_TOKEN:
                return -operand_result
            else:
                raise RuntimeError(f'Unexpected unary operator {operator_kind}.')

        elif isinstance(node, BinaryExpressionSyntax):
            left, operator, right = node.get_children()
            left_expression = self._evaluate_expression(left)
            right_expression = self._evaluate_expression(right)

            operator_kind = operator.get_kind()
            if operator_kind == SyntaxKind.PLUS_TOKEN:
                return left_expression + right_expression
            elif operator_kind == SyntaxKind.MINUS_TOKEN:
                return left_expression - right_expression
            elif operator_kind == SyntaxKind.STAR_TOKEN:
                return left_expression * right_expression
            elif operator_kind == SyntaxKind.SLASH_TOKEN:
                return left_expression / right_expression
            else:
                raise RuntimeError(f'Unexpected binary operator {operator_kind}.')

        elif isinstance(node, ParenthesizedExpressionSyntax):
            return self._evaluate_expression(node.get_expression())

        raise RuntimeError(f'Unexpected node {node.get_kind()}')
