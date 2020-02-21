'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    start = word[0:2]
    rest = word[1:]
    if len(word) <= 2 and word == 'th':
        return 1
    elif len(word) <= 2:
        return 0
    else:
        return count_th(start) + count_th(rest)
