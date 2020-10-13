'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # If the overall length of the input word is less than 2, 
    # the word can contain no occurences of our substring
    if len(word) < 2:
        return 0


    # If the input word starts with input, add 1 to count,
    # and continue to count remaining occurences of substring
    elif word[:2] == "th":
        return 1 + count_th(word[1:])

    # Count all occurences of the substring
    # starting from the second index
    else:
        return count_th(word[1:])