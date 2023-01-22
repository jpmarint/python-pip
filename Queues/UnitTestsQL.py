# Unittest
import unittest

# Utilities
from QueuesLists import Queue


class QueueTestCase(unittest.TestCase):
    """Queue test cases."""

    def test_initialize_empty(self):
        """Test initialize empty queue."""
        _queue = Queue()
        self.assertEqual(len(_queue), 0)

    def test_intialize_with_list(self):
        """Test initialize with list."""
        _queue = Queue([1, 2, 3])
        self.assertEqual(len(_queue), 3)

        for a, b in zip(_queue, [1, 2, 3]):
            self.assertEqual(a, b)

    def test_initialize_with_tuple(self):
        """Test initialize with tuple."""
        _queue = Queue((1, 2, 3))
        self.assertEqual(len(_queue), 3)

        for a, b in zip(_queue, [1, 2, 3]):
            self.assertEqual(a, b)

    def test_initialize_with_set(self):
        """Test initialize with set."""
        _queue = Queue({1, 2, 3})
        self.assertEqual(len(_queue), 3)

        for a, b in zip(_queue, [1, 2, 3]):
            self.assertEqual(a, b)

    def test_initialize_with_iterable(self):
        """Test initialize with iterable."""
        _queue = Queue(range(1, 4))
        self.assertEqual(len(_queue), 3)

        for a, b in zip(_queue, [1, 2, 3]):
            self.assertEqual(a, b)

    def test_is_empty(self):
        """Test is empty."""
        _queue = Queue()
        self.assertTrue(_queue.is_empty())

        _queue = Queue([1, 2, 3])
        self.assertFalse(_queue.is_empty())

    def test_enqueue(self):
        """Test add."""
        _queue = Queue()
        _queue.enqueue(1)
        self.assertEqual(len(_queue), 1)

        _queue.enqueue(2)
        self.assertEqual(len(_queue), 2)

    def test_peek(self):
        """Test peek."""
        _queue = Queue()
        self.assertRaises(IndexError, _queue.peek)

        _queue = Queue([1, 2, 3])
        self.assertEqual(_queue.peek(), 1)

    def test_dequeue(self):
        """Test dequeue."""
        _queue = Queue([1, 2, 3])
        self.assertEqual(_queue.dequeue(), 1)
        self.assertEqual(_queue.dequeue(), 2)
        self.assertEqual(_queue.dequeue(), 3)

        self.assertRaises(IndexError, _queue.dequeue)

    def test_copy(self):
        """Test copy."""
        _queue = Queue([1, 2, 3])
        queue_copy = _queue.copy()
        self.assertIsNot(_queue, queue_copy)
        self.assertEqual(len(_queue), len(queue_copy))

        for a, b in zip(_queue, queue_copy):
            self.assertEqual(a, b)

    def test_depthcopy(self):
        """Test depthcopy."""
        _queue = Queue([1, 2, 3])
        queue_copy: Queue = _queue.depthcopy()
        self.assertIsNot(_queue, queue_copy)
        self.assertEqual(len(_queue), len(queue_copy))

        for a, b in zip(_queue, queue_copy):
            self.assertEqual(a, b)

    def test_clear(self):
        """Test clear."""
        _queue = Queue([1, 2, 3])
        _queue.clear()
        self.assertEqual(len(_queue), 0)

    def test_contains(self):
        """Test contains."""
        _queue = Queue([1, 2, 3])
        self.assertTrue(1 in _queue)
        self.assertFalse(4 in _queue)

    def test_add_operator(self):
        """Test add operator."""
        _queue = Queue([1, 2, 3])
        _queue += [4, 5, 6]
        self.assertEqual(len(_queue), 6)

        for a, b in zip(_queue, [1, 2, 3, 4, 5, 6]):
            self.assertEqual(a, b)
