'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # not going to find th in a word less than 2
    if (len(word) < 2): 
        return 0

    # count starts at zero cause no values can be found
    count = 0

    # if the first and second letters are 'th', increase counter
    if word[0] == 't' and word[1] == 'h':
        count = 1

    # slide word over and recurse, 
    count = count + count_th(word[1:])

    return count
