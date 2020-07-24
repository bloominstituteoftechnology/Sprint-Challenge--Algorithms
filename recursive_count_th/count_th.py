'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # check to see if we are at the end of the word.. 
    # can't possibly  contain "th" if we have less than
    # two characters
    if len(word) < 2:
        return 0

    # if the first two letters are "th" return 1 to up 
    # the  count AND the rest of the word without 
    if word[:2] == "th":
        return 1 + count_th(word[2:])

    # if the first two letters are not "th", then we need
    # to just move over once and return the rest of the word
    else:
        return count_th(word[1:])
