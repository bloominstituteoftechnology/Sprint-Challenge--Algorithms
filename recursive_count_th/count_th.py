'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if "th" not in word:
        return 0
    else:
        return 1 + count_th(word[word.index("th") + 2:])
