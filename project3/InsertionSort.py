"""
PROJECT 3 - Quick/Insertion Sort
Name: Abhinav Thirupathi
PID: A57671702
"""


def _insertion_wrapper(insertion_sort):
    """
    DO NOT EDIT
    :return:
    """
    def insertion_counter(*args, **kwargs):
        if args[0].size > 1:
            args[0].c += 1
        insertion_sort(*args, **kwargs)
    return insertion_counter

# ------------------------Complete function below---------------------------
@_insertion_wrapper
def insertion_sort(dll, low, high):
    """
    Sort a doubly linked list from the given low and high points using insertion sort
    :param dll: the doubly linked list that is being sorted - used for insertion_sort wrapper
    :param low: node to start sorting at (inclusive)
    :param high: node to end sorting at (inclusive)
    :return: None - DLL class should be altered
    """
    lst = []
    node = dll.get_head()
    while node is not None:
        lst.append(node.get_value())
        node = node.get_next()

    for i in range(1, len(lst)):
        j = i
        # Insert numbers[i] into sorted part
        # stopping once numbers[i] in correct position
        while j > 0 and lst[j] < lst[j - 1]:
            # Swap numbers[j] and numbers[j - 1]
            temp = lst[j]
            lst[j] = lst[j - 1]
            lst[j - 1] = temp
            j = j - 1

    k = 0
    node = dll.get_head()
    while node is not None:
        node.set_value(lst[k])
        k += 1
        node = node.get_next()
