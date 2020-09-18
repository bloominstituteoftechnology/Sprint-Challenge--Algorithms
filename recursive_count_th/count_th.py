'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    

    # If the length of word is less than 2, then it will be impossible for the word to contain 'th', so we just return 0
    if len(word) < 2:
        return 0
    
    # If the word has th, then we add one and start at the end index
    elif word[0:2] == 'th':
        return 1 + count_th(word[1:])
    # If it doesn't keep iterating
    else:
        return count_th(word[1:])
    

