'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # This find method is useful because it finds the first occurrence of the specified value
        # If it doesn't find the value, it will return -1
        # The value we need to find is "th"
    total = word.find("th")

    # If the 
    if total > 0:
        return count_th(word[total + 2:]) + 1
    return 0
