"""Quadratic equation."""
from math import sqrt


def solve_equation():
    x2 = x = c = ""

    while len(x2) == 0:
        x2 = input("Insert square member(x^2)")

    while len(x) == 0:
        x = input("Insert member(x)")

    while len(c) == 0:
        c = input("Insert free member(c)")

    try:
        x2 = int(x2)
        x = int(x)
        c = int(c)
    except ValueError as e:
        print("Entered value isn't a number!")
        return

    return find_roots(x2, x, c)


def find_roots(a, b, c):
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


if __name__ == "__main__":  # <- This line is needed for automatic testing
    solve_equation()
