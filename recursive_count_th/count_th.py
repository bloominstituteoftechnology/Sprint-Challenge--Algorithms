'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # check length of word
    #base case is len(word) <2 return nothing
    if len(word) <2:
        return 0
    #Begin recurssion
    if word[:2] == "th":
    #if found return 1 and keep going
        return 1+ count_th(word[2:])
    #otherwise return 0 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])
