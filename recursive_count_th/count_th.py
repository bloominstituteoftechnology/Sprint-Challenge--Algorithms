'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # Base case: a word much have 2 or more letters
    if len(word) < 2:
        return 0

    # Check first two letters of word for 'th'
    elif word[0:2] == 'th':
        # Recursive call that slices the first 2 letters
        # off the word each time while counting each occurance of th
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])