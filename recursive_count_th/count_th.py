'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    return find_word(word, 0)


def find_word(word, n):
    i = word.find('th')

    if i == -1:
        return n

    word = word[0: i:] + word[i+3::]
    n += 1
    return find_word(word, n)
