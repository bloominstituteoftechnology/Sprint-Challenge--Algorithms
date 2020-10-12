'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word)< 2: # cannot be th if there are less than 2 characters
        return 0
    # TBC
    elif word[:2] == 'th':
        return 1 + count_th(word[1:]) # increment the count by one, go through the rest of the word
    else:
        return count_th(word[1:])#  Move forward


if __name__ == "__main__":
    print(count_th("fifth"))

"""
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
"""