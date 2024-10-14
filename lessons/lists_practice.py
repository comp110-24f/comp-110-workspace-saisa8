"""Basic syntax of lists."""

# create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# print(my_numbers)

# string analogy
# my_name: str = "" #literal
# my_name: str = str() #constructor

# adding a value to a list
my_numbers.append(1.5)
my_numbers.append(2.3)
# print(my_numbers)

# creating an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# subscription notation/indexing
# print(game_points[2])
last_game: int = game_points[2]
# print(last_game)

# modifying by index
# bc lists are mutable
game_points[1] = 72
print(game_points)

# getting the length
len(game_points)

# removing an item
game_points.pop(1)
print(game_points)
game_points.append(94)
print(game_points)


# function name: display
# parameter: list of integers
# RV: none
# print every element in the input list
# call display on game_points
# hint: we did something very similar to this with strings + while loops :)
"""def display(int_list: list[int]) -> None:
    Display all elements of int_list
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)"""
