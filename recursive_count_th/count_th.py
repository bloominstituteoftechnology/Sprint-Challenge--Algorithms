'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
# Would've liked to return the recursive depth as the count but that wasn't allowed, so I moved on

    if len(word) < 2:
        return 0

    else:
        if word[0:2] == 'th':
            return 1 + count_th(word[2:])
        else:
            return count_th(word[1:])

if __name__ == '__main__':
    print(count_th('thsevthentht'))