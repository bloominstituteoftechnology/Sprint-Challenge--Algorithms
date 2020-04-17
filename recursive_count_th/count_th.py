'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

word = "thethe"


def count_th(word):

    # Base cases
    if word == "":
        return 0
    if len(word) == 2:
        if word[0] == "t" and word[1] == "h":
            return 1
        else:
            return 0

    new_word = word[1:]

    if word[0] == "t" and word[1] == "h":
        return count_th(new_word) + 1
    else:
        return count_th(new_word)

