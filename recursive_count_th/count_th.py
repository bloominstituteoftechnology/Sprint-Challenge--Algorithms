'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case
    # if the word is an empty string, return 0
    if len(word)==0:
        return 0
    # if the word has only 1 letter
    if len(word)<2: # 2 is the len('th')
        return 0
    
    # recursive case
    # check if the first substring matches
    if word[:2] == 'th':
        return count_th(word[1:]) +1
    
    # otherwise, return the count from the remaining index
    # and repeat
    return count_th(word[1:])

print(count_th('abcthxyz'))