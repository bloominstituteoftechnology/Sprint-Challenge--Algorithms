'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # print(word)
    if len(word) < 2:
        return 0
    elif len(word) == 2:
        if word == 'th':
            return 1
        else:
            return 0
    else:
        front = word[:2] #slice of the first two letters
        #print(front)
        if front == 'th':
            back = word[2:] #because if front is th, we can skip the second char
            return 1 + count_th(back)
        else:
            back = word[1:]
            return 0 + count_th(back)