'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    count = 0

    def recurr(word):
        if len(word) < 2:
            return
        if word[-2:] == "th":
            nonlocal count
            count = count + 1
            recurr(word[:-2])
        else:
            recurr(word[:-1])
    recurr(word)
    return count
