"""A game where the user tries to guess the secret number."""

__author__: str = "730750404"


def guess_a_number() -> None:
    """Takes the user's guess as input, then returns whether they were correct."""
    secret: int = 7
    guess = int(input("Guess a number: "))
    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


# By using elif, we can optimize our code and make it more efficient.
# the int in int(input) is for variable we are storing, not the str appears to the user

if __name__ == "__main__":
    """Good practice!"""
    guess_a_number()
