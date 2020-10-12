'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # UPER
    # establish the base case
    if len(word) == 0:
        return 0

    # slice the string according to inclusion of "th"
    # count

print(count_th("th"))