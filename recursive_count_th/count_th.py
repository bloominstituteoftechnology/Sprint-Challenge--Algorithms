'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    substring = 'th'
    l_word = len(word)
    l_substring = len(substring)
    
    # Base Case
    # Two possible situations to end the recursion.
    if l_word == 0 or l_word < l_substring:
        return 0
    
    # Happy fun recursion time!!!!!
    if word[0 : l_substring] == substring:
        return count_th(word[l_substring-1:]) + 1
    
    # Otherwise return the count 
    return count_th(word[l_substring-1:])
    