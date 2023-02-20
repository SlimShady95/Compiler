class TextSpan:
    """
        Holds the span of a text
    """

    # Starting position
    _start = None

    # Ending position
    _end = None

    # Length of the span
    _length = None

    def __init__(self, start: int, length: int) -> None:
        """
            Sets up all properties

            :param start: int
                The starting position of the text span
            :param length: int
                The length of the text span
            :return None
        """
        self._start = start
        self._end = start + length
        self._length = length

    def get_start(self) -> int:
        """
            Returns the starting position of the text span

            :return int
                Returns the starting position of the text span
        """
        return self._start

    def get_end(self) -> int:
        """
            Returns the end position of the text span

            :return int
                Returns the end position of the text span
        """
        return self._end

    def get_length(self) -> int:
        """
            Returns the length of the text span

            :return int
                Returns the length of the text span
        """
        return self._length
