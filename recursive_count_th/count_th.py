'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    if not word:
        return 0
    if len(word) < 2:
        return 0
    if word[0] == 't' and word[1] == 'h':
        return 1 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])
    # TBC
    
    # pass
