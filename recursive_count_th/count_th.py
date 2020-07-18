'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

"""
U - We're looking to see if the combination of characters "th" occurs within a word. This function must specifically include recursion.

P - We'll need a few things for the recipe.
    1) We'll need a base case where the word is less than 2. In that case, we'd return 0 because you can only have 0 instances of a substring from a string shorter than 2 characters.
    2) We then need to check and see if from the start of the word we have an instance of "th". If so, we recurse and return a counter of some sort.
    3) We can use a new recursive call starting at the next index of "word" to go through the entire word to check it for additional instances of "th".
    
E - 3 cases to deal with. Base case is 0, simple case is 1 plus a recursive call to check the rest of the word.

R - 

"""


def count_th(word):

    # I choose to use a target variable because it enables me to re-use the variable in multiple places.
    # This also will be caught in the linter if I make a typo.
    target = "th"

    # base case - word is less than 2. This will return 0.
    if len(word) < 2:
        return 0

    # check to see if the beginning of the word is a "th" substring.
    if word[:2] == target:
        return count_th(word[1:]) + 1

    # if the beginning of the word is NOT a "th" substring, we want to iterate
    # to the next letter in the word and repeat the process.
    return count_th(word[1:])
