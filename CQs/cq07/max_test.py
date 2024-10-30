from CQs.cq07.find_max import find_and_remove_max

"""3 unit tests for find_max. Ensures that the program is returning expected values."""

__author__: str = "730750404"


def test_return_value() -> None:
    # use case unit test that checks whether the returned value is correct
    # which means that the largest integer of the list is returned
    return_list: list[int] = [8, 10, 13, 15, 2, 4]
    assert find_and_remove_max(return_list) == 15


def test_mutate_list() -> None:
    # use case unit test that checks whether the list is mutated correctly
    # which means that every instance of the largest integer of the list is removed
    mutate_list: list[int] = [4, 2, 6, 7, 1, 7, 2]
    find_and_remove_max(mutate_list)
    # i originally forgot to call the function! the program insisted that i was trying
    # to assert [4, 2, 6, 7, 1, 7, 2] == [4, 2, 6, 1, 2] since list wasn't being mutated
    # without the function being called.
    assert mutate_list == [4, 2, 6, 1, 2]


def test_unconventional_input() -> None:
    # edge case unit test that checks whether the function has the correct return for
    # unconventional input which means that a -1 is returned when the inputted list is
    # empty
    empty_list: list[int] = []
    assert find_and_remove_max(empty_list) == -1


"""def test_gradescope() -> None:
    # this replicates the unit test in gradescope that says "Part 1. find_and_remove_max
    # should remove all instances of max value from list of ints."
    # although this unit test works in my program, it is not working within gradescope
    # so as of right now, i have not received points for this part.
    gradescope_list: list[int] = [1, 8, 2, 3, 3]
    find_and_remove_max(gradescope_list)
    assert gradescope_list == [1, 2, 3, 3]"""
