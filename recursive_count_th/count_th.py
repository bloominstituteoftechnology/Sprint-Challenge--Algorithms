'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    th = 0
    if word.find("th") == -1:
        return th
    else:
        word.find("th")
        return 1 + count_th(word.replace("th", " ", 1))
