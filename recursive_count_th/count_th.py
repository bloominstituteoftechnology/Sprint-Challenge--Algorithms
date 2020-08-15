'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
# Would've liked to return the recursive depth as the count but that wasn't allowed, so I moved on

    length = len(word)

    if length < 2:
        return 0

    elif 'th' not in word:
        return 0

    else:
        word = word.rpartition('th')
        print(word)
        word = count_th(word[0])

    return word

if __name__ == '__main__':
    print(count_th('seventhth'))