'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    found_th = 0

    if word.startswith("th", 0, len(word)):
        found_th = 1

    remainder_of_word = word[1:]

    if len(remainder_of_word) == 0:
        return found_th
    else:
        return count_th(remainder_of_word) + found_th