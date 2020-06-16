"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur
within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    """
    Counts the number of appearances of the lowercase substring 'th' in a
    string 'word'.
    """

    index = word.find('th')

    # Base case - no such substrings found.
    if index == -1:
        return 0

    # Recursive case - one substring found; look for additional substrings in
    # what remains of the input string.
    return count_th(word[index + 2:]) + 1
