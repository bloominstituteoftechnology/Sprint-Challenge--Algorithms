'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # bottom out here - we've trimmed word down to less than two characters.
    if len(word) < 2:
        return 0
    else:
        if word[:2] == 'th': # if the first 2 leters are 'th', increment and count on the remaining letters
            return 1 + count_th(word[2:])
        else: # otherwise, drop the first character and count on the remaining characters.
            return count_th(word[1:])
