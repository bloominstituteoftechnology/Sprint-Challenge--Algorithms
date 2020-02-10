'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    count = 0
    for x in range(len(word)):
        if word[x] == 't' and word[x+1] == 'h':
            count += 1
    return count

    if word == 0:
        return 0
    
    pass


print(count_th("thdddtghtdh"))