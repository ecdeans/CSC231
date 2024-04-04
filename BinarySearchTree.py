# ===============================================================
# Name: Eva Deans
# Date: 10/26/23
# Algorithm: n/a
# References: TA Andrew Davison, Nex Humphrey,
# https://www.prepbytes.com/blog/heap/height-of-a-complete-binary-tree-or-binary-heap-with-n-nodes/#:~:text=As%20mentioned%20earlier%2C%20the%20height,the%20height%20by%20only%201.
#
# Note: Honestly had no idea where to start with the turtle part of
# the assignment, so didn't include the file
# ===============================================================


from math import log2

class BinaryNode:
    """
    Represents a node in a binary tree.
    """

    def __init__(self, data, parent=None):
        """
        Initializes a BinaryNode.
        """
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        """
        Returns a string representation of the node, and its children.
        """
        return "[%s, %s, %s]" % (self.left, str(self.data), self.right)

    def display(self):
        """
        Displays the binary tree visually.
        """
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """
        Returns list of strings, width, height, and horizontal coordinate
        of the root.
        """
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def has_left(self):
        """
        Checks if the node has a left child.
        """
        return self.left

    def has_right(self):
        """
        Checks if the node has a right child.
        """
        return self.right

class BinarySearchTree:
    """
    Represents a binary search tree.
    """

    def __init__(self):
        """
        Initializes an empty BinarySearchTree.
        """
        self.root = None
        self._size = 0
        self._height = 0
        self._max_height = 0

    def __contains__(self, item):
        """
        Checks if the tree contains a specific item.
        """
        return bool(self._get(item, self.root))

    def __len__(self):
        """
        Returns the number of nodes in the tree.
        """
        return self._size

    def _get(self, item, current):
        """
        Helper function to recursively search for an item in the tree.
        """
        if not current:
            return
        if current.data == item:
            return current
        if item < current.data:
            return self._get(item, current.left)
        else:
            return self._get(item, current.right)

    def current_height(self):
        """
        Returns the current height of the tree.
        """
        return self._height

    def max_height(self):
        """
        Returns the maximum height the tree has reached.
        """
        return self._max_height

    def _update_height(self):
        """
        Updates the height of the tree based on the current size.
        """
        self._height = int(log2(self._size + 1))
        self._max_height = max(self._max_height, self._height)

    def insert(self, item):
        """
        Inserts an item into the tree.
        """
        if not self.root:
            self.root = BinaryNode(item)
            self._size += 1
        else:
            self._insert(item, self.root)

    def _insert(self, item, current):
        """
        Helper function to recursively insert an item into the tree.
        """
        if item == current.data:
            raise ValueError(f"{item} already in Tree.")
        elif item < current.data:
            # go to left
            if current.has_left(): # continue to left
                self._insert(item, current.left)
            else: # insert
                current.left = BinaryNode(item, current)
                self._size += 1
                self._update_height()
        elif item > current.data:
                # go to left
            if current.has_right(): # continue to left
                self._insert(item, current.right)
            else: # insert
                current.right = BinaryNode(item, current)
                self._size += 1
                self._update_height()

    def delete(self, item):
        """
        Deletes an item from the tree.
        """
        node_to_delete = self._get(item, self.root)
        if not node_to_delete:
            raise ValueError(f"{item} not found in Tree.")
        else:
            self._delete(node_to_delete)

    def _delete(self, node):
        """
         Helper function to recursively delete a node from the tree.
        """
        if not node.has_left() and not node.has_right(): # node no children
            parent = node.parent
            if parent: # if node has a parent, update the parent's reference to remove the node
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else: # if  node is the root, set root to None
                self.root = None
            self._size -= 1
            self._update_height()
        elif node.has_left() and node.has_right(): # node 2 children
            # find successor node to replace current node
            successor = self._find_successor(node.right)
            node.data = successor.data
            self._delete(successor) # recursively delete successor node
        else: # node 1 child
            parent = node.parent
            child = node.left if node.has_left() else node.right
            if parent: # if the node has parent, update parent's reference
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child
            else: # if node is the root, update the root to the child and set the child's parent to None
                self.root = child
                child.parent = None
            self._size -= 1
            self._update_height()

    def _find_successor(self, node):
        """
        Finds the successor of a node in the tree.
        """
        while node.left:
            node = node.left
        return node

    def traverse_inorder(self, node=None):
        """
        Traverses the tree in inorder and prints the values.
        """
        if not node:
            current = self.root
        else:
            current = self._get(node, self.root)
            self._inorder(current)

    def _inorder(self, current): # LPR
        """
        Helper function to recursively traverse the tree in inorder.
        """
        if current:
            self._inorder(current.left)
            print(current.data, end=" ")
            self._inorder(current.right)

    def traverse_preorder(self, node=None):
        """
        Traverses the tree in preorder and prints the values.
        """
        if not node:
            current = self.root
        else:
            current = self._get(node, self.root)
            self._preorder(current)

    def _preorder(self, current):  # PLR
        """
        Helper function to recursively traverse the tree in preorder.
        """
        if current:
            print(current.data, end=" ")
            self._preorder(current.left)
            self._preorder(current.right)

    def traverse_postorder(self, node=None):
        """
        Traverses the tree in postorder and prints the values.
        """
        if not node:
            current = self.root
        else:
            current = self._get(node, self.root)
            self._preorder(current)

    def _postorder(self, current): # LRP
        """
        Helper function to recursively traverse the tree in postorder.
        """
        if current:
            self._preorder(current.left)
            self._preorder(current.right)
            print(current.data, end=" ")


