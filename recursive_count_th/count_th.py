'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # account for if word is 1 or 0 characters.
    if len(word) < 2:
        return 0
        
    # check recursively from the end and from the front

    elif 'th' in word[:2]:
        return 1 + count_th(word[1:])

    else:
        return 0 + count_th(word[1:])
