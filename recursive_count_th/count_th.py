"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    # if length of word is 0, return 0
    # if length of word is < "th" return 0
    if len(word) == 0 or len(word) < len("th"):
        return 0

    # check the first 2 indices
    # if 2 letters do not equal "th", recurse with a new word removing the first letter
    if word[:2] != "th":
        return count_th(word[1:])
    else:
        # if the 2 letters = "th" remove those two letters and add 1 for the occurrence
        return count_th(word[2:]) + 1
