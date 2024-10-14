"""Mutating functions."""

__author__: str = "730750404"


def manual_append(appending_list: list[int], adding_values: int) -> None:
    # appends values to the given list
    appending_list.append(adding_values)


def double(doubling_list: list[int]) -> None:
    # doubles each value in a list
    index: int = 0
    while len(doubling_list) > index:
        # loops through each value of the list to double it
        doubling_list[index] = doubling_list[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
# both lists were [2, 4, 6] after calling doubl(list_2)
# this is because we are mutating the arguments of list_2
# but that is the same list as list_1 since we set list_2 = list_1
# both list_1 and list_2 are just referencing the list of [1, 2, 3];
# unlike other data types
# so when we mutate list_2, it mutates the original list both are referencing
# so when we print both lists after calling double(list_2), both lists show doubling
# b/c they reference the same list which we mutated!!!
