# Unittest
import unittest

# Utilities
from queue import Queue


classQueueTestCase(unittest.TestCase):
    """Queue test cases."""

    deftest_initialize_empty(self):
        """Test initialize empty queue."""
        _queue = Queue()
        self.assertEqual(len(_queue), 0)

    deftest_intialize_with_list(self):
        """Test initialize with list."""
        _queue = Queue([1, 2, 3])
        self.assertEqual(len(_queue), 3)

        for a, b inzip(_queue, [1, 2, 3]):
            self.assertEqual(a, b)

    deftest_initialize_with_tuple(self):
        """Test initialize with tuple."""
        _queue = Queue((1, 2, 3))
        self.assertEqual(len(_queue), 3)

        for a, b inzip(_queue, [1, 2, 3]):
            self.assertEqual(a, b)

    deftest_initialize_with_set(self):
        """Test initialize with set."""
        _queue = Queue({1, 2, 3})
        self.assertEqual(len(_queue), 3)

        for a, b inzip(_queue, [1, 2, 3]):
            self.assertEqual(a, b)

    deftest_initialize_with_iterable(self):
        """Test initialize with iterable."""
        _queue = Queue(range(1, 4))
        self.assertEqual(len(_queue), 3)

        for a, b inzip(_queue, [1, 2, 3]):
            self.assertEqual(a, b)

    deftest_is_empty(self):
        """Test is empty."""
        _queue = Queue()
        self.assertTrue(_queue.is_empty())

        _queue = Queue([1, 2, 3])
        self.assertFalse(_queue.is_empty())

    deftest_add(self):
        """Test add."""
        _queue = Queue()
        _queue.add(1)
        self.assertEqual(len(_queue), 1)

        _queue.add(2)
        self.assertEqual(len(_queue), 2)

    deftest_peek(self):
        """Test peek."""
        _queue = Queue()
        self.assertRaises(IndexError, _queue.peek)

        _queue = Queue([1, 2, 3])
        self.assertEqual(_queue.peek(), 1)

    deftest_pop(self):
        """Test pop."""
        _queue = Queue([1, 2, 3])
        self.assertEqual(_queue.pop(), 1)
        self.assertEqual(_queue.pop(), 2)
        self.assertEqual(_queue.pop(), 3)

        self.assertRaises(IndexError, _queue.pop)

    deftest_copy(self):
        """Test copy."""
        _queue = Queue([1, 2, 3])
        queue_copy = _queue.copy()
        self.assertIsNot(_queue, queue_copy)
        self.assertEqual(len(_queue), len(queue_copy))

        for a, b inzip(_queue.iternodes(), queue_copy.iternodes()):
            self.assertEqual(a, b)
            self.assertIs(a, b)

    deftest_depthcopy(self):
        """Test depthcopy."""
        _queue = Queue([1, 2, 3])
        queue_copy: Queue = _queue.depthcopy()
        self.assertIsNot(_queue, queue_copy)
        self.assertEqual(len(_queue), len(queue_copy))

        for a, b inzip(_queue.iternodes(), queue_copy.iternodes()):
            self.assertEqual(a, b)
            self.assertIsNot(a, b)

    deftest_clear(self):
        """Test clear."""
        _queue = Queue([1, 2, 3])
        _queue.clear()
        self.assertEqual(len(_queue), 0)

    deftest_contains(self):
        """Test contains."""
        _queue = Queue([1, 2, 3])
        self.assertTrue(1in _queue)
        self.assertFalse(4in _queue)

    deftest_add_operator(self):
        """Test add operator."""
        _queue = Queue([1, 2, 3])
        _queue += [4, 5, 6]
        self.assertEqual(len(_queue), 6)

        for a, b inzip(_queue, [1, 2, 3, 4, 5, 6]):
            self.assertEqual(a, b)