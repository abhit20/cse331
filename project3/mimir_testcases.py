import unittest
from Project3.QuickSort import quick_sort
from Project3.DoublyLinkedList import DLL
from Project3.InsertionSort import insertion_sort


class TestProject1(unittest.TestCase):

    def test_accessors(self):

        dll = DLL([])

        assert dll.get_size() == 0
        assert dll.get_head() is None
        assert dll.get_tail() is None

        orig = [6, 5, 4, 3, 2, 1]

        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 4)

        assert dll.get_size() == 6
        assert dll.get_head().get_value() == 1
        assert dll.get_tail().get_value() == 6

        orig = [1, 1, 1, 0, 1, 1, 1]

        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 0)

        assert dll.get_size() == 7
        #assert dll.get_head().get_value() == 0
        #assert dll.get_tail().get_value() == 1

    def test_insertion(self):
        orig = [6, 1, 4, 7, 3, 5, 10, 8, 9, 2]

        dll = DLL(orig)
        insertion_sort(dll, dll.get_head(), dll.get_tail())
        assert dll == DLL(sorted(orig))

    def test_quick_sort(self):
        orig = [9, 2, 7, 1, 3, 6, 4, 5]

        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 0)

        assert dll == DLL(sorted(orig))

    def test_guick_insertion(self):
        orig = [20, 18, 4, 2, 5, 7, 13, 10, 11, 3, 1, 17, 16, 9, 6, 8, 15, 12, 14, 19]

        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 15)

        assert dll == DLL(sorted(orig))
    
    def test_application(self):
        dll = DLL([1, 2, 2, 3, 3, 3])
        dll.count_unique()

        assert dll == DLL([1, 2, 2, 3, 3])



if __name__ == "__main__":
    unittest.main()
