'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):

    count = 0
    if word == str.split(''):
        return 0

    if word == count:
        return 1 + count_th(str(word.split('')))
       
    else:
        return 0 






    