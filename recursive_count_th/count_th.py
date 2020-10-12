'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # Verify if the length of the word is not less than "th"; else, it contains it
    
    if len(word) < len('th'):
        return 0

    #Furthermore, verify if the first two letters equals "th", return 1 
    elif word[:2] == 'th':
        return count_th(word[2:]) + 1

    #Else, proceed with the next letter of the word
    else:
        return count_th(word[1:])
