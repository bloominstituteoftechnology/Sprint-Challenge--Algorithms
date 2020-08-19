'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # if t and h occur consecutively at the beginning count and return 1 occurence
    if word[0] == 't' and word[1] == 'h':
        # recursive call will search consecutive occurences beginning at the 2nd index of the last word
        # word --> ord --> rd
        return 1 + count_th(word[1:])

    pass
