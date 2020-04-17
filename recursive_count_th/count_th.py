'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if word[:2] == "th":
        return count_th(word[1:]) + 1
    elif len(word) < 2:
        return 0
    return count_th(word[1:])