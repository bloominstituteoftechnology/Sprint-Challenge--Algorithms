'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if word == '':
        return 0
    if len(word)>1:
        if word[:2] == 'th':
            less_word = word[1:]
            return 1 + count_th(less_word)
        else:
            less_word = word[1:]
            return 0 + count_th(less_word)
    else:
        return 0
    

print(count_th('abcthxyz'))