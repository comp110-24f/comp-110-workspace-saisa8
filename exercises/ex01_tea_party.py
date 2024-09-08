"""Tells user cost of a tea party based on number of guests."""

__author__: str = "730750404"


def main_planner(guests: int) -> None:
    """Ties all the functions together to deliver the output to the user."""
    print("A Cozy Tea Party For " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# str() must be used because strings can only be concatenated with other strings.
# I'm not sure why print function from line 11 automatically spreads to lines 11-16 -
# - I think it makes the code easier to comprehend, or the original line was too long. -
# - The function seems to run fine with the code like this so I guess I'll keep it!


def tea_bags(people: int) -> int:
    """Returns the number of teabags per guest."""
    return people * 2


def treats(people: int) -> int:
    """Returns the number of treats per guest based on how much tea they drink."""
    return int(tea_bags(people=people) * 1.5)


# In order to use the return value of one function in the definition of another one, -
# - we must ensure that our arguments remain global, hence why we have to do -
# - people (for the function treats) = people (for the function tea_bags).


def cost(tea_count: int, treat_count: int) -> float:
    """Returns the cost of all the tea bags and treats needed."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# Makes the Python program runnable! MUST come AFTER ALL function definitions.
