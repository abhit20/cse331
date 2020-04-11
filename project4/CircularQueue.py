"""
Project 4- Solution
"""


class CircularQueue:
    """
    Circular Queue Class.
    """

    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0
        self.total = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size and self.total == other.get_total()

    def __str__(self):
        """
        String representation of the queue
        :return: the queue as a string
        """
        if self.is_empty():
            return "Empty queue"
        result = ""
        str_list = [str(self.data[(self.head + i) % self.capacity]) for i in range(self.size)]
        return "Queue: " + (", ").join(str_list)

    # -----------MODIFY BELOW--------------

    def is_empty(self):
        """
        Checks if queue is empty
        :return: true if queue is empty, false otherwis
        """
        return self.size == 0

    def __len__(self):
        """
        Finds the size of the queue
        :return: the size of the queue
        """
        return self.size

    def get_total(self):
        """
        Calculates the sum of the elements in the queue
        :return: the sum of the elements in the queue
        """
        return self.total

    def head_element(self):
        """
        Finds the head of the queue
        :return: front element of the queue
        """
        return self.data[self.head]

    def tail_element(self):
        """
        Finds the tail of the queue
        :return: last element of the queue
        """
        return self.data[self.tail-1]

    def enqueue(self, val):
        """
        Add an element to the back of the queue
        :param val: value to add
        :return: None
        """
        avail = (self.head + self.size) % len(self.data)
        self.data[avail] = val
        self.total += val
        self.size += 1
        self.tail = self.size
        if self.size == len(self.data):
            self.grow()

    def dequeue(self):
        """
        Remove an element from the front of a queue.
        :return: element popped, None if empty
        """
        if self.is_empty():
            return None
        answer = self.data[self.head]
        self.total -= answer
        self.data[self.head] = None
        self.head = (self.head + 1) % len(self.data)
        self.size -= 1
        self.shrink()
        return answer

    def grow(self):
        """
        Doubles the capacity of queue
        :return: None
        """
        old = self.data
        self.data = [None] * (int(self.capacity * 2))
        self.capacity *= 2
        walk = self.head
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.head = 0

    def shrink(self):
        """
        Halves the capacity of the queue
        if the size is 1/4 or less of the capacity
        :return: None
        """
        if (self.capacity/4) >= self.size and self.capacity//2 >= 4:
            old = self.data
            self.capacity /= 2
            self.capacity = int(self.capacity)
            if self.capacity < 4:
                self.capacity = 4
            self.data = [None] * (int(self.capacity))

            walk = self.head
            for k in range(self.size):
                self.data[k] = old[walk]
                walk = (1 + walk) % len(old)
            self.head = 0
            self.tail = self.size


def threshold_sum(nums, threshold):
    """
    Finds the sequence of consecutive numbers
    in nums with the highest possible sum less than or
    equal to the threshold.
    :param nums: sequence of consecutive numbers
    :param threshold: the sum of the sequence of consecutive numbers
    :return: tuple containing the sum of the elements for that sequence and the length of the sequence
    """
    circular_nums = CircularQueue()
    n = len(nums)
    curr_sum = nums[0]
    start = 0
    i = 1
    while i <= n:

        while curr_sum > threshold and start < i - 1:
            curr_sum = curr_sum - nums[start]
            start += 1

        if curr_sum >= threshold:
            return (curr_sum, i - start)

        if i < n:
            curr_sum = curr_sum + nums[i]
        i += 1

    return 0
