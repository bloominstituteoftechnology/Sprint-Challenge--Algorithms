'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # base case,if word.count < 2, no way to contain `th`,return 0 and stop the function
    if len(word) < 2:
        return 0
    # simply check the first two character is `th`,give it a plus 1 and moving on
    elif word[0:2] == "th":
        return 1 + count_th(word[1:])
    else: # simply moving on
        return count_th(word[1:])
