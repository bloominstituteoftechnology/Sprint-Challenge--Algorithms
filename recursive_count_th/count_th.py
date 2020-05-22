'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Base case if the length of the word is zero or less than the string "th"
    # we are done, stop recursing
    if len(word) == 0 or len(word) < len("th"):
        return 0
    
    # if the first two letters does not equal th, recurse removing the first two indices from the word
    if word[:2] != "th":
        return count_th(word[1:])
    # else add 1 and recurse throughout the word removing the first two indices
    else:
        return count_th(word[1:]) + 1