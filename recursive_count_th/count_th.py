'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) == 0:
        return 0
    
    if word.find("th") == -1:
        return 0
    
    else: 
        index = word.find("th")
        count = 1 + count_th(word[index + 2:])
    
    return count
