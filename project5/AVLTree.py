import random as r
import copy

class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        :param height: the height of the node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value and self.height == other.height

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)

class AVLTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result
            
    ### Implement/Modify the functions below ###

    def insert(self, node, value):
        """
        Inserts in a value and node of the (sub)tree the node will be added into
        :param node: Root of the (sub)tree the node will be added into
        :param value: Value to be added
        :return:
        """
        if self.root is None:
            self.root = Node(value)
            self.size += 1
        else:
            if self.search(node, value).value != value:
                if value < node.value:  # we know that `node` cannot be None - so it's safe to check its value!
                    if node.left is not None:
                        self.insert(node.left, value)  # the recursive call is done only when `node.left` is not None
                    else:
                        node.left = Node(value, parent=node)  # direct assignment
                        self.size += 1
                else:
                    if node.right is not None:
                        self.insert(node.right, value)
                    else:
                        node.right = Node(value, parent=node)  # direct assignment
                        self.size += 1

        self.rebalance(node)

    def remove(self, node, value):
        """
        Removes the value at the tree rooted at the node
        :param node: Root of the (sub)tree the node
        :param value: Value to remove from the tree
        :return:
        """
        node = self.search(node, value)
        return self._remove_node(node)

    def _remove_node(self, node):
        """
        Remove the node from the tree
        :param node: Node to remove
        :return:
        """
        if node is None:
            return False
        # Parent needed for rebalancing
        parent = node.parent

        # Case 1: Internal node with 2 children
        if node.left is not None and node.right is not None:
            # Find successor
            succNode = node.left
            while succNode.right is not None:
                succNode = succNode.right
            # Copy the value from the node
            node.value = succNode.value
            # Recursively remove successor
            self._remove_node(succNode)
            # Nothing left to do since the recursive call will have rebalanced
            return True

        # Case 2: Root node (with 1 or 0 children)
        elif node is self.root:
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right

            if self.root:
                self.root.parent = None
            return True

        # Case 3: Internal with left child only
        elif node.left is not None:
            self._replace_child(parent, node, node.left)

        # Case 4: Internal with right child only OR leaf
        else:
            self._replace_child(parent, node, node.left)

        self.size -= 1

        # node is gone. Anything that was below node that has persisted is already correctly
        # balanced, but ancestors of node may need rebalancing.
        node = parent
        while node is not None:
            self.rebalance(node)
            node = node.parent
        return True

    def search(self, node, value):
        """
        Search the value at the root of a given node
        :param value: Value to search for
        :param node: A node which is the root of a given tree or subtree
        :return: the node with the given value if found, else returns the potential parent node
        """
        if self.root is None:
            return None
        cur = node
        while cur is not None:
            if (value == cur.value) or (self.height(cur) == 0):
                return cur
            elif value < cur.value:
                if cur.left is None:
                    return cur
                cur = cur.left
            else:
                if cur.right is None:
                    return cur
                cur = cur.right

    def inorder(self, node):
        """
        Inorder method of traversal of the tree rooted at the node
        :param node: Node to start the traversal at
        :return: Generator object of the tree
        """
        if node is None: return
        yield from self.inorder(node.left) if node.left else ()
        yield node
        yield from self.inorder(node.right) if node.right else ()

    def preorder(self, node):
        """
        Preorder method of traversal of the tree rooted at the node
        :param node: Node to start the traversal at
        :return: Generator object of the tree
        """
        if node is None: return
        yield node
        yield from self.preorder(node.left) if node.left else ()
        yield from self.preorder(node.right) if node.right else ()

    def postorder(self, node):
        """
        Postorder method of traversal of the tree rooted at the node
        :param node: Node to start the traversal at
        :return: Generator object of the tree
        """
        if node is None: return
        yield from self.postorder(node.left) if node.left else ()
        yield from self.postorder(node.right) if node.right else ()
        yield node

    def breadth_first(self, node):
        """
        Breadth-first method of traversal of the tree rooted at the node
        :param node: Node to start the traversal at
        :return: Generator object of the tree
        """
        if node is None: return

        queue = []
        queue.append(node)

        while len(queue) > 0:
            yield queue[0]
            node1 = queue.pop(0)

            if node1.left: queue.append(node1.left)
            if node1.right: queue.append(node1.right)

    def depth(self, value):
        """
        Finds the depth of the node with the given value
        :param value: value of the node
        :return: Returns the depth of the node with the given value
        """
        search = self.search(self.root, value)
        if search is None or search.value is not value:
            return -1

        count = 0
        if search.value == value:
            while search.parent is not None:
                count += 1
                search = search.parent
            return count

    def height(self, node):
        """
        Finds the height of the tree rooted at the given value
        :param node: The node at which tree is rooted at
        :return: height of the tree rooted at the given node
        """
        if node is None:
            return -1
        else:
            leftHeight = -1
            if node.left is not None:
                leftHeight = node.left.height
            rightHeight = -1
            if node.right is not None:
                rightHeight = node.right.height
            node.height = max(leftHeight, rightHeight) + 1
        return node.height

    def min(self, node):
        """
        Finds the min of the tree rooted at the given node
        :param node: Tree rooted at the given node
        :return: Minimum of the tree rooted at the given node
        """
        if node is None: return None
        if node.left is None: return node
        return self.min(node.left)

    def max(self, node):
        """
        Finds the max of the tree rooted at the given node
        :param node: Tree rooted at the given node
        :return: Maximum of the tree rooted at the given node
        """
        if node is None: return None
        if node.right is None: return node
        return self.max(node.right)

    def get_size(self):
        """
        Find the number of nodes in the AVL Tree
        :return: Returns the number of nodes in the AVL Tree
        """
        return self.size

    def get_balance(self, node):
        """
        Gets the balance factor of the node
        :param node: Node for whch balanced factor is checked
        :return: Balance factor of the node passed in
        """
        if not node:
            return 0
        else:
            leftHeight = -1
            if node.left is not None:
                leftHeight = node.left.height
            rightHeight = -1
            if node.right is not None:
                rightHeight = node.right.height
        return leftHeight - rightHeight

    def _set_child(self, parent, whichChild, child):
        """
        Sets a node as the parent's left or right child
        :param parent: Parent node of the subtree
        :param whichChild: Left of right child
        :param child: Child to be replaced with
        :return: False if which child is not 'left' or 'right', else True
        """
        if whichChild is not "left" and whichChild is not "right":
            return False
        if whichChild is "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent

        self.height(parent)
        return True

    def _replace_child(self, parent, currentChild, newChild):
        """
        Replaces one of a node's existing child with a new value
        :param parent: Parent node of the subtree
        :param currentChild: Current child of the subtree
        :param newChild: New child of the subtree
        :return: True if replacement is successful, else false
        """
        if parent.left is currentChild:
            return self._set_child(parent, "left", newChild)
        elif parent.right is currentChild:
            return self._set_child(parent, "right", newChild)
        return False

    def left_rotate(self, root):
        """
        Performs an AVL left rotation on the subtree rooted at root
        :param root: Root of the subtree
        :return: Root of the new subtree
        """
        rightLeftChild = root.right.left
        if root.parent is not None:
            self._replace_child(root.parent, root, root.right)
        else:
            self.root = root.right
            self.root.parent = None
        self._set_child(root.right, "left", root)
        self._set_child(root, "right", rightLeftChild)

        self.height(root.parent)
        return root.parent

    def right_rotate(self, root):
        """
        Performs an AVL right rotation on the subtree rooted at root
        :param root: Root of the subtree
        :return: Root of the new subtree
        """
        leftRightChild = root.left.right
        if root.parent is not None:
            self._replace_child(root.parent, root, root.left)
        else:
            self.root = root.left
            self.root.parent = None
        self._set_child(root.left, "right", root)
        self._set_child(root, "left", leftRightChild)

        self.height(root.parent)
        return root.parent

    def rebalance(self, node):
        """
        Rebalances the subtree rooted at node, if needed
        :param node: The subtree rooted at the node
        :return: Root of the new, balanced subtree
        """
        self.height(node)
        balance = self.get_balance(node)
        if balance == -2:
            if (self.get_balance(node.right) == 1):
                # Double rotation case
                self.right_rotate(node.right)
            return self.left_rotate(node)
        elif balance == 2:
            if (self.get_balance(node.left) == -1):
                #Double rotation case
                self.left_rotate(node.left)
            return self.right_rotate(node)
        return node

def sum_update(root, total):
    """
    Replaces the keys in the tree with the sum of keys and fix the tree to be correct
    :param root: Root of a binary search tree
    :param total: Total parameter is used for keeping track of a running total for keys greater than a specific key
    :return: No return
    """
    avl = AVLTree()
    avl.root = root
    total = total

    max_node = avl.max(avl.root.right)
    node = max_node

    while node.parent is not None:
        node.value += total
        total = node.value
        if node.left is not None:
            node.left.value += total
            total = node.left.value
        node = node.parent

    node.value += total
    total = node.value

    max_node = avl.max(avl.root.left)
    node = max_node

    while node.parent is not None:
        node.value += total
        total = node.value
        if node.left is not None:
            node.left.value += total
            total = node.left.value
        node = node.parent
    m_node = avl.max(avl.root)
    swap_branches(avl.root)

def swap_branches(root):
    """
    Swap the branches of the AVL tree
    :param root: The root of the avl tree
    :return:
    """
    if root is not None:
        if root.left is not None and root.right is not None:
            root.left, root.right = root.right, root.left
            swap_branches(root.right)
            swap_branches(root.left)
        if root.left is not None:
            root.left, root.right = None, root.left
        if root.right is not None:
            root.left, root.right = root.right, None
