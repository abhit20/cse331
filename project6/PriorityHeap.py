class Node:
    """
    Node definition should not be changed in any way
    """
    __slots__ = ['_key', '_value']

    def __init__(self, k, v):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self._key = k
        self._value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False if otherwise
        """
        return self._key < other.get_key() or (self._key == other.get_key() and self._value < other.get_value())

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False if otherwise
        """
        return self._key > other.get_key() or (self._key == other.get_key() and self._value > other.get_value())

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False if otherwise
        """
        return self._key == other.get_key() and self._value == other.get_value()

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0},{1})'.format(self._key, self._value)

    __repr__ = __str__

    def get_key(self):
        """
        Key getter function
        :return: key value of the node
        """
        return self._key

    def set_key(self, new_key):
        """
        Key setter function
        :param new_key: the value the key is to be changed to
        """
        self._key = new_key

    def get_value(self):
        """
        Value getter function
        :return: value of the node
        """
        return self._value


class PriorityHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = '_data'

    def __init__(self):
        """
        Initializes the priority heap
        """
        self._data = []

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self._data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self._data)

    __repr__ = __str__

#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Modify below this line

    def empty(self):
        """
        Checks if the priority queue is empty
        :return: Return true if empty, else false
        """
        return len(self) == 0

    def top(self):
        """
        Gives the root value
        :return: If no root value, return None, else Node
        """
        if self.empty(): return None
        return self._data[0].get_value()

    def push(self, key, val):
        """
        Use the key and value parameters to add a Node to the heap.
        :param key: Key, also the priority of the Node
        :param val: Value of the node
        :return: None
        """
        self._data.append(Node(key, val))
        self.percolate_up(len(self)-1)

    def pop(self):
        """
        Removes the smallest element from the priority queue
        :return: Return Node, else None if no elements exist
        """
        if self.empty(): return None
        self._swap(0, len(self._data) - 1)  # put minimum item at the end
        item = self._data.pop()  # and remove it from the list;
        self.percolate_down(0)  # then fix new root
        return item

    def min_child(self, index):
        """
        Given an index of a node, return the index of the smaller child.
        :param index: Index of a node
        :return: If index is a leaf, return None, else int
        """
        if self.empty() is False:
            lhs = self._left(index)
            rhs = self._right(index)
            if self._has_left(index):
                if self._has_right(index):
                    return lhs if self._data[lhs] < self._data[rhs] else rhs
                return lhs

    def _parent(self, index):
        """
        Computes index of the parent
        :param index: Index in the array
        :return: Index of the parent
        """
        return (index - 1) // 2

    def _left(self, index):
        """
        Computes index of the left child
        :param index: Index in the array
        :return: Index of the parent's left child
        """
        return 2 * index + 1

    def _right(self, index):
        """
        Computes index of the right child
        :param index: Index in the array
        :return: Index of the parent's right child
        """
        return 2 * index + 2

    def _has_left(self, index):
        """
        Checks if left child exists
        :param index: Index of the child
        :return: True if left child exists, else false
        """
        return self._left(index) < len(self._data)  # index beyond end of list?

    def _has_right(self, index):
        """
        Checks if right child exists
        :param index: Index of the child
        :return: True if right child exists, else false
        """
        return self._right(index) < len(self._data)  # index beyond end of list?

    def _swap(self, i, j):
        """
        Swap the elements at indices i and j of array.
        :param i: The first index
        :param j: The second index
        :return:
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def percolate_up(self, index):
        """
        Given the index of a node, move the node up to its valid spot in the heap.
        :param index: Index of the node
        :return: None
        """
        parent = self._parent(index)
        if index > 0 and self._data[index] < self._data[parent]:
            self._swap(index, parent)
            self.percolate_up(parent)

    def percolate_down(self, index):
        """
        Given the index of a node, move the node down to its valid spot in the heap
        :param index: Index of the node
        :return: None
        """
        if self._has_left(index):
            left = self._left(index)
            small_child = left
            if self._has_right(index):
                right = self._right(index)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[index]:
                self._swap(index, small_child)
                self.percolate_down(small_child)

    def change_priority(self, index, new_key):
        """
        Change the priority of the node at the given index to the given value.
        :param index: A nonnegative value
        :param new_key: The new priority (key)
        :return:
        """
        if self.empty() is False:
            if index >= 0 and index <= len(self)-1:
                self._data[index].set_key(new_key)
                if index < new_key:
                    self.percolate_down(index)
                elif index > new_key:
                    self.percolate_up(index)

def heap_sort(array):
    """
    Given a list of data, use heap sort to sort the data
    :param array: Array to be sorted
    :return: List of the sorted data
    """
    if array is not None:
        heap = PriorityHeap()
        for ele in array:
            heap.push(ele, "a")
        temp = []
        while heap.empty() is not True:
            temp.append(heap.pop().get_key())
        return temp

def merge_lists(array_list):
    """
    Merge lists and then sort them
    :param array_list: The list of unsorted lists
    :return: List of the sorted data
    """
    if array_list is not None:
        for i in range(len(array_list)):
            array_list[i] = heap_sort(array_list[i])

        temp = []
        heap = PriorityHeap()
        for i in range(len(array_list)):
            if array_list[i] is not None:
                if len(array_list[i]) > 0:
                    heap.push(array_list[i][0], i)
                    array_list[i].pop(0)

        while heap.empty() is not True:
            node = heap.pop()
            if len(temp) > 0:
                if node.get_key() is not temp[-1]:
                    temp.append(node.get_key())
            else:
                temp.append(node.get_key())

            if array_list[node.get_value()] is not None:
                if len(array_list[node.get_value()]) > 0:
                    heap.push(array_list[node.get_value()][0],node.get_value())
                    array_list[node.get_value()].pop(0)

        return temp