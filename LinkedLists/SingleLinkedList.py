from typing import Any
from typing import Optional
from typing import Iterator
from typing import Union
from typing import Iterable

from node import Node


class SinglyLinkedList:
    """Singly Linked List"""

    _head: Optional[Node]
    _tail: Optional[Node]
    _size: int

    def __init__(self, *items) -> None:
        """Initialize an empty list

        Args:
            *items: Items to be added to the list.
        """

        self._head = None
        self._tail = None
        self._size = 0

        if len(items) == 1 and isinstance(items[0], (Iterable, SinglyLinkedList)):
            items = items[0]

        for item in items:
            self.append(item)

    @property
    def size(self):
        """Returns the size of the linked list.

        Time complexity: O(1)
        """

        return self._size

    def clear(self):
        """Clears the list.

        Removes all the items inside the list.
        """

        self._head = None
        self._size = 0

    def copy(self):
        """Returns a copy of the list.

        Time Complexity: O(1)
        """

        new_list = SinglyLinkedList()

        if self._head is not None:
            # Caution: This is a shallow copy
            new_list._head = self._head
            new_list._size = self._size

        return new_list

    def depthcopy(self) -> 'SinglyLinkedList':
        """Returns a copy of the list and its nodes.

        Time complexity: O(n)

        Returns:
            SinglyLinkedList: Copy of the list.
        """

        new_list = SinglyLinkedList()

        for item in self:
            new_list.append(item.value)

        return new_list

    def append(self, value: Any):
        """Appends a new value at the end of the list.

        Time complexity: O(1)
        """

        node = Node(value)

        if self._head is None:
            self._head = node
            self._tail = self._head

        else:
            self._tail.next = Node(value)
            self._tail = self._tail.next

        self._size += 1

    def extend(self, other: Iterable):
        """Extends the current list with the provided list.

        Time complexity: O(n) where n is the length of the list to extend.

        Args:
            other: List to be extended.
        """

        for item in other:
            if isinstance(other, Node):
                self.append(item.value)

            else:
                self.append(item)

    def pop(self, index: int = -1) -> Any:
        """Removes an item from the list.

        Raises IndexError if the list is empty or index is out of range.

        Time complexity: O(n) where n is the length of the nodes.

        Args:
            index: Index of the item to be removed.

        Returns:
            Any: Item removed.
        """

        if index < 0:
            index = self._size + index

        if self._head is None or index > self._size - 1:
            raise IndexError('Index out of range.')

        prev_pointer = self._head

        value: Node
        for idx, value in enumerate(self):
            if idx == index:
                if value == self._head:
                    self._head = None
                    self._tail = None
                else:
                    prev_pointer.next = value.next
                    self._tail = prev_pointer
                    self._size -= 1

                return value

            prev_pointer = value

    def index(self, target: object):
        """Return first index of value.

        Raises ValueError if the value is not present.

        Time complexity: O(n) where n is the length of nodes.

        Args:
            target: Value to look up.

        Returns:
            int: Index of the value.
        """

        item: Node
        for index, item in enumerate(self):
            if item.value == target:
                return index

        raise ValueError(f'{target} is not in list')

    def count(self, target: object) -> int:
        """Counts the number of occurrences of the provided value.

        Time complexity: O(n) where n is the length of the nodes.

        Args:
            target: Value to be counted.

        Returns:
            int: Number of occurrences.
        """

        count = 0

        item: Node
        for item in self:
            if item.value == target:
                count += 1

        return count

    def insert(self, index: int, value: object):
        """Insert before index.

        Time complexity: O(n)

        Args:
            index: Index to insert before.
            value: Value to insert.
        """

        if index < 0:
            index = self._size + index

        if index > self._size - 1:
            raise IndexError('Index out of range.')

        if index == 0:
            self._head = Node(value, self._head)

        else:
            prev_pointer = self._head
            item: Node
            for idx, item in enumerate(self):
                if idx == index:
                    new_node = Node(value, item)
                    prev_pointer.next = new_node
                    break;

                prev_pointer = item

        self._size += 1

    def remove(self, value):
        """Removes the first occurrence of value.

        Raises ValueError if the value is not present.

        Args:
            value: Value to be removed.
        """

        common_error = ValueError('Value not found')

        if self._head is None:
            raise common_error

        if self._head.value == value:
            self._head = self._head.next

        else:
            prev_node: Optional[Node] = None
            item: Node
            for item in self:
                if item.value == value:
                    prev_node.next = item.next

                    if item == self._tail:
                        self._tail = prev_node

                    found = True
                    break

                prev_node = item


            if not found:
                raise common_error

        self._size -= 1

    def _sort_nodes(self, head: Node, reversed: bool = False):
        """Sorts the nodes of a linked list.

        Time complexity: O(n log n)

        Args:
            head: head node of the linked list.
            reversed: True to sort in descending order, False to sort in ascending order.

        Returns:
            tuple: (head, tail) of the sorted linked list.
        """

        # If there are only 1 or 0 nodes heads that the list is already sorted.
        if head is None or head.next is None:
            return head

        temp = head
        slow = head
        fast = head

        # We need to divide the list in half.
        # The fast node will be the last node when the loop ends,
        # and the slow node will be at the middle of the list beacause
        # the fast node is traversing the list two steps at the once and the slow 1 at once.

        # temp will be the end of the first half.
        # slow will be the head of the second half.
        # fast will be the end of the second half.

        # Example:
        #  head          temp   slow                 fast
        # [1,   2,   3,   4   , 5   ,  6,  7,   8,  9]

        while fast is not None and fast.next is not None:
            temp = slow
            slow = slow.next
            fast = fast.next.next

        # Set the end of the first half
        temp.next = None

        left_half = self._sort_nodes(head, reversed=reversed)
        if isinstance(left_half, tuple):
            left_half = left_half[0]

        right_half = self._sort_nodes(slow, reversed=reversed)
        if isinstance(right_half, tuple):
            right_half = right_half[0]

        # Merge
        sorted_temp = Node(Node)
        current_node = sorted_temp

        while left_half is not None and right_half is not None:

            if (not reversed and left_half.value < right_half.value) or (reversed and left_half.value > right_half.value):
                current_node.next = left_half
                left_half = left_half.next

            else:
                current_node.next = right_half
                right_half = right_half.next

            current_node = current_node.next

        if left_half is not None:
            current_node.next = left_half
            left_half = left_half.next

        if right_half is not None:
            current_node.next = right_half
            right_half = right_half.next

        tail = current_node
        while tail.next is not None:
            tail = tail.next

        return sorted_temp.next, tail

    def sort(self, reversed: bool = False):
        """Sort the list in ascending order and return None.

        The reverse flag can be set to sort in descending order.

        Time complexity: O(n log n)

        Args:
            reversed: True to sort in descending order.

        Returns:
            None
        """

        self._head, self._tail = self._sort_nodes(self._head, reversed)

        return None

    def search(self, target: object) -> bool:
        """Check if the provided value is in the list.

        Time complexity: O(n) where n is the length of the nodes.

        Args:
            target: Value to be searched inside the list.

        Returns:
            bool: True if found. False otherwise.
        """

        return target in self

    def iter(self):
        """Allows to iterate over the list using a generator.

        Time complexity: O(n)

        Returns:
            Iterator[Node]: Iterator over the list.
        """

        if self._head is not None:
            pointer = self._head

            while pointer is not None:
                val = pointer
                pointer = pointer.next

                yield val

        return None

    def reverse(self):
        """Reverses the list.

        Time complexity: O(n)

        Returns:
            None
        """

        if self._head is not None:

            current_node: None = self._head
            remaining_values: Optional[Node] = self._head.next

            # Set the head next value to None beacuse now it will be the tail
            current_node.next = None

            while remaining_values is not None:

                temp_ref = current_node
                current_node: Node = remaining_values
                remaining_values = current_node.next

                current_node.next = temp_ref

            self._tail = self._head
            self._head = current_node

    # ==========================
    # Dunders
    # ==========================

    def __delitem__(self, index: Union[int, slice]):
        """Deletes an item from the list.

        Time complexity: O(n)

        Args:
            index: Index of the item to be removed.

        Returns:
            None
        """

        if isinstance(index, slice):
            list_items = list(self)

            del list_items[index]

            self.clear()
            for item in list_items:
                self.append(item)

        else:

            if index > self._size - 1:
                raise IndexError('Index out of range.')

            if index == 0:
                self._head = self._head.next

            else:
                prev_pointer: Optional[Node] = None

                item: Node
                for idx, item in enumerate(self):
                    if idx == index:
                        prev_pointer.next = item.next

                        if item == self._tail:
                            self._tail = prev_pointer

                        break
                    prev_pointer = item

            self._size -= 1

        return None

    def __setitem__(self, index: Union[int, slice], value: Union[object, Iterable]):
        """Set self[key] to value.

        Time complexity: O(n)

        Args:
            index: Index to be set.
            value: Value to assign.
        """

        if isinstance(index, slice):
            if not isinstance(value, Iterable):
                raise TypeError('can only assign an iterable')

            if len(value) > 0:
                list_items = list(self)
                list_items[index] = value

                self.clear()
                for item in list_items:
                    self.append(item)

        else:

            if index < 0:
                index = self._size + index

            if index > self._size - 1:
                raise IndexError('list assignment index out of range')

            if index == 0:
                self._head.value = value

            else:
                item: Node
                for idx, item in enumerate(self):
                    if idx == index:
                        item.value = value
                        break

    def __add__(self, values: Iterable) -> 'SinglyLinkedList':
        """Returns a new list with the nodes of the current list a the values or nodes of the other list.

        Time complexity: O(n) where n is the length of values to add.

        Returns:
            SinglyLinkedList: Merged linked list.
        """

        new_list = self.depthcopy()

        for item in values:
            new_list.append(item)

        return new_list

    def __iadd__(self, values: Iterable):
        """Appends values to the list when using the += operator.

        Time complexity: O(n) where n is the length of items to append.

        Returns:
            self
        """

        for item in values:
            self.append(item)

        return self

    def __len__(self):
        """Returns the size of the linked list when using the built-in function len."""
        return self._size

    def __mul__(self, times: int):
        """
        Returns a new list with the items duplicated by provided factor.

        Args:
            times: Number of times to duplicate the list.

        Returns:
            SinglyLinkedList: Duplicated list.
        """

        if times <= 0:
            return SinglyLinkedList()

        new_list = self.depthcopy()

        for _ in range(times - 1):
            new_list += self.depthcopy()

        return new_list

    def __rmul__(self, times: int):
        """
        Returns a new list with the items duplicated by provided factor.

        Args:
            times: Number of times to duplicate the list.

        Returns:
            SinglyLinkedList: Duplicated list.
        """

        return self.__mul__(times)

    def __imul__(self, times: int):
        """Duplicates the current list items by the provided factor and appends them to the end.

        Time complexity: O(a * b) where a is the number of duplicates to add and b is the length of the list.

        Args:
            times: Number of times to duplicate the list.

        Returns:
            self
        """

        if times <= 0:
            self.clear()

        else:

            base = self.depthcopy()

            for _ in range(times - 1):
                self.extend(base.depthcopy())

        return self

    def __iter__(self) -> Iterator[Node]:
        """Allows to iterate over the list using a generator.

        Time complexity: O(n)

        Returns:
            Iterator[Node]: Iterator over the list.
        """
        return self.iter()

    def __contains__(self, target: object) -> bool:
        """Check if a value is in the list when using the 'in' operator.

        Time complexity: O(n) where n is the length of the nodes.
        """

        output = False

        pointer = self._head

        while pointer is not None and pointer.value != target and pointer.next is not None:
            pointer = pointer.next

        if pointer is not None and pointer.value == target:
            return target

        return output

    def __getitem__(self, index: Union[int, slice]):
        """Get item with the index or slice from the linked list.

        Time Complexity: O(n) where n is the length of the nodes.

        Returns:
            Any: Item with the index or slice.
        """

        if isinstance(index, slice):

            items = list(self)[index]
            new_list = SinglyLinkedList(items)

            return new_list

        if index > self.size - 1:
            raise IndexError('Index out of range')

        if index < 0:
            index = self._size + index

        for idx, value in enumerate(self):
            if index == idx:
                return value

        return None

    def __lt__(self, other: 'SinglyLinkedList') -> bool:
        """Check if the list is less than the other list.

        Time Complexity: O(n) where n is the length of the nodes of the list with less nodes.

        Args:
            other (SinglyLinkedList): Other list to be compared.

        Returns:
            bool: True if the list is equals to the other list. False otherwise.
        """

        if len(self) >= len(other):
            return False

        for self_item, other_item in zip(self, other):
            if self_item.value != Node._parse_other_value(other_item):
                return False

        return True

    def __le__(self, other: 'SinglyLinkedList') -> bool:
        """Check if the list is less than or equals to the other list.

        Time Complexity: O(n) where n is the length of the nodes of the list with less nodes.

        Args:
            other (SinglyLinkedList): Other list to be compared.

        Returns:
            bool: True if the list is equals to the other list. False otherwise.
        """

        if len(self) > len(other):
            return False

        for self_item, other_item in zip(self, other):
            if self_item.value != Node._parse_other_value(other_item):
                return False

        return True

    def __eq__(self, other: 'SinglyLinkedList') -> bool:
        """Check if the list is equal to the other list.

        Time Complexity: O(n) where n is the length of the nodes of the list with less nodes.

        Args:
            other (SinglyLinkedList): Other list to be compared.

        Returns:
            bool: True if the list is equals to the other list. False otherwise.
        """

        if len(self) != len(other):
            return False

        for self_item, other_item in zip(self, other):
            if self_item.value != Node._parse_other_value(other_item):
                return False

        return True

    def __ge__(self, other: 'SinglyLinkedList') -> bool:
        """
        Check if the list is greater or equal than the other list.

        Time Complexity: O(n) where n is the length of the nodes of the list with less nodes.

        Args:
            other (SinglyLinkedList): Other list to be compared.

        Returns:
            bool: True if the list is greater or equal than the other list. False otherwise.
        """

        if len(self) < len(other):
            return False

        for self_item, other_item in zip(self, other):
            if self_item.value != Node._parse_other_value(other_item):
                return False

        return True

    def __gt__(self, other: 'SinglyLinkedList') -> bool:
        """
        Check if the list is greater than the other list.

        Time Complexity: O(n) where n is the length of the nodes of the list with less nodes.

        Args:
            other (SinglyLinkedList): Other list to be compared.

        Returns:
            bool: True if the list is greater than the other list. False otherwise.
        """

        if len(self) <= len(other):
            return False

        for self_item, other_item in zip(self, other):
            if self_item.value != Node._parse_other_value(other_item):
                return False

        return True