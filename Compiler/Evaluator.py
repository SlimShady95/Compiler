from Compiler.Syntax.BinaryExpressionSyntax import BinaryExpressionSyntax
from Compiler.Syntax.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.LiteralExpressionSyntax import LiteralExpressionSyntax
from Compiler.Syntax.ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from Compiler.SyntaxKind import SyntaxKind


class Evaluator:
    _root = None

    def __init__(self, root: ExpressionSyntax) -> None:
        self._root = root

    def evaluate(self) -> float:
        return self._evaluate_expression(self._root)

    def _evaluate_expression(self, node: ExpressionSyntax) -> float:
        if isinstance(node, LiteralExpressionSyntax):
            return node.get_token().get_value()

        elif isinstance(node, BinaryExpressionSyntax):
            left, operator, right = node.get_children()
            left_expression = self._evaluate_expression(left)
            right_expression = self._evaluate_expression(right)
            if operator == SyntaxKind.PLUS_TOKEN:
                return left_expression + right_expression
            elif operator == SyntaxKind.MINUS_TOKEN:
                return left_expression - right_expression
            elif operator == SyntaxKind.STAR_TOKEN:
                return left_expression * right_expression
            elif operator == SyntaxKind.SLASH_TOKEN:
                return left_expression / right_expression
            else:
                raise RuntimeError(f'Unexpected binary operator {operator}.')

        elif isinstance(node, ParenthesizedExpressionSyntax):
            return self._evaluate_expression(node.get_expression())

        raise RuntimeError(f'Unexpected node {node.get_kind()}')
