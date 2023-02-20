from Compiler.Binding.BoundBinaryExpression import BoundBinaryExpression
from Compiler.Binding.BoundBinaryOperator import BoundBinaryOperator
from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundLiteralExpression import BoundLiteralExpression
from Compiler.Binding.BoundUnaryExpression import BoundUnaryExpression
from Compiler.Binding.BoundUnaryOperator import BoundUnaryOperator
from Compiler.Diagnostic.DiagnosticBag import DiagnosticBag
from Compiler.Syntax.Expression.BinaryExpressionSyntax import BinaryExpressionSyntax
from Compiler.Syntax.Expression.ExpressionSyntax import ExpressionSyntax
from Compiler.Syntax.Expression.LiteralExpressionSyntax import LiteralExpressionSyntax
from Compiler.Syntax.Expression.UnaryExpressionSyntax import UnaryExpressionSyntax
from Compiler.Syntax.SyntaxKind import SyntaxKind


class Binder:
    """
        Class handling the binding process
    """

    # A bag containing all diagnostics
    _diagnostics = None

    def __init__(self):
        """
            Sets up the diagnostic list

            :return None
        """
        self._diagnostics = DiagnosticBag()

    def bind_expression(self, syntax: ExpressionSyntax) -> BoundExpression:
        """
            Binds an expression

            :param syntax: ExpressionSyntax
                The expression to bind
            :return BoundExpression
                Returns the bound expression
        """
        syntax_kind = syntax.get_kind()
        if syntax_kind == SyntaxKind.LITERAL_EXPRESSION:
            return self._bind_literal_expression(syntax)
        elif syntax_kind == SyntaxKind.BINARY_EXPRESSION:
            return self._bind_binary_expression(syntax)
        elif syntax_kind == SyntaxKind.UNARY_EXPRESSION:
            return self._bind_unary_expression(syntax)
        elif syntax_kind == SyntaxKind.PARENTHESIZED_EXPRESSION:
            return self.bind_expression(syntax.get_children()[1])

        raise RuntimeError(f'Unexpected syntax {syntax_kind}.')

    def _bind_literal_expression(self,  syntax: LiteralExpressionSyntax):
        """
            Binds a literal expression

            :param syntax: LiteralExpressionSyntax
                The literal expression to bind
            :return BoundLiteralExpression
                Returns the bound literal expression
        """
        return BoundLiteralExpression(syntax.get_value())

    def _bind_binary_expression(self,  syntax: BinaryExpressionSyntax):
        """
            Binds a binary expression

            :param syntax: BinaryExpressionSyntax
                The binary expression to bind
            :return BoundBinaryExpression
                Returns the bound binary expression
        """
        left, operator, right = syntax.get_children()
        bound_left = self.bind_expression(left)
        bound_right = self.bind_expression(right)
        bound_operator = BoundBinaryOperator.bind(operator.get_kind(), bound_left.get_type(), bound_right.get_type())

        if bound_operator is None:
            self._diagnostics.report_undefined_binary_operator(operator.get_span(), operator.get_kind(), bound_left.get_type(), bound_right.get_type())
            return bound_left

        return BoundBinaryExpression(bound_left, bound_operator, bound_right)

    def _bind_unary_expression(self, syntax: UnaryExpressionSyntax):
        """
            Binds a unary expression

            :param syntax: UnaryExpressionSyntax
                The unary expression to bind
            :return BoundUnaryExpression
                Returns the bound unary expression
        """
        operator, operand = syntax.get_children()
        bound_operand = self.bind_expression(operand)
        bound_operator = BoundUnaryOperator.bind(operator.get_kind(), bound_operand.get_type())

        if bound_operator is None:
            self._diagnostics.report_undefined_unary_operator(operator.get_span(), operator.get_kind(), bound_operand.get_type())
            return bound_operand

        return BoundUnaryExpression(bound_operator, bound_operand)

    def get_diagnostics(self) -> DiagnosticBag:
        """
            Returns a bag containing all diagnostics

            :return DiagnosticBag
                Returns a bag containing all diagnostics
        """
        return self._diagnostics
