'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    # print(len(word))
    # print(word[-2:])
    # word = word.replace(word[-2:-1], '')
    # print(len(word))
    # print(word[-2:-1])
    print(word)
    '''
        start from end of the word to find last two chars if they are th
        if they are th, count and remove
        if they are not th
            check if 2nd from last is h, 
                if so, remove the last char
            remove the last 2 chars
    '''
    if len(word) <= 1:
        return 0
    elif word[-2:] == 'th':
        # word = word.replace(word[-2:], '')
        word = word[:-2]
        print(f"word: {word} ")
        return 1 + count_th(word)
    elif word[-2:-1] == 'h':
        # word = word.replace(word[-1:], '')
        word = word[:-1]
        return count_th(word)
    else:
        # word = word.replace(word[-2:], '')
        word = word[:-2]
        return count_th(word)


print(count_th('abcthxyz')) # 1
print(count_th('abcthefthghith')) # 3
