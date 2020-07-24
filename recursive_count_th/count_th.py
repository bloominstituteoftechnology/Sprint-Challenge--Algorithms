'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Base case - If the word length is less that two chars, it can't have "th" occur within it, therefore we return 0
    if len(word) < 2:
        return 0
    # Proceed and check first 2 characters of word, see if "th" occurs, if it does: recurse the function (with
    # the word from index position 1 onwards) + 1. If "th" doesn't occur, then recurse the function in the same way, but don't add
    # + 1, since we didn't find a match.
    elif word[:2] == "th":
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])

