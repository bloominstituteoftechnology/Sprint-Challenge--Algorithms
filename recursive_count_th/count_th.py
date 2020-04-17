'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC

    wrd_size = len(word)
    ptr = 0

    s = "th"
    str_size = len(s)

    if (word[ptr : str_size] == s):
        return count_th(word[str_size - 1:]) + 1 
    else:
        return count_th(word[wrd_size - 1:])