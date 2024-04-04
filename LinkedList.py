# ===============================================================
# Name: Eva Deans
# Date: 10/26/23
# Algorithm: n/a
# References: TA Andrew Davison
# ===============================================================
class Node:
    def __init__(self, data):
        """
        Initializes Node.
        """
        self.data = data
        self.next = None

    def __str__(self):
        """
        Returns a string representation of the Node.
        """
        return str(self.data)

class LinkedList:
    def __init__(self):
        """
        Initializes a LinkedList.
        """
        self.head = None
        self.length = 0

    def __iter__(self):
        """
        Allows iterating over the LinkedList.
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
        if self.is_empty():
            self.add(item)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(item)
            self.length += 1

    def pop(self, pos=None):
        """
        Removes the last node from the list (if pos is None) or
        removes the node at position pos.
        """
        previous, current = self.head, self.head
        if self.is_empty() or (pos is not None and pos >= self.length):
            raise IndexError("List index out of range.")
        if pos is not None and pos < 0:
            raise ValueError("Enter a positive integer.")
        if self.size() == 1:
            self.head = None
        elif pos is not None:
            if pos == 0:
                self.head = current.next
            else:
                count = 0
                while count != pos:
                    previous = current
                    current = current.next
                    count += 1
                previous.next = current.next
        else:
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None

        self.length -= 1
        return current

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
                    previous =  current
                    current = current.next
        if not is_found:
            raise ValueError("list.remove(x) x not in list")
        self.length -= 1