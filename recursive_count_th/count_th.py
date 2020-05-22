'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # If the string contains less than 2 characters it cannot contain the 2 character
    # string we are searching for.
    if len(word) < 2:
        return 0
    else:
        # I will walk through the word looking for the characters specified "th" and if I find them I will return 1
        # plus a recursive search through the rest of the string moving forward 2 spaces, otherwise, I will not add
        # 1 to the value and move forward through the string only one space.
        if word[0:2] == 'th':
            return 1 + count_th(word[2:])
        else:
            return count_th(word[1:])
