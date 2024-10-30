"""EX06 - Dictionary Utility Functions -
Practice with dictionary functions!"""

__author__: str = "730750404"


def invert(og_invert: dict[str, str]) -> dict[str, str]:
    """Takes a dict of str (both key and value) and returns a dict of strs,
    but with the key and values inversed."""
    new_invert: dict[str, str] = {}
    # initializing empty dict that we will add stuff to
    for idx in og_invert:
        if og_invert[idx] in new_invert:
            # if the value at idx in original list already exists as key in the new dict
            # . originally had this after line 18, but that doesn't work bc the value at
            # idx will already be added to dict as a key by the if statement, so the
            # error will always be raised.
            raise KeyError("Sorry, not possible!")
            # raises an error and exits out of the program
        new_invert[og_invert[idx]] = idx
        # adds the value of og dict at idx as key to new dict with idx of og list as
        # its value
    return new_invert


def count(count_data: list[str]) -> dict[str, int]:
    """Takes a list of str as an argument and returns a dict that tracks each str in
    the list and how many times it was mentioned."""
    result_dict: dict[str, int] = {}
    # initializing empty dict that we will add stuff to
    for idx in range(0, len(count_data)):
        if count_data[idx] in result_dict:
            # if the str is already in dict
            result_dict[count_data[idx]] += 1
            # increase the value of the str's key by 1
        else:
            # if the str is not yet in dict
            result_dict[count_data[idx]] = 1
            # add str to dict as a key with a value of 1
    return result_dict


def favorite_color(color_data: dict[str, str]) -> str:
    """Takes a dict of str (both key and value) defining each person's favorite color
    and returns the str of the most popular color."""
    all_colors: list[str] = []
    # initializing empty list that we will append stuff to
    for idx in color_data:
        all_colors.append(color_data[idx])
        # adding all the values of the dict color_data to all_colors
        # so that we can use it with count()
    post_count: dict[str, int] = count(all_colors)
    # using count() on the colors and storing the dict it returns in post_count
    highest_color_count: int = 0
    # we can use 0 for this initial comparison int bc there will never be
    # a negative number for the color count
    highest_color_name: str = ""
    # initializing empty str that we will add stuff to
    for idx in post_count:
        # similar to max() from ex04, looping through the dict to find the highest value
        if post_count[idx] > highest_color_count:
            # if the count is higher than 0 (if idx = 0)/the last highest number in dict
            highest_color_count = post_count[idx]
            # redefining highest_color_count to have the count of most popular color
            # not returning this, but need it for comparison
            highest_color_name = idx
            # redefining highest_color_name to have the name of most popular color
            # will be returning this
    return highest_color_name


def update_attendance(
    og_attendance: dict[str, list[str]], day: str, student: str
) -> None:
    """Takes an original dict with a key as the day of the week and value as a list of
    students who were present, and then an updated str of the day str of the student
    who was present, mutates the dict to include updated keys/values.
    """
    if day in og_attendance:
        # if the day already exists as a key for the dict
        if student not in og_attendance[day]:
            # if the student has not been marked as present on
            # a specific day that is already in the dict
            og_attendance[day].append(student)
            # append the student to the list that is a value for that day's key
    else:
        # if the day does not already exist as a key within the dict
        og_attendance[day] = [student]
        # create a new key for that day that has the student in the list as a value


def alphabetizer(alpha_list: list[str]) -> dict[str, list[str]]:
    """Takes a list[str] and returns a dict with a key of the words' first letters and
    a value of each word in the list that starts with that letter."""
    post_alpha: dict[str, list[str]] = {}
    # initializing empty dict that we will add stuff to
    for idx in range(0, len(alpha_list)):
        just_word: str = alpha_list[idx]
        first_letter: str = just_word[0].lower()
        # the method .lower() returns the lower case of the str
        # this is useful if we get two words that start with the same letter as
        # arguments but they have different casing, this method helps recognize them as
        # the same letter instead of as different characters
        if first_letter in post_alpha:
            # this is if first letter of the word in the argument is already in our dict
            post_alpha[first_letter].append(alpha_list[idx])
            # appending word at idx to dict as value for exisiting first letter key
        else:
            # this is if first letter of word in argument is not already in our dict
            post_alpha[first_letter] = [just_word]
            # creating new key of the first letter w a value of the word
    return post_alpha
