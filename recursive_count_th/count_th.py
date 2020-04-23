"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrence of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    if len(word) < 2:  # skips words with less than 2 characters.
        return 0
    elif word[:2] == 'th':  # checks to see if 'th' is in the first two indexes.
        return 1 + count_th(word[1:])  # Moves to the next index skipping the first
    else:
        return count_th(word[1:])  # just remove the first index of the word w/o incrementing
