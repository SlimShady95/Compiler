from Compiler.Binding.BoundBinaryOperatorKind import BoundBinaryOperatorKind
from Compiler.Binding.BoundUnaryOperatorKind import BoundUnaryOperatorKind
from Compiler.Diagnostic.Diagnostic import Diagnostic
from Compiler.Syntax.SyntaxKind import SyntaxKind
from Compiler.Type.TextSpan import TextSpan


class DiagnosticBag:
    """
        Contains all diagnostics
    """

    # List containing all diagnostics
    _diagnostics = []

    # The current index used for enumerating
    _current_index = -1

    def __init__(self) -> None:
        """
            Sets up an empty list for the diagnostics

            :return None
        """
        self._diagnostics = []

    def report(self, span: TextSpan, message: str) -> None:
        """
            Reports a new diagnostic

            :param span: TextSpan
                The text span of the diagnostic
            :param message: str
                The message of the diagnostic
            :return None
        """
        self._diagnostics.append(Diagnostic(span, message))

    def report_invalid_number(self, span: TextSpan, text: str, type_: object) -> None:
        """
            Reports an invalid number
            :param span: TextSpan
                The text span of the diagnostic
            :param text: str
                The invalid number
            :param type_: object
                The type the invalid number should have
            :return None
        """
        self.report(span, f'The number {text} isn\'t a valid {type_}.')

    def report_bad_character(self, position: int, character: str) -> None:
        """
            Reports a bad character

            :param position: int
                The position of the character
            :param character: str
                The character itself
            :return None
        """
        self.report(TextSpan(position, 1), f'Invalid character found: {character} at position {position}.')

    def report_unexpected_token(self, span: TextSpan, kind: SyntaxKind, expected_kind: SyntaxKind) -> None:
        """
            Reports an unexpected token

            :param span: TextSpan
                The text span of the diagnostic
            :param kind: SyntaxKind
                The given kind of syntax
            :param expected_kind: SyntaxKind
                The expected kind of syntax
            :return None
        """
        self.report(span, f'Unexpected token <{kind}>, expected <{expected_kind}>.')

    def report_undefined_binary_operator(self, span: TextSpan, operator_kind: BoundBinaryOperatorKind, left_type: object, right_type: object) -> None:
        """
            Reports an unexpected token

            :param span: TextSpan
                The text span of the diagnostic
            :param operator_kind: BoundBinaryOperatorKind
                The given binary operator kind
            :param left_type: object
                The type of the left operand
            :param right_type: object
                The type of the right operand
            :return None
        """
        self.report(span, f'Binary operator {operator_kind} is not defined for {left_type} and {right_type}.')

    def report_undefined_unary_operator(self, span: TextSpan, operator_kind: BoundUnaryOperatorKind, type_: object) -> None:
        """
            Reports an unexpected token

            :param span: TextSpan
                The text span of the diagnostic
            :param operator_kind: BoundUnaryOperatorKind
                The given unary operator kind
            :param type_: object
                The type the operand
            :return None
        """
        self.report(span, f'Unary operator {operator_kind} is not defined for {type_}.')

    def get_diagnostics(self) -> list:
        """
            Returns a list containing all diagnostics

            :return list
                Returns a list containing all diagnostics
        """
        return self._diagnostics

    def __add__(self, bag) -> 'DiagnosticBag':
        """
            Handles what happens if the diagnostic bag is added to something

            :param bag: object
                The bag to add
            :return DiagnosticBag
                Returns the altered diagnostic bag
        """
        if not isinstance(bag, DiagnosticBag):
            raise ValueError('Can only add other DiagnosticBag instances.')

        self._diagnostics += bag.get_diagnostics()

        return self

    def __iadd__(self, bag) -> 'DiagnosticBag':
        """
            Handles what happens if the diagnostic bag is added to something

            :param bag: object
                The bag to add
            :return DiagnosticBag
                Returns the altered diagnostic bag
        """
        if not isinstance(bag, DiagnosticBag):
            raise ValueError('Can only add other DiagnosticBag instances.')

        self._diagnostics += bag.get_diagnostics()

        return self

    def __iter__(self):
        """
            Returns the iter

            :return self
        """
        return self

    def __next__(self) -> Diagnostic:
        """
            Returns the next element of the list

            :return Diagnostic
                Returns the next element of the list
        """
        if self._current_index < len(self._diagnostics) - 1:
            self._current_index += 1

            return self._diagnostics[self._current_index]

        raise StopIteration

    def __len__(self) -> int:
        """
            Returns the length of the diagnostic bag

            :return int
                Returns the length of the diagnostic bag
        """
        return len(self._diagnostics)
