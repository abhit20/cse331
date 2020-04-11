import unittest
from CircularQueue import CircularQueue, threshold_sum


class TestProject1(unittest.TestCase):

    def test_accessors(self):
        queue = CircularQueue()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        assert not queue.is_empty()
        assert len(queue) == 4
        assert queue.get_total() == 10
        assert queue.head_element() == 1
        assert queue.tail_element() == 4

    def test_enqueue(self):
        queue = CircularQueue()

        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        assert queue.data == [10, 20, 30, None]
        assert queue.size == 3
        assert queue.head == 0
        assert queue.tail == 3
        assert queue.capacity == 4

    def test_dequeue(self):
        queue = CircularQueue(6)

        for i in range(0, 5):
            queue.enqueue(i * 5)

        assert queue.data == [0, 5, 10, 15, 20, None]
        assert queue.size == 5
        assert queue.capacity == 6
        assert queue.head == 0
        assert queue.tail == 5

        queue.dequeue()

        assert queue.data == [None, 5, 10, 15, 20, None]
        assert queue.size == 4
        assert queue.capacity == 6
        assert queue.head == 1
        assert queue.tail == 5

    def test_grow(self):
        queue = CircularQueue(5)

        for i in range(0, 8):
            queue.enqueue(i * 2)

        assert queue.data == [0, 2, 4, 6, 8, 10, 12, 14, None, None]
        assert queue.capacity == 10
        assert queue.size == 8
        assert queue.head == 0
        assert queue.tail == 8

    def test_shrink(self):
        queue = CircularQueue()

        for i in range(0, 5):
            queue.enqueue(i)

        assert queue.data == [0, 1, 2, 3, 4, None, None, None]
        assert queue.size == 5
        assert queue.capacity == 8
        assert queue.head == 0
        assert queue.tail == 5

        for _ in range(3):
            queue.dequeue()

        print(queue.data)
        assert queue.data == [3, 4, None, None]
        assert queue.size == 2
        assert queue.capacity == 4
        assert queue.head == 0
        assert queue.tail == 2

    def test_threshold_sum(self):
        assert threshold_sum([1, 2, 3, 4], 4) == (4, 1)
        assert threshold_sum([1, 3, 2, 4], 4) == (4, 2)
        assert threshold_sum([1, 2, 3, 4], 8) == (7, 2)
        assert threshold_sum([1, 2, 7, 3], 4) == (3, 2)
        assert threshold_sum([1, 2, 2, 3], 6) == (5, 3)
        assert threshold_sum([7, 8, 9, 0, 9, 9], 6) == (0, 1)


if __name__ == "__main__":
    unittest.main()
