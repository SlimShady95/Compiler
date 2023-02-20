class EvaluationResult:
    """
        Holds the result of an evaluation
    """

    # The value of the evaluation
    _value = None

    # A list containing all diagnostics
    _diagnostics = []

    def __init__(self, value: object, diagnostics: list) -> None:
        """
            Sets the given properties

            :param value: object
                 The actual value of the result
            :param diagnostics: list
                A list containing all diagnostics
            :return None
        """
        self._value = value
        self._diagnostics = diagnostics

    def get_value(self) -> object:
        """
            Returns the value of the expression

            :return object
                Returns the value of the expression
        """
        return self._value

    def get_diagnostics(self) -> list:
        """
            Returns a list containing all diagnostics

            :return list
                Returns a list containing all diagnostics
        """
        return self._diagnostics
