'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    index = 0
    counter = 0
    def inner(word):
        nonlocal index
        nonlocal counter
        if index > len(word) - 2:
            return counter
        else:
            if word[0] == 't' and word[1] == 'h':
                counter += 1
            return inner(word[index + 1:])
    inner(word)
    return counter
