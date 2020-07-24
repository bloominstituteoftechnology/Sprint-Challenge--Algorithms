'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    #Base case
    if len(word) < 2: #Case is either 1 or 0 and cannot have the string in it
        return 0

    if word [:2] == 'th':
        return count_th(word[2:]) +1 #start at the 2 index because if it is th, then word[1:] would start with h and be false.
    else:
        return count_th(word[1:])
