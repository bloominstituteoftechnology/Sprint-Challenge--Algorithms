'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # base case
    if len(word) <= 0:
        return 0
        # if the 2 spots contain th save it for later and adds one on the way back up
    if word[:2] == "th":
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])

    # okay here is what you know about recursion it replaces the loop so all logic needs to come before the recursive call.
    # the logic needs to work each time and then build its self back up.
