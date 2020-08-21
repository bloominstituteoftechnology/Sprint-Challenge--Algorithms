'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # Variable that checks to see if 'th' occurs in the word.
    instance = word.find('th')
    # If it does...
    if instance != -1:
        # Return a +1 and the result of running the function again, but two letters ahead of the current position.
        return 1 + count_th(word[instance+2:])
    # If it does not...
    else:
        return 0

    # if word.count('th') > 0:
    #     return word.count('th')
    # else:
    #     return 0
