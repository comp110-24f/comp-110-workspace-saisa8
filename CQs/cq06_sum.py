"""Summing the elements of a list using different loops."""

__author__: str = "730750404"


def w_sum(vals: list[float]) -> float:
    # adds up all the elements in the list using a while loop
    index: int = 0
    # we need an index for while loops, or else we'll get an infinite loop
    sum_1: float = 0.0
    while index < len(vals):
        sum_1 += vals[index]
        index += 1
    return sum_1


def f_sum(vals: list[float]) -> float:
    # adds up all the elements in the list using a for loop
    sum_2: float = 0.0
    for digit in vals:
        # built in index with for loops!
        sum_2 += digit
    return sum_2


def f_range_sum(vals: list[float]) -> float:
    # adds up all the elements in the list using a for loop with range
    sum_3: float = 0.0
    for digit in range(0, len(vals)):
        # loop will "step through" every index from 0 to the end of the list
        sum_3 += digit
    return sum_3


print(w_sum([1.1, 0.9, 1.0]))
print(f_sum([1.1, 0.9, 1.0]))
print(f_range_sum([1.1, 0.9, 1.0]))
