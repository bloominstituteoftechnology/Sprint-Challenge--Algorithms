'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    str = 'th'
    if str not in word:
        return 0

    if str in word:
        word = word.replace(str, 'xd', 1)
        return count_th(word) + 1