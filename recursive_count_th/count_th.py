'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    start = 0
    end = len(word) - 1

    th = "th"

    if start and end == 0:
        return None

    if not word.find(th):
        return None
    else:
        return count_th(word[1:])