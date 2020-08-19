'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0
    # base case - if the word is less than 2 characters
    if len(word) < 2:
        count += 0
        return count
    # if t and h occur consecutively starting at the beginning count up 1 occurence
    if word[0] == 't' and word[1] == 'h':
        # recursive call will search consecutive occurences beginning at the 2nd index of the last word
        # each recurse will successively shorten the original input, word --recurse--> ord --recurse--> rd
        count += 1
        return count + count_th(word[1:])
    else:
        count += 0
        return count + count_th(word[1:])
