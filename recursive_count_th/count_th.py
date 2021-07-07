'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    if len(word) < 1:
        return 0
    if len(word) - 1 == False:
        return 0
    if word[0] + word[1] == 'th':
        return 1 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])


# string = "abcthefthghith"

# print(string[1:len(string)-1])


print(count_th("abcthefthghith"))
