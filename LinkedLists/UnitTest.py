# Unittest
import unittest

# Utils
from CircularDoubleLinkedList import DoubleLinkedList


class DoubleLinkedListTestCase(unittest.TestCase):
    """Test case for DoubleLinkedList"""

    def test_initialize_empty_list(self):
        """Test initialize empty list"""
        dll = DoubleLinkedList()
        self.assertEqual(dll.size, 0)

    def test_initialize_list_with_values(self):
        """Test initialize list with values"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        self.assertEqual(dll.size, 3)

        for a, b in zip(['a', 'b', 'c'], dll):
            self.assertEqual(a, b)

    def test_append_item(self):
        """Test append item"""
        dll = DoubleLinkedList()
        dll.append('a')
        self.assertEqual(dll.size, 1)

    def test_insert_item_at_first_position(self):
        """Test insert item at first position"""
        dll = DoubleLinkedList(1)
        dll.insert(0, 'a')
        self.assertEqual(dll.size, 2)

        for a, b in zip(['a', 1], dll):
            self.assertEqual(a, b)

    def test_insert_item(self):
        """Test insert item"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        dll.insert(1, 'd')
        self.assertEqual(dll.size, 4)

        for a, b in zip(['a', 'd', 'b', 'c'], dll):
            self.assertEqual(a, b)

    def test_index_item(self):
        """Test index item"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        self.assertEqual(dll.index('b'), 1)

    def test_index_item_not_found(self):
        """Test index item not found"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        self.assertRaises(ValueError, dll.index, 'd')

    def test_clear_list(self):
        """Test clear list"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        dll.clear()
        self.assertEqual(dll.size, 0)

    def test_replace_item(self):
        """Test replace item"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        dll.replace('b', 'd')
        self.assertEqual(dll.size, 3)

        for a, b in zip(['a', 'd', 'c'], dll):
            self.assertEqual(a, b)

    def test_replace_item_not_found(self):
        """Test replace item not found"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        self.assertRaises(ValueError, dll.replace, 'd', 'e')

    def test_replace_by_index(self):
        """Test replace by index"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        dll[1] = 'd'
        self.assertEqual(dll.size, 3)

        for a, b in zip(['a', 'd', 'c'], dll):
            self.assertEqual(a, b)

    def test_pop_item(self):
        """Test pop item"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        self.assertEqual(dll.pop(), 'c')
        self.assertEqual(dll.size, 2)

        for a, b in zip(['a', 'b'], dll):
            self.assertEqual(a, b)

    def test_remove_item_by_index(self):
        """Test remove item by index"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        del dll[1]
        self.assertEqual(dll.size, 2)

        for a, b in zip(['a', 'c'], dll):
            self.assertEqual(a, b)

    def test_reverse_list(self):
        """Test reverse list"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        dll.reverse()
        self.assertEqual(dll.size, 3)

        for a, b in zip(['c', 'b', 'a'], dll):
            self.assertEqual(a, b)