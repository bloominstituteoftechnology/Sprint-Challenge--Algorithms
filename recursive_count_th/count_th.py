'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
th = "th"
def count_th(word):
    # base 
    if len(word) == 0 or len(word) < 2:
        return 0
    if word[0] + word[1] == th:
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])