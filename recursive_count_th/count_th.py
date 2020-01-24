'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #base case, word length is too short
    if len(word) < 2:
        return  0 # can't have a "th" with less than 2 characters now can we?
    else:
        # we found a "th"
        if word[:2] == "th":
            return count_th(word[1:]) + 1
        else: # we don't find a "th"
            return count_th(word[1:])

