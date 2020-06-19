'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    """
    Takes in a word/phrase and returns the amount of times 'th' occurs.
    
    Parameters:
            word (str): a word, phrase, sentence, etc. that is a string.
            
    Returns:
            count (int): number of times that 'th' occurs in the input.
    """
    # if length of the string is less than two characters, it won't contain any
    # instances of 'th' so return 0
    if len(word) < 2:
        return 0
    # TBC - first two characters of string are 'th', so add one and recur
    #. starting at the next index
    elif word[0:2] == 'th':
        return 1 + count_th(word[1:])
    # Otherwise, recur starting at the next index over
    else:
        return count_th(word[1:])
    
    
    
# word = 'THis thing goes fourth'
# print(count_th(word))
