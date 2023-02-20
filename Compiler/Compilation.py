from Compiler.Binding.Binder import Binder
from Compiler.EvaluationResult import EvaluationResult
from Compiler.Evaluator import Evaluator
from Compiler.Syntax.SyntaxTree import SyntaxTree


class Compilation:
    """
        Wrapper class for the binding and evaluation process
    """

    # The syntax tree which should be evaluated
    _syntax = None

    def __init__(self, syntax: SyntaxTree) -> None:
        """
            Sets the syntax tree

            :param syntax: SyntaxTree
                The syntax tree which should be evaluated
            :return None
        """
        self._syntax = syntax

    def evaluate(self) -> EvaluationResult:
        """
            Evaluates the syntax tree

            :return EvaluationResult
                Returns an evaluation result container which contains the value and the diagnostics
        """
        binder = Binder()
        bound_expression = binder.bind_expression(self._syntax.get_root())
        evaluator = Evaluator(bound_expression)
        value = evaluator.evaluate()
        diagnostics = self._syntax.get_diagnostics() + binder.get_diagnostics()

        if len(diagnostics):
            return EvaluationResult(None, diagnostics)

        return EvaluationResult(value, [])
