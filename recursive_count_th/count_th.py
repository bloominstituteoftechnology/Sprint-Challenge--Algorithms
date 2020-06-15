"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    if word == "":
        return 0

    idx = 0
    selection = word[idx : idx + 2]
    occurences = 0

    if selection == "th":
        occurences += 1

    if idx == len(word) - 2:
        return occurences

    return occurences + count_th(word[idx + 1 :])
