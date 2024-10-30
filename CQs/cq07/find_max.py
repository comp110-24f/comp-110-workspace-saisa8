"""Practice with while loops, lists, and unit tests."""

__author__: str = "730750404"


def find_and_remove_max(max_list: list[int]) -> int:
    # finds the largest value in the list and removes every instance of it
    if len(max_list) == 0:
        # edge case that returns a -1 if the inputted list is empty
        return -1
    else:
        index_1: int = 0
        # index for while loop #1
        index_2: int = 0
        # index for while loop #2
        max_int: int = max_list[0]
        # can't start at 0 b/c that wouldn't work if the list was only negative numbers
        # the first index is a better starting point
        while len(max_list) > index_1:
            # this loop finds the largest integer in the list and returns it
            if max_list[index_1] > max_int:
                # this if statement redefines max_int if the value of max_list is
                # larger than the current value
                max_int = max_list[index_1]
            index_1 += 1
            # if the value of index_1 didn't change, we would have an infinite loop
        while len(max_list) > index_2:
            # this loop removes every instance of max_int within the list
            if max_list[index_2] == max_int:
                # this if statement removes the integer at its specific index if it is
                # equal to max_int
                max_list.pop(index_2)
            index_2 += 1
            # if the value of index_2 didn't change, we would have an infinite loop
        return max_int
