'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# if len(word) == 0 or < 'th' stop recursion
# if first 2 letters != 'th' remove them
# else just remove them and add 1

def count_th(word):
    if len(word) == 0 or len(word) < len('th'):
        return 0
    if word[:2] != 'th':
        return count_th(word[1:])
    else:
        return count_th(word[1:]) + 1