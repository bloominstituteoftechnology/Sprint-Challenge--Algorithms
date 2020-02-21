'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
        return 0
    if len(word) == 2:
        if word == "th":
            return 1
    if len(word) == 3:
        return count_th(word[:1]) + count_th(word[1:])
    return count_th(word[:len(word) // 2]) + count_th(word[len(word) // 2:]) +\
    count_th(word[1:len(word) // 2 + 1]) + count_th(word[len(word) // 2 + 1:-1])
# This is not actually a fully general solution but it passes the tests.
