'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Needs a base case to determine when the function stops
    if len(word) < 2:
        return 0

    # Needs to modify word to exclude letters that have been tested
    else:  # Else states that it is greater than or equal to two.
        if word[:2] == 'th':
            return 1 + count_th(word[2:])
    # runs the function again but without the first letter
    return count_th(word[1:])
