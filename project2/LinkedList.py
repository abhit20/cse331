"""
PROJECT 2 - Linked List Recursion
Name: Abhinav Thirupathi
PID:
"""

class LinkedNode:
    """
    Class representing a node in the singly linked list implemented below.
    """
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next'

    def __init__(self, value, next=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next: pointer to the next node in the LinkedList, default is None
        """
        self.value = value  # element at the node
        self.next = next  # reference to next node in the LinkedList

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)

    __str__ = __repr__


# IMPLEMENT THESE FUNCTIONS - DO NOT MODIFY FUNCTION SIGNATURES #


def insert(value, node=None):
    """
    Insert the value into the linked list that has head node
    :param value: the value to insert
    :param node: the head node of the linked list
    :return: [node] the starting node of the linked list
    """
    if node is None:
        return LinkedNode(value)
    if node.next is None:
        node.next = LinkedNode(value)
    else:
        insert(value, node.next)
    return node

def to_string(node):
    """
    Generates and returns a string representation of the list
    :param node: the head node of the linked list
    :return: [string] the string of the list
    """
    if node is None:
        return ""
    elif node.next is not None:
      return str(node.value) + ", " + to_string(node.next)
    return str(node.value) + to_string(node.next)

def remove(value, node):
    """
    Removes the first instance of the value from the list
    :param value: the value to remove
    :param node: the head node of the linked list
    :return: [node] the starting node of the linked list
    """
    if node is None:
        return node
    elif node.value == value:
        return node.next
    node.next = remove(value, node.next)
    return node

def remove_all(value, node):
    """
    Removes all the instances of the value from the list
    :param value: the value to remove
    :param node: the head node of the linked list
    :return: [node] the starting node of the linked list
    """
    if node is None:
        return node
    elif node.value == value:
        return remove_all(value, node.next)
    node.next = remove_all(value, node.next)
    return node

def search(value, node):
    """
    Looks for value in the list
    :param value: the value to search
    :param node: the head node of the linked list
    :return: [boolean] True if value exists, else False
    """
    if node is None:
        return False
    elif node.value == value:
        return True
    return search(value, node.next)

def length(node):
    """
    Gives the user the length of their linked list
    :param node: the head node of the linked list
    :return: [length] the length of the linked list
    """
    if node is None:
        return 0
    return 1 + length(node.next)

def sum_list(node):
    """
    Finds the sum of all nodes in the list
    :param node: the head node of the linked list
    :return: the sum of all items in the list
    """
    if node is None:
        return 0
    return node.value + sum_list(node.next)

def count(value, node):
    """
    Counts all of the instances of the value in the list
    :param value: the value to find
    :return: [int] the count of all the instances of the value
    """
    if node is None:
        return 0
    elif node.value == value:
        return 1 + count(value, node.next)
    return count(value, node.next)

def reverse(node):
    """
    Reverse the singly linked list
    :param node: the head node of the linked list
    :return: [node] the starting node of the reversed list
    """
    if node is None or node.next is None:
        return node
    linked_list = reverse(node.next)
    node.next.next = node
    node.next = None
    return linked_list

def remove_fake_requests(head):
    """
    Removes the repeated requests
    :param head: the head node of the linked list
    :return: [node] the starting node of the linked list
    """
    if head is None or head.next is None:
        return head
    elif head.value == head.next.value:
        return remove_fake_requests(head.next.next)
    head.next = remove_fake_requests(head.next)
    return head


