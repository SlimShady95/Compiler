from Compiler.Binding.BoundAssignmentExpression import BoundAssignmentExpression
from Compiler.Binding.BoundUnaryExpression import BoundUnaryExpression
from Compiler.Binding.BoundBinaryExpression import BoundBinaryExpression
from Compiler.Binding.BoundLiteralExpression import BoundLiteralExpression
from Compiler.Binding.BoundExpression import BoundExpression
from Compiler.Binding.BoundUnaryOperatorKind import BoundUnaryOperatorKind
from Compiler.Binding.BoundBinaryOperatorKind import BoundBinaryOperatorKind

from typing import Union

from Compiler.Binding.BoundVariableExpression import BoundVariableExpression


class Evaluator:
    """
        Evaluates the given bound expression
    """

    # The root node
    _root = None

    # A dictionary containing all variables
    _variables = None

    def __init__(self, root: BoundExpression, variables: dict) -> None:
        """
            Sets the root node

            :param root: BoundExpression
                The bound expression which should be evaluated
            :param variables: dict
                A dictionary containing all variables
            :return None
        """
        self._root = root
        self._variables = variables

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

        # If it is a variable, just return its value
        elif isinstance(node, BoundVariableExpression):
            return self._variables.get(node.get_children()[0])

        # If its an assignment, set the variable in the internal storage
        elif isinstance(node, BoundAssignmentExpression):
            value = self._evaluate_expression(node.get_children()[0])
            self._variables[node.get_children()[0]] = value

            return value

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
            elif operator_kind == BoundBinaryOperatorKind.MODULO:
                return int(left_expression) % int(right_expression)
            elif operator_kind == BoundBinaryOperatorKind.POWER:
                return int(left_expression) ** int(right_expression)

            # Binary operations
            elif operator_kind == BoundBinaryOperatorKind.LOGICAL_AND:
                return bool(left_expression) and bool(right_expression)
            elif operator_kind == BoundBinaryOperatorKind.LOGICAL_OR:
                return bool(left_expression) or bool(right_expression)

            # Comparison operations
            elif operator_kind == BoundBinaryOperatorKind.EQUALS:
                return left_expression == right_expression
            elif operator_kind == BoundBinaryOperatorKind.NOT_EQUALS:
                return left_expression != right_expression

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

        raise RuntimeError(f'Unexpected node {node.get_kind()}')
