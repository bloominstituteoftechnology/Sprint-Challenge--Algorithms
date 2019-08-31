'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
global count
count = 0

def count_th(word):
    ## if initial word length is less than 2, it returns 0
    if len(word) < 2:
        return 0
    ## if th matches, it increments until word length is less than 2.
    elif word[0] + word[1] == 'th':
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])

# count_th("abcthxyz")
