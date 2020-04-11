"""
CSE 331 Project 1
Author: Abhinav Thirupathi
"""

class DLLNode:
    """
    Class representing a node in the doubly linked list implemented below.
    """

    def __init__(self, value, next=None, prev=None):
        """
        Constructor
        @attribute value: the value to give this node
        @attribute next: the next node for this node
        @attribute prev: the previous node for this node
        """
        self.__next = next
        self.__prev = prev
        self.__value = value

    def __repr__(self):
        return str(self.__value)

    def __str__(self):
        return str(self.__value)

    def get_value(self):
        """
        Getter for value
        :return: the value of the node
        """
        return self.__value

    def set_value(self, value):
        """
        Setter for value
        :param value: the value to set
        """
        self.__value = value

    def get_next(self):
        """
        Getter for next node
        :return: the next node
        """
        return self.__next

    def set_next(self, node):
        """
        Setter for next node
        :param node: the node to set
        """
        self.__next = node

    def get_previous(self):
        """
        Getter for previous node
        :return: the previous node
        """
        return self.__prev

    def set_previous(self, node):
        """
        Setter for previous node
        :param node: the node to set
        """
        self.__prev = node

class DLL:
    """
    Class representing a doubly linked list.
    """
    def __init__(self):
        """
        Constructor
        @attribute head: the head of the linked list
        @attribute tail: the tail of the linked list
        @attribute size: the size of the linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.get_next():
                res += " "
            node = node.get_next()
        return res

    def __str__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.get_next():
                res += " "
            node = node.get_next()
        return res

    ######### MODIFY BELOW ##########

    def get_size(self):
        """
        Gives the user the size of their linked list
        :return: [int] the size of the linked list
        """
        return self.size

    def is_empty(self):
        """
        Determines if the linked list is empty or not
        :return: [boolean] true if DLL is empty, false otherwise
        """
        if self.head is None:
            return True
        return False

    def insert_front(self, value):
        """
        Inserts a value into the front of the list
        :param value: the value to insert
        """
        node = DLLNode(value)
        self.size += 1
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        node.set_next(self.head)
        self.head.set_previous(node)
        self.head = node

    def insert_back(self, value):
        """
        Inserts a value into the back of the list
        :param value: the value to insert
        """
        node = DLLNode(value)
        self.size += 1
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        node.set_previous(self.tail)
        self.tail = node

    def delete_front(self):
        """
        Deletes the front node of the list
        """
        if self.size is 0:
            return
        elif self.size == 1:
            self.size -= 1
            self.head = None
            self.tail = None
            return
        self.size -= 1
        self.head = self.head.get_next()
        self.head.set_previous(None)

    def delete_back(self):
        """
        Deletes the back node of the list
        """
        if self.size is 0:
            return
        elif self.size == 1:
            self.size -= 1
            self.head = None
            self.tail = None
            return
        self.size -= 1
        self.tail = self.tail.get_previous()
        self.tail.set_next(None)

    def delete_value(self, value):
        """
        Deletes the first instance of the value in the list.
        :param value: The value to remove
        """
        node = self.find_first(value)
        if node is self.head:
            self.delete_front()
        elif node is self.tail:
            self.delete_back()
        elif node != None:
            self.size -= 1
            node.get_next().set_previous(node.get_previous())
            node.get_previous().set_next(node.get_next())

    def delete_all(self, value):
        """
        Deletes all instances of the value in the list
        :param value: the value to remove
        """
        node = self.head
        while node is not None:
            self.delete_value(value)
            node = node.get_next()

    def find_first(self, value):
        """
        Finds the first instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the first node containing the value
        """
        node = self.head
        while node is not None:
            if node.get_value() == value:
                return node
            node = node.get_next()

    def find_last(self, value):
        """
        Finds the last instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the last node containing the value
        """
        node = self.tail
        while node is not None:
            if node.get_value() == value:
                return node
            node = node.get_previous()

    def find_all(self, value):
        """
        Finds all of the instances of the value in the list
        :param value: the value to find
        :return: [List] a list of the nodes containing the value
        """
        node_lst = list()
        node = self.head
        while node is not None:
            if node.get_value() == value:
                node_lst.append(node)
            node = node.get_next()
        return node_lst

    def count(self, value):
        """
        Finds the count of times that the value occurs in the list
        :param value: the value to count
        :return: [int] the count of nodes that contain the given value
        """
        return(len(self.find_all(value)))

    def sum(self):
        """
        Finds the sum of all nodes in the list
        :param start: the indicator of the contents of the list
        :return: the sum of all items in the list
        """
        if self.size == 0:
            return None
        sum = self.head.get_value()
        node = self.head.get_next()
        while node is not None:
            if type(self.head.get_value()) == type(node.get_value()):
                sum += node.get_value()
            node = node.get_next()
        return sum

def remove_middle(LL):
    """
    Removes the middle of a given doubly linked list.
    :param DLL: The doubly linked list that must be modified
    :return: The updated linked list
    """
    if LL.get_size() == 0:
        return LL
    elif LL.get_size() == 1:
        LL.delete_front()
        return LL
    elif LL.get_size() == 2:
        while LL.get_size() != 0:
            LL.delete_front()
        return LL
    elif LL.get_size()%2 == 1:
        count = 1
        node = LL.head
        while count != (LL.get_size()//2+1):
            count += 1
            node = node.get_next()
        LL.size -= 1
        node.get_next().set_previous(node.get_previous())
        node.get_previous().set_next(node.get_next())
        return LL
    elif LL.get_size()%2 == 0:
        count = 1
        node = LL.head
        while count != (LL.get_size() // 2):
            count += 1
            node = node.get_next()
        LL.size -= 1
        node.get_next().set_previous(node.get_previous())
        node.get_previous().set_next(node.get_next())
        LL = remove_middle(LL)
        return LL
