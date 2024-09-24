"""Practicing my conditionals."""


def less_than_10(num: int) -> None:
    """Tell us if num < 10."""
    dub: int = num * 2
    dub = dub - 1  # 14
    print(dub)  # 13
    if num < 10:  # check if this is true
        print("Small number!")  # "then" block
    else:
        print("Big number!")
    print("This is the end of the function!")


less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """Return a message based on if allarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp110!"
    else:
        return "Keep sleeping. You deserve it. :)"


# print(wake_up(alarm=False))


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter is first character of word."""
    if word[0] == letter:
        return "Match!"
    else:
        return "No match!"


print(check_first_letter(word="Happy", letter="h"))
