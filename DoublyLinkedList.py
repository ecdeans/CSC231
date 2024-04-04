# ===============================================================
# Name: Eva Deans
# Date: 10/26/23
# Algorithm: n/a
# References: TA Andrew Davison
# ===============================================================

# Besides adding a few more things to init, the only things that
# really changed from the linkedlist class was the code in the pop
# method, so the bulk of comments are there.

class Node:
    def __init__(self, data):
        """
        Initializes Node.
        """
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        """
        Returns a string representation of the Node.
        """
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        """
        Initializes a DoublyLinkedList.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        """
        Allows iterating over the DoublyLinkedList.
        """
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def is_empty(self):
        """
        Checks if the list is empty.
        """
        return self.head is None

    def size(self):
        """
        Returns the number of items in the list.
        """
        return self.length

    def add(self, item):
        """
        Adds an item to the head of the list.
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self, item):
        """
        Adds an item to the tail of the list.
        """
        new_node = Node(item)
        if self.is_empty(): # if list empty
            self.tail = new_node
            self.head = new_node
        else: # if list has nodes
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self, pos=None):
        """
        Removes the last node from the list (if pos is None) or
        removes the node at position pos.
        """
        if self.is_empty(): # check to see if list empty
            raise IndexError("List is empty.")

        if pos is not None:
            if pos < 0 or pos >= self.length: # see if its of valid range
                raise IndexError("List index out of range.")
            current = self.head
            for _ in range(pos): # iterates through list moving current node
                current = current.next
        else:
            current = self.tail # if no pos, pop last node

        data = current.data

        if current is self.head:
            # if the node to remove is head of the list
            self.head = current.next
        if current is self.tail:
            # if the node to remove is tail of the list
            self.tail = current.prev
        if current.next:
            # if there's a next node, update previous pointer
            current.next.prev = current.prev
        if current.prev:
            # if there's a previous node, update next pointer
            current.prev.next = current.next

        self.length -= 1 # reduce length of the list

        return data

    def search(self, item):
        """
        Searches for an item in the list.
        """
        is_found, current = False, self.head
        if not self.is_empty():
            while not is_found and current is not None:
                if current.data == item:
                    is_found = True
                else:
                    current = current.next
        return is_found

    def remove(self, item):
        """
        Removes the item from the list.
        """
        previous, current, is_found = self.head, self.head, False
        if self.is_empty():
            raise ValueError("list.remove(x) x not in list")
        if self.head.data == item:
            is_found = True
            self.head = self.head.next
        else:
            while not is_found and current is not None:
                if current.data == item:
                    is_found = True
                    previous.next = current.next
                else:
                    previous = current
                    current = current.next
        if not is_found:
            raise ValueError("list.remove(x) x not in list")
        self.length -= 1
