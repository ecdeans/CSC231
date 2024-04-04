# ===============================================================
# Name: Eva Deans
# Date: 9/29/23
# Algorithm: n/a
# References: TA Andrew Davison
# ===============================================================

class Queue:

    def __init__(self):
        """
        Class constructor.
        """
        self.__queue = []

    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise.
        :return: boolean
        """
        return len(self.__queue) == 0

    def size(self):
        """
        Returns the number of items on the stack.
        :return: int length of stack
        """
        return len(self.__queue)

    def enqueue(self, item):
        """
        Adds item to the rear of the queue.
        :parameters: item to add to queue
        """
        self.__queue.append(item)

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.
        :return: item at front of queue
        """
        if not self.is_empty(): # check if empty before trying to remove
            return self.__queue.pop(0)
