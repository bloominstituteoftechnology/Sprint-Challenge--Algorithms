'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

    
    # TBC
    
def count_th(word):
    if len(word) < 2:
        return 0
    elif word[:2] == 'th':
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
    pass

    #base cases:
    #word needs to be at least
    #as big as th- or 2 letters.
    #if less leave early
    #we need to check if from the
    #first to the 2nd is th.
    #we can leave early if so
    #and recurisvely keep counting
    #else were going to return
    #the word.
    
