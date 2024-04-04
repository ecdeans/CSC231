# ===============================================================
# Name: Eva Deans
# Date: 9/15/23
# Algorithm: N/A
# References: TA Andrew Davison, Runestone Textbook, pythontutor.com

# Title: Fraction Class
# Purpose: The purpose of this program is to practice
# classes, functions and test files.
# ===============================================================

# Note: Because the fractions get reduced in __init__ I didn't
# use .reduce() in any of the math operators

class Fraction:

    def __init__(self, numerator, denominator):
        '''
        Inits Fractions with a numerator and denominator, and simplifies them.
        '''
        # check that input is type int
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError("Values must be of type integer")
        # checks denominator not 0
        if denominator == 0:
            raise ValueError("Divide by zero error")

        # set up variables
        self.__numerator = numerator
        self.__denominator = denominator

        # simplify given fractions
        self.reduce()

    def __str__(self):
        '''
        Prints Fraction as a string.
        '''

        if self.__denominator == 1: # checks to see if fraction is a whole number
            return str(self.__numerator)
        return f"{self.__numerator}/{self.__denominator}"

    def get_numerator(self):
        '''
        Returns the numerator of a fraction.
        '''
        return self.__numerator

    def get_denominator(self):
        '''
        Returns the denominator of a fraction.
        '''
        return self.__denominator

    def set_numerator(self, new_num):
        '''
        Sets the numerator of a fraction.
        '''
        if not isinstance(new_num, int): # checks to see if input int
            raise TypeError("Must be type integer")
        self.__numerator = new_num

    def set_denominator(self, new_den):
        '''
        Sets the denominator of a fraction.
        '''
        if not isinstance(new_den, int): # checks to see if input int
            raise TypeError("Must be type integer")
        if new_den == 0: # checks denominator not 0
            raise ValueError("Divide by zero error")
        self.__denominator = new_den

    def reduce(self):
        '''
        Puts a fraction to it's simplest form.
        '''
        gcd = self.__calc_gcd() # gets gcd to find simplest form
        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd

    def __calc_gcd(self):
        '''
        Finds the greatest common factor of a fraction.
        '''
        a = max(self.__numerator, self.__denominator)
        b = min(self.__numerator, self.__denominator)

        while b != 0: # loop to reduce as much as possible
            temp = b
            b = a % b
            a = temp

        return abs(a)

    # ## SPECIAL MATH OPERATORS:

    def __neg__(self):
        '''
        Negates a fraction.
        '''
        if self.__numerator and self.__denominator > 0: # should negation be negative
            return Fraction(-self.__numerator, self.__denominator)
        elif self.__numerator or self.__denominator < 0: # should negation be positive
            return Fraction(abs(self.__denominator), abs(self.__denominator))
        else: # is numerator 0
            return Fraction(self.__numerator, self.__denominator)

    def __add__(self, other):
        '''
        Adds together two fractions.
        '''
        new_den = self.__denominator * other.__denominator
        new_num = (other.__denominator * self.__numerator) + (other.__numerator * self.__denominator)
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        '''
        Subtracts one fraction from another.
        '''
        new_den = self.__denominator * other.__denominator
        new_num = (other.__denominator * self.__numerator) - (other.__numerator * self.__denominator)
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        '''
        Multiplies two fractions together.
        '''
        new_num = self.__numerator * other.__numerator
        new_den = self.__denominator * other.__denominator
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        '''
        Divides one fraction from another.
        '''
        new_num = self.__numerator * other.__denominator
        new_den = self.__denominator * other.__numerator
        return Fraction(new_num, new_den)

    ## BOOLEAN OPERATORS:

    def __eq__(self, other):
        '''
        Determines whether two fractions are equal.
        '''
        num1 = self.__numerator * other.__denominator
        num2 = self.__denominator * other.__numerator
        return num1 == num2

    def __ne__(self, other):
        '''
        Determines whether two fractions are NOT equal.
        '''
        num1 = self.__numerator * other.__denominator
        num2 = self.__denominator * other.__numerator
        return num1 != num2

    def __lt__(self, other):
        '''
        Determines whether a fraction is less than another.
        '''
        num1 = self.__numerator * other.__denominator
        num2 = other.__numerator * self.__denominator

        return num1 < num2

    def __le__(self, other):
        '''
        Determines whether a fraction is less than or equal to another.
        '''
        num1 = self.__numerator * other.__denominator
        num2 = other.__numerator * self.__denominator

        return num1 <= num2

    def __gt__(self, other):
        '''
        Determines whether a fraction is greater than another.
        '''
        num1 = self.__numerator * other.__denominator
        num2 = other.__numerator * self.__denominator

        return num1 > num2

    def __ge__(self, other):
        '''
        Determines whether a fraction is greater than or equal to another.
        '''
        num1 = self.__numerator * other.__denominator
        num2 = other.__numerator * self.__denominator

        return num1 >= num2


    def __repr__(self):
        '''
        Returns printable representation of Fraction object.
        '''
        return f"Fraction(numerator={self.__numerator}, denominator={self.__denominator}"


