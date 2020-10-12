'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    #base case, stop counting
    if len(word) < 2:
        return 0
    
    #if found return 1 and count from the next letters
    if word[:2] == "th":
        return 1+ count_th(word[2:])
    #else return 0 and count from the next letters
    else:
        return 0 + count_th(word[1:])
