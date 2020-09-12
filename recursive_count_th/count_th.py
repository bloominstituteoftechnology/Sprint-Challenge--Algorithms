'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    substring = 'th'
    n1 = len(word)
    n2 = len(substring)

    #BASE CASE
    if(n1 == 0 or n1 < n2):
        return 0
    
    #CHECK IF THE FIRST SUBSTRING MATCHES
    if(word[0:n2] == substring):
        return count_th(word[n2 -1:]) + 1
    #OTHERWISE RETURN THE COUNT FROM THE REMAINING INDEX
    return count_th(word[n2 - 1:])
    
    # TBC
    
    
count_th('thean')