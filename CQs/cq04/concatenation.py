__author__: str = "730750404"

"""Concatenates two variables together."""


def concat(input_one=str, input_two=str) -> str:
    return input_one + input_two


# global variables
word1: str = "happy"
word2: str = "tuesday"

# built-in function that ensures that the print will only run when running
# concatenation.py, not when concat() is imported to other programs
if __name__ == "__main__":
    print(concat(word1, word2))
