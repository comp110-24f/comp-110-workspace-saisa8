__author__: str = "730750404"

"""Assembles characters of variables into pairs of coordinates"""


def get_coords(xs=str, ys=str) -> None:
    count_xs: int = 0
    while len(xs) > count_xs:
        # loops through the characters in the xs variable +
        # allows the nested loop to occur everytime a new xs character is looped through
        count_ys: int = 0
        # initializing count_ys must be in the first while loop or else only the first
        # character of xs will be looped through
        while len(ys) > count_ys:
            # loops through the characters in the ys variable
            print("(" + xs[count_xs] + "," + ys[count_ys] + ")")
            # if we don't add to the count, the loop will go on forever
            count_ys += 1
        # if we don't add to the count, the loop will go on forever
        count_xs += 1


# built-in function that ensures that the print will only run when running
# coordinates.py, not when get_coords() is imported to other programs
if __name__ == "__main__":
    get_coords(xs="12", ys="34")
