'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    string1 = 't'
    string2 = 'h'
    # # count how many times something occures
    if not word:
        return 0
    elif word[0] == string1 and word[1] == string2:
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])
    # if not word:
    #     return 0
    # return (1 if word[0] == string1 and word[1] == string2 else 0) + count_th(word[1:])
