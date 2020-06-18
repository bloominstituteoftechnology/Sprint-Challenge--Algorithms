'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if len(word) < 2:  # Ignores strings with less than 2 characters.
        return 0
    elif word[:2] == 'th':  # Looks for 'th' in the 1st two indices. 
        return 1 + count_th(word[1:])  # Jumps to the next index.
    else:
        return count_th(word[1:])  # Removes first index. Doesn't add a count.
