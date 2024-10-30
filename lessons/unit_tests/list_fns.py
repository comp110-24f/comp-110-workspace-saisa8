def get_first(input: list[str]) -> str:
    # returns first element
    if len(input) == 0:
        return ""
    return input[0]


def remove_first(input: list[str]) -> None:
    # removes first element
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    # removes and returns first element
    first_elem: str = input[0]
    input.pop(0)
    return first_elem


print(get_and_remove_first(["apple", "3", "yay"]))
