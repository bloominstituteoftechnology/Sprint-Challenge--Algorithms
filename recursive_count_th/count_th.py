'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # set up our properties
    th = "th"
    len_th = len(th) # get the length of th
    len_word = len(word) # get the length of our comparison word
    
    # base case.  If we've decrimented word to 0 or less than "th" return.
    if len_word == 0 or len_word < len_th:
        return 0
    
    # check to see if we have a match using slices.
    if word[0 : len_th] == th:
        # if we have a match increment our counter by 1 and advance 1 character in our comparison word.  Call our count_th function.
        return count_th(word[len_th-1:]) + 1
    
    # if we don't have a match, avdvance our search by one character and then recurse.
    return count_th(word[len_th-1:])
