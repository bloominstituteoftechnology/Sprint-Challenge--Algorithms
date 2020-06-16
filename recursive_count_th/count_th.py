'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


# Your function should take in a single parameter (a string `word`)
def count_th(word):
    # Your function should return a count of how many occurrences of
    # ***"th"*** occur within `word`. Case matters.
    if word.count('th') < 1:
        return 0
    else:
        return word.count('th')
