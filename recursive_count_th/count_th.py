'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if word is less than the count for 'th', then it does not contain it, return
    if len(word) < len('th'):
        return 0
    # if the first two letters are == to 'th' return 1 & continue with the remaining letters
    elif word[:2] == 'th':
        return count_th(word[2:]) + 1
    # otherwise continue with the next letter in word
    else:
        return count_th(word[1:])
