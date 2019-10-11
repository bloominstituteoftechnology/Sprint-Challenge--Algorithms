'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
from textwrap import wrap

def count_th(word):
    
    if word == 'th':
        return 1
    elif word != 'th':
        return 0
    else:
        #word_wrap_list = wrap(word, 2)
        #s1 = sum(map(count_th, wrap(word,2)))
        #s2 = sum(map(count_th, wrap(word[1:],2)))
        return sum(map(count_th1, wrap(word,2)))
