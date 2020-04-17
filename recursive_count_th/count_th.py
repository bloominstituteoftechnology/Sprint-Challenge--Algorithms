'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# Understand: 
# count occurences of "th" occur in a word, 
# so I'm counting the occurences of a substring within a string

# Plan:
# iterate through the word using recursion
# check if the beginning first two chars match "th"
# if yes, then add 1 to count
# if no, then add 0 to count
# either way drop the beginning first two chars of the word,
# to simulate iterating through the lengh of the original word

# Execute:
# seems like base case when the len(word) is less than the lenght of "th"

# Reflect:
# How can I improve this? Use one of the python builtins (:


def count_th(word):
    if len(word)<2:
        return 0
    if word[:2]=='th':
        return count_th(word[1:]) + 1
    return count_th(word[1:])

# test = 'thaslth;dfkja;th'
# print(count_th(test))
