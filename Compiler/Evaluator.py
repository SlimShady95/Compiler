from Compiler.Syntax.BinaryExpressionSyntax import BinaryExpressionSyntax
from Compiler.Syntax.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.NumberExpressionSyntax import NumberExpressionSyntax
from Compiler.Syntax.ParenthesizedExpressionSyntax import ParenthesizedExpressionSyntax
from Compiler.SyntaxKind import SyntaxKind

class Evaluator:
    _root = None

    def __init__(self, root: ExpressionSyntax) -> None:
        self._root = root

    def evaluate(self) -> int:
        return self._evaluate_expression(self._root)
    
    def _evaluate_expression(self, node: ExpressionSyntax) -> int:
        if isinstance(node, NumberExpressionSyntax):
            return node.get_token().get_value()
        
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