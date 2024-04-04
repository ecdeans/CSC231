# ===============================================================
# Name: Eva Deans
# Date: 9/29/23
# Algorithm: n/a
# References: TA Andrew Davison
# ===============================================================

class Stack:

    def __init__(self):
        """
        Class constructor.
        """
        self.__stack = []

    def push(self, item):
        """
        Adds item to the top of the stack.
        :parameters: item to go on stack
        """
        self.__stack.append(item)

    def pop(self):
        """
        Removes and returns the top item on the stack.
        :return: top item
        """
        if not self.is_empty(): # check if empty before trying to remove
            return self.__stack.pop()

    def peek(self):
        """
        Returns the top item on the stack, but does not remove it.
        :return: top item
        """
        if not self.is_empty(): # check if empty before trying to remove
            return self.__stack[-1]

    def is_empty(self):
        """
        Returns True if the stack is empty, False otherwise.
        :return: boolean
        """
        return len(self.__stack) == 0

    def size(self):
        """
        Returns the number of items on the stack.
        :return: int length of stack
        """
        return len(self.__stack)