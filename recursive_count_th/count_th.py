'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    string = "th"  # assigned value of 'th' to variable
    count = len(word)  # length of the input word to a variable
    string_count = len(string)  # length of 'th'

    # if the inputted word doesn't have a value or less than 'th', return 0
    if count == 0 or count < string_count:
        return 0
    # checks if the index of inputted word contains an index with 't' or 'h'
    elif word[0: string_count] == string:
        # returns the occurence of letter
        return count_th(word[string_count - 1:]) + 1
    else:
        return count_th(word[string_count - 1:])


print(count_th('th'))
# global frame ----> count_th(word)
# count_th('th') ----> word: 'th', string = "th", count = 2, string_count = 2
# checks first conditional, not 0 or less than string count so moves on
# returns: count_th(word[string_count - 1:]) + 1 -----> word = "h"
# repeats steps 1-4
# count_th('th') ----> word: 'h', string = "th", count = 1, string_count = 2
# does not pass first conditional statement
# returns 0
# returned overall value = 1
# 'th' occurs once in print(count_th('th'))
