'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

## return the length of a word set character < 2 or zero if th doesnt exist 
## define what we are looking for th in lower case at 
## we only want two characters 
## return the istances of th as a string  if just a indivual charcater return nothing.
## We can add multiple th's to gether in one word by just adding it to the count *
def count_th(word):
    if len(word) < 2: 
        return 0

    if word[:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return 0 + count_th(word[1:])
