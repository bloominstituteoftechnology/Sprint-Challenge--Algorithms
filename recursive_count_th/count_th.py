'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word)<2: # if word length is less than 2 return 0 as we are looking for 'th'
        return 0
    if word[0:2] == 'th':              # use recursion to repeated checks for 'th'
        return count_th(word[1:]) + 1
    
    return count_th(word[1:])

