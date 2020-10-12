'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
    
def count_th(word):
    
    print(word[:2])
    
    if  len(word) <= 1:
        return 0
    
    elif word[0] == "t":
        if word[1] == "h":
            return 1 + count_th(word[1:])
        else:
            return count_th(word[1:])
    else:
        return count_th(word[1:])
