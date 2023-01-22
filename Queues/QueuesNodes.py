from typing import Any
from typing import Iterable
from typing import Optional
from node import Node


class Queue:
    """Represents a simple queue."""

    _front: Optional[Node]
    _rear: Optional[Node]

    _size: int

    def __init__(self, *items) -> None:
        """Initializes the Queue"""
        self._front = None
        self._rear = None
        self._size = 0

        if len(items) > 0 and isinstance(items[0], Iterable):
            items = items[0]

        for item in items:
            self.add(item)

    def clear(self):
        """Clears the queue.

        Time complexity: O(1)
        """

        self._front = None
        self._rear = None
        self._size = 0

    def peek(self):
        """Returns the first element of the queue.

        Raises IndexError if the queue is empty.

        Time complexity: O(1)

        Returns:
            Any: First element of the queue.
        """

        if self._front is None:
            raise IndexError('The queue is empty.')

        return self._front.value

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        Returns:
            bool: True if the queue is empty. False otherwise.
        """

        return self._front is None

    def add(self, value: Any) -> None:
        """Adds a new value to the queue.

        Time Complexity: O(1)

        Args:
            value (Any): Value to be added.

        Returns:
            None
        """

        if self._front is None:
            self._front = Node(value)
            self._rear = self._front

        else:
            self._rear.next = Node(value)
            self._rear = self._rear.next

        self._size += 1

        return None

    def pop(self):
        """Removes a value from the queue.

        Raises IndexError if the queue is empty.

        Time complexity: O(1)

        Returns:
            Any: Removed value.
        """

        if self._front is None:
            raise IndexError('The queue is empty')

        value = self._front.value
        self._front = self._front.next

        self._size -= 1

        return value

    def copy(self):
        """Returns a copy of the current queue.

        Time complexity: O(1)

        Returns:
            Queue: Copy of the current queue.
        """

        new_queue = Queue()

        new_queue._front = self._front
        new_queue._rear = self._rear
        new_queue._size = self._size

        return new_queue

    def depthcopy(self):
        """Returns a copy of the current queue.

        This function will create a copy of each node in the queue.

        Time Complexity: O(n)

        Returns:
            Queue: Copy of the queue.
        """

        new_queue = Queue()

        pointer = self._front

        while pointer is not None:
            new_queue.add(pointer.value)
            pointer = pointer.next

        return new_queue

    def itervalues(self) -> Iterable[Any]:
        """Generates an iterable of the values in the queue.

        Time complexity: O(n)

        Returns:
            Iterable: Iterable of the values in the queue.
        """

        pointer = self._front
        while pointer is not None:
            yield pointer.value
            pointer = pointer.next

        return None

    def iternodes(self) -> Iterable[Node]:
        """Generates an iterable of the nodes in the queue.

        Returns:
            Iterable: Iterable of the nodes in the queue.
        """

        pointer = self._front
        while pointer is not None:
            yield pointer
            pointer = pointer.next

        return None

    def __len__(self) -> int:
        """Returns the length of the queue when using the `len` built-in function.

        Time complexity: O(1)

        Returns:
            int: Number of nodes into the queue.
        """

        return self._size

    def __str__(self):
        """Returns a string representation of the queue.

        Time complexity: O(n)

        Args:
            str: Representation of the queue
        """

        return '->'.join(self.itervalues())

    def __iter__(self) -> Iterable[Any]:
        """Generates an iterable of the values in the queue.

        Time complexity: O(n)

        Returns:
            Iterable: Iterable of the values in the queue.
        """

        return self.itervalues()

    def __contains__(self, value: Any) -> bool:
        """Checks if a value is in the queue.

        Time complexity: O(n)

        Args:
            value: Value to be searched in the queue.

        Returns:
            bool: True if the value is in the queue. False otherwise.
        """

        for item in self:
            if item == value:
                return True

        return False

    def __add__(self, other: Iterable) -> 'Queue':
        """Returns a new queue with the items of both queues.

        Time complexity: O(n)

        Args:
            other (Iterable): Items to be added to the current queue.

        Returns:
            Queue: New queue with the items of both queues.
        """

        new_queue = self.depthcopy()

        for item in other:
            new_queue.add(item)

        return new_queue
