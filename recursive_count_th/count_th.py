'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # check if 'th' is even possible with len < 2
    if len(word) <2:
        # if len < 2 it's not possible
        return 0
    # TBC - first two characters of str are 'th', 
    # add one and recurse
    elif word[0 : 2] == 'th':
        return 1 + count_th(word[1:])
    # if not, recurse at the next index
    else:
        return count_th(word[1:])