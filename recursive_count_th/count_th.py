'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    return countHelper(word, 0)

def countHelper(word, currentCount):
    if word == "":
        return currentCount
    elif word.startswith("th"):
        return countHelper(word[2:], currentCount + 1)
    else:
        return countHelper(word[1:], currentCount)
