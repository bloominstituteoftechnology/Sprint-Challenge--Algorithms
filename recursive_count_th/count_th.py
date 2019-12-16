'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # if no word passed in
    if not word:
        return 0

    # base case if length of 1 or less, no possibility of finding a 'th'
    if len(word) <= 1:
        return 0

    # look at first 2 positions of string for a 'th'
    if word[0] + word[0+1] == 'th':
        # return count of 1 + recursively passing the string minus 1st 2 chars
        return 1 + count_th(word[2:])
    else:
        # recursively call again minus the first char
        return count_th(word[1:])
