'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    if (len(word) < 2): 
        return 0
    count = 0
    if word[0] == 't' and word[1] == 'h':
        count = 1
    count = count + count_th(word[1:])

    return count
