# ===============================================================
# Name: Eva Deans
# Date: 9/29/23
# Algorithm: n/a
# References: TA Andrew Davison
# ===============================================================

class Deque:

    def __init__(self):
        """
        Class constructor.
        """
        self.__deque = []

    def is_empty(self):
        """
        Returns True if the queue is empty, False otherwise.
        :return: boolean
        """
        return len(self.__deque) == 0

    def size(self):
        """
        Returns the number of items in the queue.
        :return: int length of stack
        """
        return len(self.__deque)

    def add_front(self, item):
        """
        Adds item to the front of the deque.
        :parameters: item to add
        """
        self.__deque.insert(0, item)

    def add_rear(self, item):
        """
        Adds item to the rear of the deque.
        :parameters: item to add
        """
        self.__deque.append(item)

    def remove_front(self):
        """
        Removes and returns the item at the front of the deque.
        :return: front item
        """
        if not self.is_empty(): # check if empty before trying to remove
            return self.__deque.pop(0)

    def remove_rear(self):
        """
        Removes and returns the item at the rear of the deque.
        :return: rear item
        """
        if not self.is_empty(): # check if empty before trying to remove
            return self.__deque.pop()