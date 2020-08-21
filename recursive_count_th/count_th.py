'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # TBC
    # cant have th if word is less than 2 characters
    if len(word) < 2:
        return 0

    count = 0
    if word[0:2] == "th":
        count += 1

    return count + count_th(word[1:])
