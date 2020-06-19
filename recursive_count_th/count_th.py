'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# This solution runs in O(n) time
def count_th(word):
    # Let's check the last two letters of the word
    # If they are "th", remove them and return count_th + 1
    # If not, if the second to last letter isn't h, remove them and return count_th
    # Otherwise, remove only the last letter and return count_th
    # Base case is we have one or less letters left

    if len(word) <= 1:
        return 0
    elif word[-2:] == "th":
        return count_th(word[:-2]) + 1
    elif word[-2] != "h": # this is an optimization, if the second to last letter isn't h, remove it
        return count_th(word[:-2])
    else:
        return count_th(word[:-1]) # otherwise, just remove the last letter, so we can check again for "th"
    
