# ===============================================================
# Name: Eva Deans
# Date: 9/15/23
# Algorithm: <When required>
# References: TA, Textbook, pythontutor.com
# ===============================================================

from fraction import Fraction

def main():
    f = Fraction
    print("Creating fractions: (2,4), (-1/4), (1,2), (4, 1) and (1,8)")
    frac1 = Fraction(2,4)
    frac2 = Fraction(-1,4)
    frac3 = Fraction(1,2)
    frac4 = Fraction(4,1)
    frac5 = Fraction(1,8)

    print("\n__str__ method:")
    print(f"Fraction 1 should read 1/2: {frac1}")

    print("\nget_numerator method:")
    print(f"Here is the numerator for frac1: {f.get_numerator(frac1)}")

    print("\nget_denominator method:")
    print(f"Here is the denominator for frac1: {f.get_denominator(frac1)}")

    print("\nget_numerator method:")
    print(f"The numerator for frac3 was: {f.get_numerator(frac5)}")
    f.set_numerator(frac5, 3)
    print(f"Here is the new numerator for frac3: {f.get_numerator(frac3)}")

    print("\nset_denominator method:")
    print(f"The denominator for frac3 was: {f.get_denominator(frac5)}")
    f.set_denominator(frac5, 4)
    print(f"Here is the new denominator for frac3: {f.get_denominator(frac3)}")

    print("\nreduce method:")
    print(f"Here is 2/4 reduced: {frac1}")
    print("The reduce method is in the __init__ function.")

    print("\n__calc_gcd method:")
    print("Cannot be called because it is private. Only called inside other methods.")

    print("\n__neg__ method:")
    print(f"Here is {frac1},{frac2}, and {frac4} negated: {f.__neg__(frac1)}, {f.__neg__(frac2)}, {f.__neg__(frac4)}")

    print("\n__add__ method:")
    print(f"Here is {frac1} + {frac4}: {frac1 + frac4}")

    print("\n__sub__ method:")
    print(f"Here is {frac4} - {frac1}: {frac4 - frac1}")

    print("\n__mul__ method:")
    print(f"Here is {frac4} * {frac1}: {frac4 * frac1}")

    print("\n__truediv__ method:")
    print(f"Here is {frac4} / {frac1}: {frac4 / frac1}")

    print("\n__eq__ method:")
    print(f"Are {frac1} and {frac3} equal? {frac1 == frac3}")

    print("\n__ne__ method:")
    print(f"Are {frac1} and {frac5} not equal? {frac1 != frac5}")

    print("\n__lt__ method:")
    print(f"Is {frac1} less than {frac5}? {frac1 < frac5}")

    print("\n__le__ method:")
    print(f"Is {frac1} less than or equal to {frac5}? {frac1 <= frac5}")

    print("\n__gt__ method:")
    print(f"Is {frac1} more than {frac5}? {frac1 > frac5}")

    print("\n__ge__ method:")
    print(f"Is {frac1} more than or equal to {frac5}? {frac1 >= frac5}")





if __name__ == '__main__':
    main()