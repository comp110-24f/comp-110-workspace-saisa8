"""EX04 - list Utility Functions -
Reverse engineering algorithms to deepen our understanding of them."""

__author__: str = "730750404"


def all(all_list: list[int], all_int: int) -> bool:
    # takes list and an int, checks to see if all values of the list are the same as int
    # returns true if they are, false if not
    all_bool: bool = False
    # by using a bool variable, we can ensure the entire list is looped through
    for idx in range(0, len(all_list)):
        if all_list[idx] == all_int:
            all_bool = True
            # if we put a return here, then if just the first value of the list is the
            # same as int, the function will return true
        else:
            all_bool = False
            return all_bool
            # this placement of return ends the for loop immediately if a single value
            # of the list doesn't match the int
    return all_bool


def max(max_list: list[int]) -> int:
    # returns the largest integer of the list
    if len(max_list) == 0:
        # raises a ValueError if the list is empty
        raise ValueError("max() arg is an empty List")
    max_int: int = max_list[1]
    # originally i had max_int = 0, but this wouldn't work if the list was only
    # negative numbers. doing max_int = max_list[1] means that the function should work
    # correctly for any list.
    for idx in range(0, len(max_list)):
        if max_list[idx] > max_int:
            max_int = max_list[idx]
            # redefining max_int so it is equal to the largest integer of the list
    return max_int


def is_equal(equal_list_1: list[int], equal_list_2: list[int]) -> bool:
    # compares two lists to see if they have all the same values in the same exact order
    # this concept is called deep equality! both lists must be the same in essence,
    # not in memory (different ids in the heap, same content).
    if len(equal_list_1) == 0 and len(equal_list_2) == 0:
        return True
        # if both equal_list_1 and equal_list_2 are empty, then they are equal!
    if len(equal_list_1) != len(equal_list_2):
        return False
        # if the two lists have different lengths, they cannot be equal
    else:
        is_equal_bool: bool = False
        # once again, by using bool variable we can ensure entire list is looped through
        for idx in range(0, len(equal_list_1)):
            if equal_list_1[idx] == equal_list_2[idx]:
                is_equal_bool = True
                # if we put a return here, then if just the first value of equal_list_1
                # is the same as equal_list_2, the function will return true
            else:
                is_equal_bool = False
                return is_equal_bool
        return is_equal_bool


def extend(extend_list_1: list[int], extend_list_2: list[int]) -> None:
    # mutate extend_list_1 by appending the values of extend_list_2 to the end of it
    for idx in range(0, len(extend_list_2)):
        extend_list_1.append(extend_list_2[idx])
        # very simple, just appends every integer of extend_list_2 to extend_list_1
