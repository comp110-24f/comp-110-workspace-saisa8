"""EX03 - Wordle - A game where the user tries to guess the program's secret word."""

__author__: str = "730750404"


def input_guess(secret_word_len: int) -> str:
    """Takes the secret word length and compares it with user's inputted word."""
    user_guess_length = str(input(f"Enter a {secret_word_len} character word: "))
    # using the f-string format makes it easier to concatenate strings with non-strings
    # and is the more efficient coding
    while len(user_guess_length) != secret_word_len:
        # loop for while the user's guess is not the length of secret word
        user_guess_length = str(
            input(f"That wasn't {secret_word_len} chars! Try again: ")
        )
    return user_guess_length


def contains_char(word_guess: str, looking_for: str) -> bool:
    """Returns whether a certain character can be found in the desired word."""
    assert len(looking_for) == 1
    contains_index: int = 0
    char_count: int = 0
    while contains_index < len(word_guess):
        # loop that goes through each character of the word and compares it to
        #  the character we're looking for
        if looking_for == word_guess[contains_index]:
            char_count += 1
        contains_index += 1
    if char_count == 0:
        # this means that the character we're looking for does not exist
        # within the inputted word
        return False
    else:
        # opposite; this means that the character we're looking for does exist
        # within the inputted word
        return True


def emojified(user_word_guess: str, secret_word: str) -> str:
    """Returns a string of emojis that reflects the user's accuracy in
    guessing the secret word."""
    assert len(user_word_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # named constants for our emojis!
    emojified_index: int = 0
    # we will add to this empty string so that all the emojis go on the same line
    emoji_string: str = ""
    while emojified_index < len(user_word_guess):
        # another loop that goes through each character of the inputted word
        if user_word_guess[emojified_index] == secret_word[emojified_index]:
            emoji_string = emoji_string + GREEN_BOX
            # character is correct and in right place, green emoji
        elif contains_char(
            word_guess=secret_word, looking_for=user_word_guess[emojified_index]
        ):
            emoji_string = emoji_string + YELLOW_BOX
            # character is in the secret word but in wrong place, yellow emoji
        else:
            emoji_string = emoji_string + WHITE_BOX
            # character is not in secret word, white emoji
        emojified_index += 1
    return emoji_string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_index: int = 1
    # turn_index keeps track of how many turns user has taken
    win: bool = False
    while turn_index <= 6 and not win:
        # while less than or at 6 turns and we have not won so far
        print(f"=== Turn {turn_index}/6 ===")
        guess: str = input_guess(secret_word_len=len(secret))
        emoji_output: str = emojified(secret, guess)
        print(emoji_output)
        # tying all the programs together!!!
        if guess == secret:
            win = True
        else:
            turn_index += 1
    if win:
        print(f"You won in {turn_index}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    """Makes it possible to run this Python program as a module and makes it
    possible for other modules to import this function and reuse it."""
    main(secret="codes")
