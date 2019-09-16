'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    word_leng = len(word)
    if word_leng == 0 or word_leng < 2:
        return 0
    elif word[0:2] == "th":
        return count_th(word[1::]) + 1
    else:
        return count_th(word[1::])
    

   