'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # print(word[:2])

    #base case of 2 letters, we cannot recurse any more
    if len(word) == 2:
        if word[:2] == 'th':
            return 1
        else:
            return 0
    # empty string etc
    elif len(word) < 2:
        return 0
    else:
        if word[0:2] == 'th':
            return 1 + count_th(word[1:])
        else:
            return 0 + count_th(word[1:])


# print(count_th('theworldawaits'))