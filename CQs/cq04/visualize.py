from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

"""Allows user to use get_coords and concat in the same program with 
the same global variables."""

__author__: str = "730750404"

# global variables that we use in concat() and get_coords()
x: str = "123"
y: str = "abc"

# calling both functions
print(concat(x, y))
get_coords(x, y)
