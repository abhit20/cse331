import unittest
from AVLTree import AVLTree, sum_update,Node


class TestProject1(unittest.TestCase):
    '''
    def test_left_and_right_rotate(self):

        avl = AVLTree()
        avl.root = Node(3)
        avl.root.left = Node(2, parent=avl.root)
        avl.root.left.left = Node(1, parent=avl.root.left)
        avl.size = 3

        avl.right_rotate(avl.root)

        assert avl.root.value == 2
        assert avl.root.left.value == 1
        assert avl.root.right.value == 3

    def test_insert(self):

        avl = AVLTree()
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 1)
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 7)

        assert avl.root.value == 5
        assert avl.root.height == 2

        assert avl.root.left.value == 1
        assert avl.root.left.height == 1

        assert avl.root.left.right.value == 3
        assert avl.root.left.right.height == 0

        assert avl.root.right.value == 10
        assert avl.root.right.height == 1

        assert avl.root.right.left.value == 7
        assert avl.root.right.left.height == 0


        avl2 = AVLTree()
        avl2.insert(avl2.root, 3)
        avl2.insert(avl2.root, 2)
        avl2.insert(avl2.root, 1)
        avl2.insert(avl2.root, 4)
        avl2.insert(avl2.root, 5)

        assert avl2.root.value == 2
        assert avl2.root.height == 2

        assert avl2.root.left.value == 1
        assert avl2.root.left.height == 0

        assert avl2.root.right.value == 4
        assert avl2.root.right.height == 1

        assert avl2.root.right.left.value == 3
        assert avl2.root.right.left.height == 0

        assert avl2.root.right.right.value == 5
        assert avl2.root.right.right.height == 0


        avl3 = AVLTree()
        avl3.insert(avl3.root, 1)
        avl3.insert(avl3.root, 5)
        avl3.insert(avl3.root, 2)
        avl3.insert(avl3.root, 9)
        avl3.insert(avl3.root, 10)
        avl3.insert(avl3.root, 20)
        avl3.insert(avl3.root, 7)

        assert avl3.root.value == 9
        assert avl3.root.height == 3

        assert avl3.root.left.value == 2
        assert avl3.root.left.height == 2

        assert avl3.root.left.left.value == 1
        assert avl3.root.left.left.height == 0

        assert avl3.root.left.right.value == 5
        assert avl3.root.left.right.height == 1

        assert avl3.root.left.right.right.value == 7
        assert avl3.root.left.right.right.height == 0

        assert avl3.root.right.value == 10
        assert avl3.root.right.height == 1

        assert avl3.root.right.right.value == 20
        assert avl3.root.right.right.height == 0

    def test_search(self):
        avl = AVLTree()

        avl.insert(avl.root, 30)
        avl.insert(avl.root, 20)
        avl.insert(avl.root, 40)
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 25)
        avl.insert(avl.root, 35)
        avl.insert(avl.root, 50)

        assert avl.search(avl.root, 10) == avl.root.left.left
        assert avl.search(avl.root, 50) == avl.root.right.right
        assert avl.search(avl.root, 20) == avl.root.left
    '''
    def test_remove(self):

        avl = AVLTree()

        avl.insert(avl.root, 9)
        avl.insert(avl.root, 6)
        avl.insert(avl.root, 14)
        avl.insert(avl.root, 4)
        avl.insert(avl.root, 8)
        avl.insert(avl.root, 11)
        avl.insert(avl.root, 18)

        avl.remove(avl.root, 9)

        assert avl.root.value == 8
        assert avl.root.left.value == 6
        assert avl.root.left.left.value == 4
        #assert avl.root.left.right.value == 8
        assert avl.root.right.value == 14
        assert avl.root.right.left.value == 11
        assert avl.root.right.right.value == 18
        '''
        avl1 = AVLTree()
    
        avl1.insert(avl1.root, 10)
        avl1.insert(avl1.root, 5)
        avl1.insert(avl1.root, 15)
        avl1.insert(avl1.root, 1)
        avl1.insert(avl1.root, 7)
        avl1.insert(avl1.root, 13)
        avl1.insert(avl1.root, 19)

        avl1.remove(avl1.root, 7)
        assert avl1.root.left.right == None
        avl1.remove(avl1.root, 1)
        assert avl1.root.left.left == None
        avl1.remove(avl1.root, 5)
        assert avl1.root.value == 15
        assert avl1.root.left.value == 10
        assert avl1.root.right.value == 19
        assert avl1.root.left.right.value == 13
        
        avl2 = AVLTree()

        avl2.insert(avl2.root, 9)
        avl2.remove(avl2.root, 9)

        avl3 = AVLTree()

        avl3.insert(avl3.root, 9)
        avl3.insert(avl3.root, 6)
        avl3.remove(avl3.root, 9)

        avl4 = AVLTree()
        avl4.remove(avl4.root,9)
        '''
    '''
    def test_traversals(self):
        avl = AVLTree()

        avl.insert(avl.root, 14)
        avl.insert(avl.root, 7)
        avl.insert(avl.root, 21)
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 17)
        avl.insert(avl.root, 25)

        gen1 = avl.preorder(avl.root)
        gen2 = avl.postorder(avl.root)
        gen3 = avl.inorder(avl.root)
        gen4 = avl.breadth_first(avl.root)

        pre = [14, 7, 3, 10, 21, 17, 25]
        post = [3, 10, 7, 17, 25, 21, 14]
        inorder = sorted(post)
        bfs = [14, 7, 21, 3, 10, 17, 25]

        for i in range(7):
            assert next(gen1, None).value == pre[i]
            assert next(gen2, None).value == post[i]
            assert next(gen3, None).value == inorder[i]
            assert next(gen4, None).value == bfs[i]

    def test_depth_height(self):
        avl = AVLTree()

        assert avl.depth(4) == -1

        avl.insert(avl.root, 21)
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 32)
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 16)
        avl.insert(avl.root, 27)
        avl.insert(avl.root, 39)

        assert avl.depth(21) == 0
        assert avl.depth(5) == 2
        assert avl.depth(10) == 1
        assert avl.depth(30) == -1

        assert avl.height(avl.root) == 2
        assert avl.height(avl.root.left) == 1

    def test_min_and_max(self):
        avl = AVLTree()

        avl.insert(avl.root, 10)
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 15)
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 8)
        avl.insert(avl.root, 12)
        avl.insert(avl.root, 18)

        assert avl.min(avl.root).value == 3
        assert avl.max(avl.root).value == 18
    '''
    def test_sum_update(self):
        avl = AVLTree()

        """
        Structure of initial tree:
              10
             /  \
            8   12
           / \  / \
          7  9 11  13 
        """
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 8)
        avl.insert(avl.root, 12)
        avl.insert(avl.root, 7)
        avl.insert(avl.root, 9)
        avl.insert(avl.root, 11)
        avl.insert(avl.root, 13)

        sum_update(avl.root, 0)

        """
        Structure of final tree:

              46
             /  \
            25   63
           / \   / \
          13 36 55  70
        """
        x = avl.inorder(avl.root)
        sol = [13, 25, 36, 46, 55, 63, 70]

        #for i in range(7):
            #assert next(x, None).value == sol[i]
    '''
    def your_test_here(self):

        avl = AVLTree()
        assert avl.root is None
    '''
if __name__ == "__main__":
    unittest.main()
