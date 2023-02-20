from Compiler.Type.TextSpan import TextSpan


class Diagnostic:
    """
        Contains a single diagnostic
    """

    # The text span of the diagnostic
    _span = None

    # The message of the diagnostic
    _message = None

    def __init__(self, span: TextSpan, message: str) -> None:
        """
            Sets up all properties

            :param span: TextSpan
                The text span of the diagnostic
            :param message: str
                The message of the diagnostic
            :return None
        """
        self._span = span
        self._message = message

    def get_span(self) -> TextSpan:
        """
            Returns the text span of the diagnostic

            :return TextSpan
                Returns the text span of the diagnostic
        """
        return self._span

    def __repr__(self) -> str:
        """
            Returns the str representation of this diagnostic

            :return str
                Returns the str representation of this diagnostic
        """
        return self._message

    def __str__(self) -> str:
        """
            Returns the str representation of this diagnostic

            :return str
                Returns the str representation of this diagnostic
        """
        return self.__repr__()
