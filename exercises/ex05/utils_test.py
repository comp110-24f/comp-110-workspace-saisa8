from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""EX05 - List Unit Tests -
Building more functions using lists to practice using unit test."""

__author__: str = "730750404"


def test_only_evens_mutation() -> None:
    # use case unit test that makes sure list is not mutated
    evens_nonmutated_list: list[int] = [7, 45, 32, 23, 44, 87, 66]
    only_evens(evens_nonmutated_list)
    assert evens_nonmutated_list == [7, 45, 32, 23, 44, 87, 66]


def test_only_evens_return() -> None:
    # use case unit test that checks whether the returned value is correct
    evens_return_list: list[int] = [3, 1, 26, 62, 3, 1, 77, 2, 3, 88]
    assert only_evens(evens_return_list) == [26, 62, 2, 88]


def test_only_evens_edge() -> None:
    # edge case unit test that checks whether the function has the correct return for
    # unconventional inputs; in this case, input and output is empty list
    evens_empty_list: list[int] = []
    assert only_evens(evens_empty_list) == []


def test_sub_mutation() -> None:
    # use case unit test that makes sure list is not mutated
    sub_nonmutated_list: list[int] = [2, 4, 7, 4, 32, 4, 1, 2]
    sub(sub_nonmutated_list, 3, 5)
    assert sub_nonmutated_list == [2, 4, 7, 4, 32, 4, 1, 2]


def test_sub_return() -> None:
    # use case unit test that checks whether the returned value is correct
    sub_return_list: list[int] = [13, 62, 3, 51]
    assert sub(sub_return_list, 2, 4) == [3, 51]


def test_sub_edge() -> None:
    # edge case unit test that checks whether the function has the correct return for
    # unconventional inputs; in this case, input is starting index is greater than
    # ending index and output is empty list
    sub_edge_list: list[int] = [13, 62, 3, 51]
    assert sub(sub_edge_list, 3, 2) == []


def test_add_at_index_mutation() -> None:
    # use case unit test that makes sure list is mutated
    og_add_return_list: list[int] = [65, 55, 43, 21, 23, 88]
    add_return_list: list[int] = [65, 55, 43, 21, 23, 88]
    # same list as the other, but this one will be altered by the function
    add_at_index(add_return_list, 33, 4)
    assert og_add_return_list != add_return_list


def test_add_at_index_return() -> None:
    # use case unit test that checks whether the returned value is correct
    add_return_list: list[int] = [11, 51, 47, 85, 34, 77]
    add_at_index(add_return_list, 52, 4)
    assert add_return_list == [11, 51, 47, 85, 52, 34, 77]


def test_add_at_index_edge() -> None:
    # edge case unit test that checks whether the function has the correct return for
    # unconventional inputs; in this case, input is index is greater than length of
    # list and output is IndexError
    with pytest.raises(IndexError):
        add_edge_list: list[int] = [33, 26, 99, 66, 45, 65]
        add_at_index(add_edge_list, 21, 10)
