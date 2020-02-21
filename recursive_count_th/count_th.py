'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Check to see if the word is an empty string
    if len(word) == 0:
        return 0
    # Add to count if there's a match
    if word[0:2] == "th":
        return count_th(word[1:]) + 1
    return word.count("th")