'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # declare length of input
    word_length = (len(word))
    # declare substring we are looking for
    substring = "th"
    # declare length of substring
    substring_length = len(substring)
    # declare a base case to end recursion
    if word_length == 0:
        return 0
    # check if first 2 letters are "th"
    # if true, add 1 to the count -
    # remove first letter and run again on what remains of the string
    if(word[0:substring_length] == substring):
        return count_th(word[1:]) + 1
    # if false remove first letter and run again what remains of the string
    return count_th(word[1:])
