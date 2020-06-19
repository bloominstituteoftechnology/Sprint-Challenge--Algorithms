'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Check to see that the length of the word is not less than 'th'. If it is, it definitely doesn't contain it.
    if len(word) < len('th'):
        return 0
    # If the first two letters are equal to 'th', return 1 and carry on with the remaining letters
    elif word[:2] == 'th':
        return count_th(word[2:]) + 1
    # Otherwise continue with the next letter in 'word'
    else:
        return count_th(word[1:])
