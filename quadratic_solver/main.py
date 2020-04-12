"""Quadratic equation."""
from math import sqrt


def find_roots(a: int, b: int, c: int):
    """
    Function which finds intersection points of given quadratic equation (y = ax^2 + bx + c).

    The function returns 2 integers, if given equation has two different solutions.
    It returns one integer, if given equation has two equal solutions.
    It also returns one integer, when variable a is zero and function intersects x-axis.
    It returns None, if given equation has no real solutions.
    """
    if a == 0:
        x = -c / b
        print(f"Solution is {x}")
        return x

    d = b ** 2 - (4 * a * c)

    if d < 0:
        print("No solutions")
        return None
    elif d == 0:
        x = (-b + sqrt(d)) / (2 * a)
        print(f"Solution is {x}")
        return x

    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)

    print(f"Solutions are {x1} and {x2}")
    return x1, x2
