"""EX05 - List Unit Tests -
Building more functions using lists to practice using unit test."""

__author__: str = "730750404"


def only_evens(input_list: list[int]) -> list[int]:
    # given a list, returns a new list containing only the even numbers from original
    evens_list: list[int] = []
    # empty list that we will append to so that original list is not mutated
    index: int = 0
    while index < len(input_list):
        if input_list[index] % 2 == 0:
            # if there is no remainder when divided by 2, that means index is even
            evens_list.append(input_list[index])
        index += 1
        # if we didn't have this, index would stay same and infinite loop would happen
    return evens_list


def sub(sub_list: list[int], start_index: int, end_index: int) -> list[int]:
    # given a list and 2 indexes, returns a new subset of the list between the 2 indexes
    output_sub: list[int] = []
    # empty list that we will append to so that original list is not mutated
    if len(sub_list) == 0 or start_index >= len(sub_list) or end_index == 0:
        # edge case stuff! should return empty list if these are true
        return output_sub
        # putting a return here will ensure that program quits out of the function
    for index in range(0, len(sub_list)):
        # must use for loop w/ range because we are referencing the indexes,
        # not elements of list
        if index >= start_index and index < end_index:
            # if index is between the start_index and end_index, append to empty list
            output_sub.append(sub_list[index])
    return output_sub


def add_at_index(add_list: list[int], desired_int: int, index_location: int) -> None:
    # modifies the list to add an inputted int at the inputted desired index
    if index_location < 0 or index_location > len(add_list):
        # edge case stuff! raises IndexError for all this stuff
        # program automatically quits function
        raise IndexError("Index is out of bounds for the input list")
    add_list.append(0)
    # must append a 0 to the end of the list to make space
    # if not, last index of og list will disappear from the mutated list
    count = len(add_list) - 1
    while count > index_location:
        # goes thorugh and moves every index down one to make room for desired_int
        add_list[count] = add_list[count - 1]
        count -= 1
    add_list[index_location] = desired_int
