'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # making sure input is a string
    word = str(word)
    th = 0

    # check if empty
    if not word:
        return 0

    elif word[0:1] == 'th':
        # return 1 + count_th(word[1:])
        th += 1

    return th
