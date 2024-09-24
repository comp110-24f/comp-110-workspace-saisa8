"""EX02 - Chardle - A cute step towards Wordle."""

__author__: str = "73075404"


def input_word() -> str:
    """Asks the user for their word, and determines whether it is five characters."""
    user_word_guess = str(input("Enter a 5-character word: "))
    if len(user_word_guess) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return user_word_guess


# used to have return in an else statement, but you don't need that when you have exit()


def input_letter() -> str:
    """Asks user for their letter, and determines whether it is only one character."""
    user_letter_guess = str(input("Enter a single letter: "))
    if len(user_letter_guess) != 1:
        print("Error: Character must be a single character.")
        exit()
    return user_letter_guess


# used to have return in an else statement, but you don't need that when you have exit()


def contains_char(word: str, letter: str) -> None:
    """Searches through the word for instances of the letter, counts the number of
    times the letter was used, then returns the locations of the letter in the word."""
    print("Searching for " + letter + " in " + word)
    count: int = 0
    # i almost used a loop here! would've been more efficient but i understand
    # this exercise is for practicing if statements
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    # used to have "if word[0] != letter and word[1] != letter and" etc.
    # but using the count function is much more effective and uses less space
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Ties all the functions together so only this one must be called."""
    contains_char(word=input_word(), letter=input_letter())
    # this is just what we had to type before, but as a function that is easier to call


if __name__ == "__main__":
    """Makes it possible to run this Python program as a module and makes it possible
    for other modules to import this function and reuse it."""
    main()
