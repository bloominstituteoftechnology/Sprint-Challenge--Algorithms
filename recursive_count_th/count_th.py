'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Iterate until a substring is impossible
    if len(word) < 2:
        return 0
    
    # Case of letters to iterate over
    # Using a slice as input for a recursive function will
    # Slice the slice, iterating through a string
    if word[0:2] == 'th':
        # Returning 1 + output of recurred function
        # Will keep running tally of occurrences that are
        # Continually added
        # word[1:] basically just slices the input successively
        return 1 + count_th(word[1:])
    else:
        # Continue to perform recursion, but do not increase tally
        return count_th(word[1:])
