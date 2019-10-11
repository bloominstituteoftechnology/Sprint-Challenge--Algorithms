'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    var_length = 2 #"th"
    if len(word) < var_length:
        return 0

    if (word[0 : var_length] == "th"):
        return 1 + count_th(word[var_length - 1:])
    else:
        return count_th(word[var_length - 1:])


    