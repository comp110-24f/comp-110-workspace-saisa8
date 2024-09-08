"""My first challenge question in COMP110!"""

__author__ = "730750404"


def mimic(message: str) -> str:
    """Returns a message back to you."""
    return message


def main() -> None:
    """Prints the result of calling mimic."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    """Conditional statement that evaluates whether main() has been fufilled or not."""
    main()
