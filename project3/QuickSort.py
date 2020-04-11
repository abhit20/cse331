"""
PROJECT 3 - Quick/Insertion Sort
Name: Abhinav Thirupathi
PID: Abhinav Thirupathi
"""

from Project3.InsertionSort import insertion_sort


def quick_sort(dll, start, end, size, threshold):
    """
    Quick sort on a doubly linked list larger than threshold
    :param dll: the doubly linked list that is being sorted
    :param start: node to start sorting at (inclusive)
    :param end: node to end sorting at (inclusive)
    :param size: size from start node to end node
    :param threshold: insertion sort when the DLL's size is less than or equal to the threshold
    :return: None
    """

    if size > 1 and size <= threshold:
        insertion_sort(dll, start, end)
    else:
        if end is not None:
            if start != end:
                if start != end.get_next():
                    pivot, size_p = partition(start, end)
                    quick_sort(dll, start, pivot.get_previous(), size_p, threshold)
                    quick_sort(dll, pivot.get_next(), end, size_p, threshold)


def partition(low, high):
    """
    Partitions the doubly linked list linked list with the high node value as the pivot
    :param low: beginning node to start partitioning at
    :param high: last node to partition at used as pivot
    :return: tuple of pivot node and new size from the start to pivot
    """
    pivot = high.get_value()
    i = low.get_previous()
    j = low
    while j != high:
        if j.get_value() <= pivot:
            if i is None:
                i = low
            else:
                i = i.get_next()

            temp = i.get_value()
            i.set_value(j.get_value())
            j.set_value(temp)

        j = j.get_next()
    if i is None:
        i = low
    else:
        i = i.get_next()

    temp = i.get_value()
    i.set_value(high.get_value())
    high.set_value(temp)

    size = 0
    node = low
    while node is not None:
        size += 1
        node = node.get_next()
    return (i, size)
