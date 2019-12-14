'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

'''
split string, slice off from 0-1, test if that equals 'th'.
if it does concat the number 1 to it
'''

def count_th(word):
    
    count = 0
    if len(word) < 2:
        return 0

    if word[:2] == 'th':
        count += 1

    count += count_th(word[1:])
    return count
