'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences
of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < 2:   # word has to be more than 1 letter
        return 0

    # check 2 letters at a time for th
    elif (word[0:2] == 'th'):
        return count_th(word[1:]) + 1

    else:
        return count_th(word[1:])


# test to see if the count works
print(count_th('Helpthetheory'))
