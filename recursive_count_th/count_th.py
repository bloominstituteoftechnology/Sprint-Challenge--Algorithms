'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    """Counts the amounts of 'th' in given string recursively. Base case is an empty string or a string that is less than length of 'th' (2 characters). After checking the first two characters (or length of 'th'), it'll will cut off another substring, and then check the rest."""

    sub = word[0:len('th')]
    rest = word[len('th')-1:]

    if len(word) < 2:
        return 0
    elif sub == 'th':
        return 1 + count_th(rest)
    else:
        return count_th(rest)
