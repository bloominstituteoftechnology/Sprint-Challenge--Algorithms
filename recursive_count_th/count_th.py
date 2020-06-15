'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # fail with words less then 2 chars in lenght
    if len(word) <= 1:
        return 0

    # check if word has 'th' in it
    if word.find("th") == -1:
        return 0

    else:
        # if none of the above is true get the index where it is found
        idx = word.find("th")
        # set count to 1 + what the function returns
        # start word at idx + 2 / to start at the letter after 'h'
        th_count = 1 + count_th(word[idx + 2:])

        # return value
        return th_count
