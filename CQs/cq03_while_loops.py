"""Searches through phrase and returns amount of times a certain character is used."""

__author__: str = "730750404"


def num_instances(phrase: str, search_char: str) -> int:
    # loops through each character of phrase and checks whether is character of interest
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count


# learned that you can use an if statement without an else! did not know that honestly
# use of relative reassignment operators makes code more efficient

print(num_instances(phrase="SignLanguageRules", search_char="g"))
# code originally wasn't returning anything in terminal because forgot to print function
