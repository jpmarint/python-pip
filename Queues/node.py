class Node:
    """
    Node class for a linked list.
    """

    def __init__(self, value, next=None) -> None:
        """
        Initialize a node with a value and a next node.

        Args:
            value: The value of the node.
            next: The next node.
        """

        self.value = value

        self.next = next

    def copy(self) -> 'Node':
        """
        Return a copy of the node.

        Returns:
            A copy of the node.
        """

        return Node(self.value, self.next)

    @staticmethod
    def _parse_other_value(other):
        if isinstance(other, Node):
            return other.value

        return other

    def __lt__(self, other: 'Node') -> bool:
        """Check if the current value is less than the other value.

        Args:
            other: Node to be compared.

        Returns:
            bool: True if the current value is less than the other one. False otherwise.
        """

        return self.value < self._parse_other_value(other)

    def __le__(self, other: 'Node') -> bool:
        """Check if the current value is less than or equals to the other value.

        Args:
            other: Node to be compared.

        Returns:
            bool: True if the current value is less than or equals to the other one. False otherwise.
        """

        return self.value <= self._parse_other_value(other)

    def __eq__(self, other: 'Node') -> bool:
        """Check if the current value is equals to the other value.

        Args:
            other: Node to be compared.

        Returns:
            bool: True if the current value is equals to the other one. False otherwise.
        """

        return self.value == self._parse_other_value(other)

    def __ge__(self, other: 'Node') -> bool:
        """Check if the current value is greater than or equals to the other value.

        Args:
            other: Node to be compared.

        Returns:
            bool: True if the current value is greater than or equals to the other one. False otherwise.
        """

        return self.value >= self._parse_other_value(other)

    def __ge__(self, other: 'Node') -> bool:
        """Check if the current value is greater than the other value.

        Args:
            other: Node to be compared.

        Returns:
            bool: True if the current value is greater than the other one. False otherwise.
        """

        return self.value > self._parse_other_value(other)

    def __str__(self) -> str:
        return str(self.value)