'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    count = 0
    if word.find("th") == -1:
        return count
    elif len(word) > 0:
        word.find("th")
        return 1 + count_th(word.replace("th", " ", 1))
